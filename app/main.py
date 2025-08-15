from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
from .retrieval import retrieve_similar
from .generation import generate_reply

app = FastAPI(
    title="Email Reply Drafter API",
    description="An AI-powered API that generates professional customer support replies based on similar past interactions",
    version="1.0.0"
)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Query(BaseModel):
    text: str

@app.get("/")
def root():
    """Root endpoint with API information"""
    return {
        "message": "Email Reply Drafter API",
        "description": "AI-powered customer support reply generation",
        "endpoints": {
            "POST /draft_reply": "Generate a reply for a customer query",
            "GET /docs": "Interactive API documentation (Swagger UI)",
            "GET /redoc": "Alternative API documentation"
        },
        "usage": "Send a POST request to /draft_reply with a JSON body containing 'text' field"
    }

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "Email Reply Drafter API"}

@app.post("/draft_reply")
def draft_reply(query: Query):
    try:
        logger.info(f"Received query: {query.text[:50]}...")  # Log truncated for brevity
        contexts = retrieve_similar(query.text)
        reply = generate_reply(query.text, contexts)
        return {"reply": reply}
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")