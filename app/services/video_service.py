import os
import subprocess

UPLOAD_DIR = "uploads"

def save_video(file):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    
    return file_path


def extract_audio(video_path):
    audio_path = video_path.replace(".mp4", ".mp3").replace(".mov", ".mp3")

    command = [
        "ffmpeg",
        "-i", video_path,
        "-vn",              # no video
        "-acodec", "mp3",
        audio_path
    ]

    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    return audio_path