from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "¡Hola FastAPI, mi primera API!"


@app.get("/url")
async def url_():
    return {"url_myweb":"https://trebool.wordpress.com/"}