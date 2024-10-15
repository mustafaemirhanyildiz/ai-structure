import uvicorn
from dotenv import load_dotenv
from openai import OpenAI
import os
from fastapi import Depends, FastAPI
from controllers import GptController

load_dotenv()

app = FastAPI()

gpt_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app.include_router(GptController.router, prefix="/api", dependencies=[Depends(lambda: gpt_client)])

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5231)
