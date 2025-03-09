FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PORT=8080

WORKDIR /app

RUN apt update && apt install -y ffmpeg && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8080

CMD ["uvicorn", "app.main:create_app", "--host", "0.0.0.0", "--port", "8080"]
