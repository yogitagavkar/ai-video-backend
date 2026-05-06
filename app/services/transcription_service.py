from openai import OpenAI

client = OpenAI()

def transcribe_audio(file_path):
    with open(file_path, "rb") as f:
        response = client.audio.transcriptions.create(
            model="gpt-4o-transcribe",
            file=f
        )
    return response.text