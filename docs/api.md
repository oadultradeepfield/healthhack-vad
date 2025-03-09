# API Documentation

This document provides information about the available API endpoints.

## Base URL

All API endpoints are relative to your server's base URL.

## Endpoints

| Method | URL        | Description                            | Parameters                        | Returns                        |
| ------ | ---------- | -------------------------------------- | --------------------------------- | ------------------------------ |
| GET    | `/health`  | Check if the service is operational    | None                              | Status object                  |
| POST   | `/analyze` | Analyze audio file from a download URL | `download_url` (string, required) | Voice activity analysis object |

## API Reference

### Health Check

| Request       | Response           |
| ------------- | ------------------ |
| `GET /health` | `{"status": "ok"}` |

### Analyze Audio

| Request         | Required Parameters     | Response    |
| --------------- | ----------------------- | ----------- |
| `POST /analyze` | `download_url` (string) | Shown below |

```json
{
  "total_duration": 120.5,
  "total_speech_duration": 85.2,
  "total_pause_duration": 35.3,
  "num_speech_segments": 12,
  "num_pauses": 11,
  "answer_delay_duration": 1.8,
  "speech_segments": [
    {
      "start_time": 0.5,
      "end_time": 10.2,
      "duration": 9.7
    },
    ...
  ],
  "pause_segments": [
    {
      "start_time": 10.2,
      "end_time": 15.5,
      "duration": 5.3
    },
    ...
  ]
}
```

## Error Codes

| Error Codes | Description                                                     |
| ----------- | --------------------------------------------------------------- |
| 400         | Bad Request - Invalid URL or unreachable download URL           |
| 500         | Internal Server Error - Environment variables not set correctly |

## Environment Variables

| Name             | Description                         | Required |
| ---------------- | ----------------------------------- | -------- |
| `SERVER_API_URL` | URL for forwarding analysis results | Yes      |
