from fastapi import FastAPI

app = FastAPI(
    title="Feedback Form API",
    description="API for the feedback form popup MultitudeX technical test",
    docs_url="/"
)

@app.get("/")
async def helloWorld():
    return {"message": "Hello World!"}