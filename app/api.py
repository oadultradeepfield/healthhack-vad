import os
import requests
from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv
from app.voice_activity_analyzer import VoiceActivityAnalyzer

load_dotenv(dotenv_path="../env")

router = APIRouter()
analyzer = VoiceActivityAnalyzer()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/api/analyze")
def analyze_audio_endpoint(download_url: str):
    audio_content = _download_audio(download_url)
    analysis = analyzer.analyze(audio_content)

    server_api_url = os.getenv("SERVER_API_URL")
    if not server_api_url:
        raise HTTPException(
            status_code=500, detail="SERVER_API_URL not set in the environment"
        )

    # _forward_analysis(analysis.model_dump(), server_api_url)
    return analysis


def _download_audio(download_url: str) -> bytes:
    """
    Downloads audio from the specified URL.
    Raises an HTTPException (400) if the download fails.
    """
    try:
        response = requests.get(download_url)
        response.raise_for_status()
        return response.content
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Could not download voice: {e}")


def _forward_analysis(analysis: dict, server_api_url: str):
    """
    Forwards the analysis data to the server API.
    Raises an HTTPException (500) if the request fails.
    """
    try:
        forward_response = requests.post(server_api_url, json=analysis)
        forward_response.raise_for_status()
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error sending analysis to server endpoint: {e}"
        )
