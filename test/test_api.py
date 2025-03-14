import pytest
from fastapi.testclient import TestClient
from app.main import create_app
from test.test_voice_activity_analyzer import create_composite_audio

app = create_app()
client = TestClient(app)


@pytest.fixture(autouse=True)
def patch_requests(monkeypatch):
    monkeypatch.setattr("app.api.requests.get", _fake_requests_get)
    monkeypatch.setattr("app.api.requests.post", _fake_requests_post)


@pytest.fixture(autouse=True)
def patch_environment(monkeypatch):
    # The correctness of server api url is not important
    # since every POST requests are replaced by the fake one
    # This code is used to by pass the None value in the testing environment
    monkeypatch.setenv("SERVER_API_URL", "http://fake-server-api.com")


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_analyze_endpoint():
    # Again, the correctness of audio url is not important
    # since every GET requests are replaced by the fake one
    test_audio_url = "http://fakeaudio.com/test.wav"
    response = client.post(
        "/api/analyze",
        json={
            "download_url": test_audio_url,
            "should_return": True,
            "history_id": "9999",
        },
    )
    assert response.status_code == 200
    data = response.json()
    keys = [
        "history_id",
        "total_duration",
        "total_speech_duration",
        "total_pause_duration",
        "num_speech_segments",
        "num_pauses",
        "answer_delay_duration",
        "speech_segments",
        "pause_segments",
    ]
    for key in keys:
        assert key in data


def _fake_requests_get(url, **kwargs):
    class FakeResponse:
        status_code = 200
        content = create_composite_audio()

        def raise_for_status(self):
            pass

    return FakeResponse()


def _fake_requests_post(url, json, **kwargs):
    class FakeResponse:
        status_code = 200

        def raise_for_status(self):
            pass

    return FakeResponse()
