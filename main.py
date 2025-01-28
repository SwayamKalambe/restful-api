from fastapi import FastAPI
from routes import router
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()



app.include_router(router)

@app.get("/")
def cover_page():
    return "Welcome to the API"






