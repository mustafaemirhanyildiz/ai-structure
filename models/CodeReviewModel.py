from pydantic import BaseModel

class CodeReviewModel(BaseModel):
    code: str
