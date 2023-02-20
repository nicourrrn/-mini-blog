from fastapi import FastAPI
from fastapi import APIRouter

app = FastAPI()


@app.get('/')
def main():
    return {"response": "Hello from my app"}


