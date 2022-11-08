from fastapi import FastAPI
from app.calculator.router import router as calculator_router

def create_app():
    app = FastAPI()
    app.include_router(calculator_router)

    return app

app = create_app()
