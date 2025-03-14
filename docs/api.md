# API Documentation

This document provides detailed information about the available API endpoints, including request methods, parameters, responses, and error codes.

## Base URL

All API endpoints are relative to the service's base URL.

## Endpoints

### Health Check

- **Method:** `GET`
- **URL:** `/health`
- **Description:** Checks if the service is operational.
- **Parameters:** None
- **Response:**
  ```json
  {
    "status": "ok"
  }
  ```

### Analyze Audio

- **Method:** `POST`
- **URL:** `/api/analyze`
- **Description:** Analyzes an audio file from a provided download URL.
- **Request Body:**
  - `download_url` (string, required): The URL of the audio file to analyze.
  - `should_return` (boolean, required): The flag to indicate whether the analysis result should be returned back to the client (set to `false` in production).
  - `history_id` (string: UUID, required): The corresponding history ID to put in the database.
  - Example body in JSON format:
    ```javascript
    {
      "download_url": "<download_url>",
      "should_return": false
      "history_id": "<history_id>"
    }
    ```
- **Response (If `should_return` is `true`):**

  Example response in JSON format:

  ```javascript
  {
    "history_id": "1f020d38-6f1b-465c-b476-a31ae153b469"
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
      }
      // Additional segments...
    ],
    "pause_segments": [
      {
        "start_time": 10.2,
        "end_time": 15.5,
        "duration": 5.3
      }
      // Additional segments...
    ]
  }
  ```

## Error Codes

| Code | Description                                                      |
| ---- | ---------------------------------------------------------------- |
| 400  | Bad Request - Invalid URL or unreachable download URL.           |
| 500  | Internal Server Error - Environment variables not set correctly. |

## Environment Variables

| Name             | Description                         | Required |
| ---------------- | ----------------------------------- | -------- |
| `SERVER_API_URL` | URL for forwarding analysis results | Yes      |
