from fastapi import APIRouter
from pydantic import BaseModel
from agent.sql_chain import run_pipeline

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

@router.post("/query")
def run_query(req: QueryRequest):
    return run_pipeline(req.question)