from fastapi import FastAPI
from app.api import router
import uvicorn


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    return app


def main():
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()
