"""Main application entrypoint."""

from fastapi import FastAPI

app = FastAPI(title="Smart Agriculture AI")


@app.get("/")
def read_root() -> dict:
    return {"message": "Smart Agriculture AI API is running"}
