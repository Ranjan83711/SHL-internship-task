from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from preprocessing.text_builder import build_documents
from preprocessing.chunker import chunk_documents
from retrieval.retriever import retrieve_chunks
from retrieval.ranker import rank_results
from utils.parser import parse_assessment_text


# -------------------------------------------------
# FastAPI App
# -------------------------------------------------
app = FastAPI(
    title="Assessment Recommendation API",
    description="Semantic recommendation API for SHL assessments",
    version="1.0"
)


# -------------------------------------------------
# Request & Response Schemas
# -------------------------------------------------
class RecommendRequest(BaseModel):
    query: str
    top_k: int = 5


class AssessmentResponse(BaseModel):
    name: str
    type: str
    skills: str
    roles: str
    duration: str        # ✅ STRING (fixes error)
    description: str


class RecommendResponse(BaseModel):
    query: str
    recommendations: List[AssessmentResponse]


# -------------------------------------------------
# Load Data ONCE (important for performance)
# -------------------------------------------------
documents = build_documents()
chunks = chunk_documents(documents)


# -------------------------------------------------
# API Endpoint
# -------------------------------------------------
@app.post("/recommend", response_model=RecommendResponse)
def recommend_assessments(request: RecommendRequest):

    results = retrieve_chunks(
        request.query,
        chunks,
        top_k=request.top_k
    )

    ranked_results = rank_results(results)

    recommendations = []

    for result in ranked_results:
        parsed = parse_assessment_text(result)
        if not parsed:
            continue

        recommendations.append({
            "name": parsed.get("name", ""),
            "type": parsed.get("type", ""),
            "skills": parsed.get("skills", ""),
            "roles": parsed.get("roles", ""),
            "duration": parsed.get("duration", ""),   # stays string
            "description": parsed.get("description", "")
        })

    return {
        "query": request.query,
        "recommendations": recommendations
    }
