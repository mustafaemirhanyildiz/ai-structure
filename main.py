import uvicorn

from fastapi import Depends, FastAPI
from controllers import GptController


app = FastAPI()

app.include_router(GptController.router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5231)
