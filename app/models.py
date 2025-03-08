from pydantic import BaseModel


class VoiceActivityAnalysis(BaseModel):
    total_duration: float
    total_speech_duration: float
    total_pause_duration: float
    num_speech_segments: int
    num_pauses: int
    answer_delay_duration: float
    speech_segments: list
    pause_segments: list
