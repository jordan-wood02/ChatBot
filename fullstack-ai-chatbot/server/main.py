from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv
from src.routes.chat import chat

load_dotenv()

api = FastAPI()
api.include_router(chat)

# Simple test route to test the API


@api.get("/test")
async def root():
    return {"msg": "API is Online"}

# Set up development server
# API will run on local port 3500
if __name__ == "__main__":
    if os.environ.get('APP_ENV') == "development":
        uvicorn.run("main:api", host="0.0.0.0", port=3500,
                    workers=4, reload=True)
    else:
        pass
