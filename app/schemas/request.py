from pydantic import BaseModel

class VideoProcessRequest(BaseModel):
    title: str | None = None


class AIInferenceRequest(BaseModel):
    text: str