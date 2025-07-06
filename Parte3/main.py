from fastapi import FastAPI, Query
from engine import procesar_pregunta

app = FastAPI()

@app.get("/chatbot")
def chatbot(q: str = Query(..., description="Pregunta en lenguaje natural")):
    respuesta = procesar_pregunta(q)
    return {"respuesta": respuesta}
