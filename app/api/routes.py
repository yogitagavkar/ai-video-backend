from fastapi import APIRouter, UploadFile, File
from app.services.video_service import save_video
from app.services.transcription_service import transcribe_audio
from app.services.ai_service import summarize_text
from app.schemas.response import VideoProcessResponse
from app.services.video_service import extract_audio

router = APIRouter()

@router.post("/process-video", response_model=VideoProcessResponse)
async def process_video(file: UploadFile = File(...)):

    video_path = save_video(file)
    audio_path = extract_audio(video_path)

    text = transcribe_audio(audio_path)
    summary = summarize_text(text)

    return VideoProcessResponse(
        transcription=text,
        summary=summary
    )