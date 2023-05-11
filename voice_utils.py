from whisper import Whisper

# Create Whisper class instance
model = Whisper()

def transcript_to_string(transcript: list) -> str:
    result = ""
    for line in transcript:

        result += "{}: {} [{} - {}]\n".format(
            line["user_id"],
            line["text"],
            line["start"],
            line["end"]
        )

    return result


def get_transcript_from_audio_data(audio_data: dict) -> str:

    all_transcripts = []

    for user_id, audio_file in audio_data.items():

        transcription = model.get_transcription(audio_file)

        for segment in transcription["segments"]:

            all_transcripts.append({
                "user_id": user_id,
                "start": segment["start"],
                "end": segment["end"],
                "text": segment["text"]
            })

    all_transcripts.sort(
        key=lambda x: x["start"]
    )

    return transcript_to_string(all_transcripts)
