from fastapi import FastAPI
from app.routers import calculator

app = FastAPI()

app.include_router(calculator.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[*],  # Replace with your frontend's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Calculator!!!!"}
