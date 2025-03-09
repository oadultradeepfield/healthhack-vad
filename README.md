# HealthHack VAD Services

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)

This Voice Activity Detection (VAD) service was developed for [HealthHack 2025](https://healthhack.sg/). It analyzes recorded speech to detect pause durations, number of pauses, pause locations, speech segment length, and response delays, which are factors associated with cognitive decline.

The service processes conversations between an AI agent and users, helping identify early signs of dementia in older adults or track changes in user response patterns over time.

![Simplified Sequence Diagram](/figure/simplified_sequence_diagram.png)

**Note**: This repository contains the code for the highlighted section of the simplified sequence diagram. The rest of the backend, developed by another team member, can be found [here](https://github.com/CATISNOTSODIUM/healthhack-backend).

## Development Roadmap

- [x] Develop an audio processing pipeline to convert recorded speech (.wav) into structured data.
- [x] Implement pause detection and speech metrics analysis, sending results to the Go server for database actions.
- [x] Create a FastAPI service to receive the audio file URLs from mobile app requests.
- [ ] Containerize the service with Docker and deploy it on Google Cloud Run for mobile app testing.

## Local Development Guide

1. **Clone the repository** and ensure Python is installed (preferably version 3.11). Then, install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run tests** after making any changes to verify everything still works:

   ```bash
   pytest
   ```

   These tests will also run automatically when you push code to GitHub or create a pull request as part of the CI workflow.

3. **Build and run the app with Docker**:

   ```bash
   docker build -t healthhack-vad .
   docker run --env-file .env -d --name healthhack-vad -p 8080:8080 healthhack-vad:latest
   ```

   Ensure you have set up your environment variables in the `.env` file. Refer to [`.env.example`](/.env.example) for guidance.

**Note:** Make sure `ffmpeg` (or an equivalent tool) is installed on your machine for `pydub` to function properly. See the installation guide [here](https://github.com/adaptlearning/adapt_authoring/wiki/installing-ffmpeg) for your operating system.

## API Reference

This service provides the following API endpoints:

| Method | URL        | Description            |
| ------ | ---------- | ---------------------- |
| GET    | `/health`  | Health check endpoint  |
| POST   | `/analyze` | Analyze audio from URL |

For complete API documentation including request/response formats, please see the [API Documentation](./docs/api.md).

## License

This project is licensed under the MIT License. See the [LICENSE](/LICENSE) file for details.
