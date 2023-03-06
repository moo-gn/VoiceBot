import discord
from discord.ext import commands
import datetime

import sys
sys.path.append("..")
import credentials

from voice_utils import get_transcript_from_audio_data

bot = discord.Bot(case_insensitive = True, intents=discord.Intents.all())
connections = {}


class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    def __init__(self, ctx, vc):
        super().__init__()
        self.ctx = ctx
        self.vc = vc
    @discord.ui.button(label="Start", style=discord.ButtonStyle.primary, emoji="🔴")
    async def start(self, button, interaction):
        await interaction.response.edit_message(content = "recording....")   
        self.vc.start_recording(
            discord.sinks.WaveSink(),  # The sink type to use.
            once_done,  # What to do once done.
            self.ctx.channel  # The channel to disconnect from.
        )

    @discord.ui.button(label="Stop", style=discord.ButtonStyle.primary, emoji="⬜")
    async def stop(self, button, interaction):
        if self.ctx.guild.id in connections:  # Check if the guild is in the cache.
            self.vc = connections[self.ctx.guild.id]
            self.vc.stop_recording()  # Stop recording, and call the callback (once_done).
            await interaction.response.edit_message(content = "You Can Started recording!",  view=MyView(self.ctx,self.vc))
        else:
            await self.ctx.respond("I am currently not recording here.")  # Respond with this if we aren't recording.



async def once_done(sink: discord.sinks, channel: discord.TextChannel, *args):  # Our voice client already passes these in.
    msg = await channel.send("Wait...")
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

    transcript = get_transcript_from_audio_data(input_audio_data)

    await msg.edit(f"finished recording audio for: {', '.join(recorded_users)}.")  # Send a message with the accumulated files.
    await channel.send(f"Transcript:\n{transcript}")  # Send a message with the accumulated files.


#say hello
@bot.slash_command(guild_ids=[credentials.guild_id] , description="Join")
async def join(ctx :discord.context):
    if not ctx.author.voice:
        await ctx.respond("You aren't in a voice channel!")
        
    vc = await ctx.author.voice.channel.connect()  # Connect to the voice channel the author is in.
    connections.update({ctx.guild.id: vc})  # Updating the cache with the guild and channel.
    await ctx.respond("You Can Started recording!", view = MyView(ctx, vc))





@bot.slash_command(guild_ids=[credentials.guild_id] , description="Leave")
async def leave(ctx):
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
    print('We have logged in as {0.user}'.format(bot) + ' ' + datetime.datetime.utcnow().strftime("%m/%d/%Y %H:%M:%S UTC"))

bot.run(credentials.VOICE_BOT_TOKEN)