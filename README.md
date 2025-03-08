# HealthHack VAD Services

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)

This Voice Activity Detection (VAD) service was developed for [HealthHack 2025](https://healthhack.sg/). It analyzes recorded speech to detect pause durations, number of pauses, pause locations, speech segment length, and response delays, which are factors associated with cognitive decline.

The service processes conversations between an AI agent and users, helping identify early signs of dementia in older adults or track changes in user response patterns over time.

![Simplified Sequence Diagram](/figure/simplified_sequence_diagram.png)

**Note**: This repository contains the code for the highlighted section of the simplified sequence diagram. The rest of the backend, developed by another team member, can be found [here](https://github.com/CATISNOTSODIUM/healthhack-backend).

## Development Roadmap

- [ ] Build an audio processing pipeline to convert recorded speech (.wav) into structured data.
- [ ] Implement pause detection and related speech metrics analysis.
- [ ] Develop lightweight machine learning models to compare metrics against user history.
- [ ] Create a FastAPI service to integrate all components and return analysis results.
- [ ] Containerize with Docker and deploy on Google Cloud Run for mobile app testing.

## Getting Started

To be updated.

## API Documentation

To be updated.

## License

This project is licensed under the MIT License. See the [LICENSE](/LICENSE) file for details.
