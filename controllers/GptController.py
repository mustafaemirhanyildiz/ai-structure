from fastapi import APIRouter, Body, Query
from services.CodeReviewService import review_code_for_clean_principles
from models.CodeReviewModel import CodeReviewModel

router = APIRouter()

@router.post("/chatWithGpt")
def chat_with_gpt_endpoint(input: CodeReviewModel = Query(...)):
    response = review_code_for_clean_principles(input)
    return response