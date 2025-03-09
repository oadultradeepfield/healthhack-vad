import io
from pydub import AudioSegment, silence
from app.models import VoiceActivityAnalysis


class VoiceActivityAnalyzer:
    def __init__(self, noise_sample_duration=1000, offset=10, min_pause_len=500):
        self.noise_sample_duration = noise_sample_duration
        self.offset = offset
        self.min_pause_len = min_pause_len

    def analyze(self, audio_bytes: bytes) -> VoiceActivityAnalysis:
        audio = self._load_audio(audio_bytes)
        total_duration = len(audio) / 1000.0

        adaptive_threshold = self._calculate_adaptive_threshold(audio)
        initial_speech = self._detect_speech_segments(audio, adaptive_threshold)
        answer_delay_duration = self._calculate_answer_delay(initial_speech)

        speech_segments = self._extract_speech_segments(
            audio, answer_delay_duration, adaptive_threshold
        )
        pause_segments = self._extract_pause_segments(speech_segments)

        total_speech_duration = sum(speech["duration"] for speech in speech_segments)
        total_pause_duration = sum(pause["duration"] for pause in pause_segments)

        return VoiceActivityAnalysis(
            total_duration=total_duration,
            total_speech_duration=total_speech_duration,
            total_pause_duration=total_pause_duration,
            num_speech_segments=len(speech_segments),
            num_pauses=len(pause_segments),
            answer_delay_duration=answer_delay_duration,
            speech_segments=speech_segments,
            pause_segments=pause_segments,
        )

    def _load_audio(self, audio_bytes: bytes) -> AudioSegment:
        """Loads an audio segment from bytes."""
        return AudioSegment.from_file(io.BytesIO(audio_bytes))

    def _calculate_adaptive_threshold(self, audio: AudioSegment) -> float:
        """Calculates the adaptive silence threshold based on a baseline noise sample."""
        baseline_segment = audio[: self.noise_sample_duration]
        noise_floor = baseline_segment.dBFS
        return noise_floor + self.offset

    def _detect_speech_segments(self, audio: AudioSegment, threshold: float) -> list:
        """Detects speech segments in the audio using the given threshold."""
        return silence.detect_nonsilent(
            audio, min_silence_len=self.min_pause_len, silence_thresh=threshold
        )

    def _calculate_answer_delay(self, speech_segments: list) -> float:
        """
        Determines the answer delay as the start time of the first speech segment.
        Returns 0.0 if no speech segment is detected.
        """
        if speech_segments:
            return speech_segments[0][0] / 1000.0
        return 0.0

    def _extract_speech_segments(
        self, audio: AudioSegment, delay: float, threshold: float
    ) -> list:
        """
        Extracts speech segments from the audio after the answer delay.
        Returns a list of dictionaries with start_time, end_time, and duration.
        """
        start_ms = int(delay * 1000)
        audio_slice = audio[start_ms:]
        speech_after = self._detect_speech_segments(audio_slice, threshold)
        segments = []

        for seg in speech_after:
            seg_start = (seg[0] / 1000.0) + delay
            seg_end = (seg[1] / 1000.0) + delay
            duration = seg_end - seg_start
            segments.append(
                {"start_time": seg_start, "end_time": seg_end, "duration": duration}
            )

        return segments

    def _extract_pause_segments(self, speech_segments: list) -> list:
        """
        Given a list of speech segments, calculates the pauses (silences) between them.
        Returns a list of pause segments with start_time, end_time, and duration.
        """
        pauses = []
        for i in range(1, len(speech_segments)):
            pause_start = speech_segments[i - 1]["end_time"]
            pause_end = speech_segments[i]["start_time"]
            duration = pause_end - pause_start
            if pause_end > pause_start:
                pauses.append(
                    {
                        "start_time": pause_start,
                        "end_time": pause_end,
                        "duration": duration,
                    }
                )

        return pauses
