from pydantic import BaseModel

class VideoProcessResponse(BaseModel):
    transcription: str
    summary: str


class ErrorResponse(BaseModel):
    message: str