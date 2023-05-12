import discord
from whisper import Whisper
from chatgpt import ChatGPT

# Constants
TIMEOUT_IN_SECS = 30
DISCORD_MAX_CHARS = 1500

# Create instance of ChatGPT
chatgpt = ChatGPT()

# Create Whisper class instance
whisper = Whisper()


async def ask_chatgpt(user_id: int, prompt: str, channel: discord.TextChannel) -> None:
    """Asks ChatGPT the prompted question

    Args:
        user_id (int): User Discord ID
        message (str): Question passed to ChatGPT
        channel (discord.TextChannel): Text channel to send response to
    """

    response = chatgpt.ask(user_id, prompt)
    await send_response(user_id, channel, response)


async def send_response(user_id: int, channel: discord.TextChannel, response: str) -> None:
    """Sends ChatGPT response in chat. If the message is long it divides it into sections.

    Args:
        user_id (int): User Discord ID
        channel (discord.TextChannel): Text Channel to send response in
        response (str): Response to message
    """
    
    # Message to reply to if response is over the discord text limit
    message = None

    # While we are processing the response slice it to fit into discord message limit
    while response:
        index = DISCORD_MAX_CHARS if len(response) <= DISCORD_MAX_CHARS else response[:DISCORD_MAX_CHARS].rindex(" ")
        to_send = response[:index]
        response = response[index:]
        # Send the intial message
        if not message:
            message = await channel.send(f"<@{user_id}> {to_send}")
        # Reply to the message
        else:
            await message.reply(to_send)

async def answer_prompts(transcripts: list, channel: discord.TextChannel) -> None:
    """Answer user prompts and send responses in the given text channel

    Args:
        transcripts (list): List of dictionaries of transcripts
        channel (discord.TextChannel): Discord Text Channel to send response to
    """
    
    # For each transcript answer
    for transcript in transcripts:
        await ask_chatgpt(transcript['user_id'], transcript['text'], channel)



def get_transcripts_from_audio_data(audio_data: dict) -> list:
    """Transforms discord audio to string using Whisper API

    Args:
        audio_data (dict): Audio data in format {user: user_audio}

    Returns:
        list: list of dictionaries of each user ID and qustion
    """

    all_transcripts = []

    for user_id, audio_file in audio_data.items():

        transcription = whisper.get_transcription(audio_file)

        for segment in transcription["segments"]:

            all_transcripts.append({
                "user_id": user_id,
                "text": segment["text"]
            })

    return all_transcripts
