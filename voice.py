import discord
from discord.ext import commands
import datetime

import sys
sys.path.append("..")
import credentials

bot = discord.Bot(case_insensitive = True, intents=discord.Intents.all())
connections = {}

async def once_done(sink: discord.sinks, channel: discord.TextChannel, *args):  # Our voice client already passes these in.
    recorded_users = [  # A list of recorded users
        f"<@{user_id}>"
        for user_id, audio in sink.audio_data.items()
    ]
    await sink.vc.disconnect()  # Disconnect from the voice channel.
    files = [discord.File(audio.file, f"{user_id}.{sink.encoding}") for user_id, audio in sink.audio_data.items()]  # List down the files.
    await channel.send(f"finished recording audio for: {', '.join(recorded_users)}.", files=files)  # Send a message with the accumulated files.

#say hello
@bot.slash_command(guild_ids=[credentials.guild_id] , description="start")
async def start(ctx :discord.context):
    voice = ctx.author.voice

    if not voice:
        await ctx.respond("You aren't in a voice channel!")

    vc = await voice.channel.connect()  # Connect to the voice channel the author is in.
    connections.update({ctx.guild.id: vc})  # Updating the cache with the guild and channel.

    vc.start_recording(
        discord.sinks.WaveSink(),  # The sink type to use.
        once_done,  # What to do once done.
        ctx.channel  # The channel to disconnect from.
    )
    await ctx.respond("Started recording!")





@bot.slash_command(guild_ids=[credentials.guild_id] , description="stop")
async def stop(ctx):
    if ctx.guild.id in connections:  # Check if the guild is in the cache.
        vc = connections[ctx.guild.id]
        vc.stop_recording()  # Stop recording, and call the callback (once_done).
        del connections[ctx.guild.id]  # Remove the guild from the cache.
        await ctx.delete()  # And delete.
    else:
        await ctx.respond("I am currently not recording here.")  # Respond with this if we aren't recording.



#login event
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot) + ' ' + datetime.datetime.utcnow().strftime("%m/%d/%Y %H:%M:%S UTC"))

bot.run(credentials.Music_Test)