from fastapi import FastAPI

app = FastAPI(
    title="QuantumScape Genealogy API Demo",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {"message": "QuantumScape genealogy API"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.get("/units/{unit_id}/ancestors")
async def get_ancestors(
    unit_id: str,
    max_depth: int = 20,
):
    return {
        "unit_id": unit_id,
        "max_depth": max_depth,
        "ancestors": [],
    }
