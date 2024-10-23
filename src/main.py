from fastapi import FastAPI

app = FastAPI(
    title="Task Collab API"
)

@app.get("/")
def home():
    return "hello word"