from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_read():
    return {"hello":"world"}