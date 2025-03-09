import io
import pytest
from pydub.generators import Sine
from app.voice_activity_analyzer import VoiceActivityAnalyzer


def test_audio_processor_composite():
    audio_bytes = create_composite_audio()
    processor = VoiceActivityAnalyzer(
        noise_sample_duration=1000, offset=10, min_pause_len=500
    )
    result = processor.analyze(audio_bytes)
    assert abs(result.answer_delay_duration - 2.0) < 0.2
    assert result.num_speech_segments == 2
    assert abs(result.total_speech_duration - 2.5) < 0.3
    assert result.num_pauses == 1
    assert abs(result.total_pause_duration - 1.0) < 0.2
    assert abs(result.total_duration - 6.5) < 0.2


def create_composite_audio():
    initial_silence = Sine(440).to_audio_segment(duration=2000).apply_gain(-40)
    speech1 = Sine(440).to_audio_segment(duration=1000)
    pause = Sine(440).to_audio_segment(duration=1000).apply_gain(-40)
    speech2 = Sine(440).to_audio_segment(duration=1500)
    trailing_silence = Sine(440).to_audio_segment(duration=1000).apply_gain(-40)
    composite = initial_silence + speech1 + pause + speech2 + trailing_silence
    buf = io.BytesIO()
    composite.export(buf, format="wav")
    return buf.getvalue()
