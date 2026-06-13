from fastapi import FastAPI

app = FastAPI(
    title="Enterprise Deep Research Agent"
)


@app.get("/")
def health_check():
    return {
        "status": "running"
    }