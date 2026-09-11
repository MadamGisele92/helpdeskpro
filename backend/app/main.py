from fastapi import FastAPI

app = FastAPI(
    title="HelpDeskPro API",
    description="IT service desk API for managing support tickets and IT operations.",
    version="0.1.0",
)


@app.get("/api/health", tags=["System"])
def health_check() -> dict[str, str]:
    """Return the current API health status."""
    return {"status": "healthy", "service": "HelpDeskPro API"}
