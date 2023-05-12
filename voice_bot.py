import discord
import datetime
from credentials import DISCORD_BOT_TOKEN
from utils import get_transcripts_from_audio_data, answer_prompts

# Init bot
bot = discord.Bot(case_insensitive = True, intents=discord.Intents.all())
connections = {}

class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    """a class that subclasses discord.ui.View that will display buttons to control the bot
    """
    def __init__(self, ctx, vc):
        super().__init__(timeout=None)
        self.ctx = ctx
        self.vc = vc
        
    # Button that starts recording
    @discord.ui.button(label="Start", style=discord.ButtonStyle.primary, emoji="🔴")
    async def start(self, button, interaction):
        await interaction.response.edit_message(content = "recording....")   
        self.vc.start_recording(
            discord.sinks.WaveSink(),  # The sink type to use.
            once_done,  # callback function after recording is finished.
            self.ctx.channel  # The channel to disconnect from.
        )

    # Button that stops recording
    @discord.ui.button(label="Stop", style=discord.ButtonStyle.primary, emoji="⬜")
    async def stop(self, button, interaction):
        if self.ctx.guild.id in connections:  # Check if the guild is in the cache.
            self.vc = connections[self.ctx.guild.id]
            self.vc.stop_recording()  # Stop recording, and call the callback (once_done).
            await interaction.response.edit_message(content = "You Can Start recording!",  view=MyView(self.ctx,self.vc))
        else:
            await self.ctx.respond("I am currently not recording here.")  # Respond with this if we aren't recording.



async def once_done(sink: discord.sinks, channel: discord.TextChannel):
    """Callback function after recording is finished. Process audio input and pass it to chatGPT, then send response in chat.

    Args:
        sink (discord.sinks): Audio Sink
        channel (discord.TextChannel): Channel to send reponse in
    """
    msg = await channel.send("Creating response...")
    # Filter bots out
    for user_id in list(sink.audio_data.keys()):
        user = await bot.fetch_user(user_id)
        if user.bot:
            del sink.audio_data[user_id]

    recorded_users = [  # A list of recorded users
        f"<@{user_id}>"
        for user_id, _ in sink.audio_data.items()
    ]

    # Prepare files for transcription
    input_audio_data = {
        f"<@{user_id}>": audio.file
        for user_id, audio in sink.audio_data.items()
    }

    # Get all transcripts of prompts
    transcripts = get_transcripts_from_audio_data(input_audio_data)
    await msg.edit(f"finished recording prompts for: {', '.join(recorded_users)}.")  # Send a message to notify that recording finished.
    
    # Send prompt responses
    await answer_prompts(transcripts, channel) # Sends answers for users prompts



#say hello
@bot.slash_command(description="Join")
async def join(ctx: discord.context):
    """Command join that lets the bot join the voice channel

    Args:
        ctx (discord.context): Discord Context
    """
    # If the user calling the bot is not in voice channel
    if not ctx.author.voice:
        await ctx.respond("You aren't in a voice channel!")
        
    vc = await ctx.author.voice.channel.connect()  # Connect to the voice channel the author is in.
    connections.update({ctx.guild.id: vc})  # Updating the cache with the guild and channel.
    # Send recording view
    await ctx.respond("You Can Start recording!", view = MyView(ctx, vc))





@bot.slash_command(description="Leave")
async def leave(ctx: discord.context):
    """Command leave that lets the bot leave the voice channel

    Args:
        ctx (discord.context): Discord context
    """
    if ctx.guild.id in connections:  # Check if the guild is in the cache.
        vc = connections[ctx.guild.id]
        await vc.disconnect()  # Disconnect from the voice channel.
        del connections[ctx.guild.id]  # Remove the guild from the cache.
        await ctx.delete()  # And delete.
    else:
        await ctx.respond("I am currently not Connected")  # Respond with this if we aren't recording.



#login event
@bot.event
async def on_ready():
    """Prints message to console once we successfully load the bot
    """
    print('We have logged in as {0.user}'.format(bot) + ' ' + datetime.datetime.utcnow().strftime("%m/%d/%Y %H:%M:%S UTC"))

# Run bot
bot.run(DISCORD_BOT_TOKEN)