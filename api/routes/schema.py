from fastapi import APIRouter
from agent.semantic_layer import SEMANTIC_LAYER
router = APIRouter()

@router.get("/schema")
def get_schema():
    return SEMANTIC_LAYER