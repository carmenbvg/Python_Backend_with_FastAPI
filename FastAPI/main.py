from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "¡Hola FastAPI, mi primera API!"


@app.get("/url")
async def url_():
    return {"url_myweb":"https://trebool.wordpress.com/"}

# Inicia el server: uvicorn main:app --reload
# Detiene el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc