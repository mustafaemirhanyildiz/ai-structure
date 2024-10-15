from fastapi import APIRouter, Depends
from services.CodeReviewService import review_code_for_clean_principles

router = APIRouter()

@router.post("/chatWithGpt")
def chat_with_gpt_endpoint(userInput: str):
    response = review_code_for_clean_principles(userInput)
    return response