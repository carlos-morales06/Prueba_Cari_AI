from fastapi import APIRouter, HTTPException
import json
import difflib
from .models import Query, Response, NewFAQ

router = APIRouter()
historial = []  # Almacena el historial de consultas

def cargar_preguntas():
    """ Carga las preguntas frecuentes desde el archivo JSON. """
    with open("app/data.json", "r", encoding="utf-8") as file:
        return json.load(file)

def guardar_preguntas(preguntas):
    """ Guarda las preguntas frecuentes en el archivo JSON. """
    with open("app/data.json", "w", encoding="utf-8") as file:
        json.dump(preguntas, file, ensure_ascii=False, indent=4)

@router.post("/suggest", response_model=Response)
def sugerir_respuesta(query: Query):
    """ Busca la respuesta más cercana basada en preguntas frecuentes. """
    preguntas = cargar_preguntas()
    lista_preguntas = [p["pregunta"] for p in preguntas]

    coincidencias = difflib.get_close_matches(query.query, lista_preguntas, n=1, cutoff=0.5)

    if coincidencias:
        mejor_coincidencia = coincidencias[0]
        respuesta = next(p["respuesta"] for p in preguntas if p["pregunta"] == mejor_coincidencia)
    else:
        respuesta = "Lo siento, no encontré una respuesta a tu consulta."

    historial.append({"query": query.query, "suggestion": respuesta})
    return {"query": query.query, "suggestion": respuesta}

@router.get("/history", response_model=list[Response])
def obtener_historial():
    """ Devuelve el historial de consultas. """
    return historial

@router.post("/add")
def agregar_pregunta(nueva_pregunta: NewFAQ):
    """ Agrega una nueva pregunta y respuesta al archivo JSON. """
    preguntas = cargar_preguntas()

    # Verificar si la pregunta ya existe
    for p in preguntas:
        if p["pregunta"].lower() == nueva_pregunta.pregunta.lower():
            raise HTTPException(status_code=400, detail="La pregunta ya existe en la base de datos.")

    preguntas.append({"pregunta": nueva_pregunta.pregunta, "respuesta": nueva_pregunta.respuesta})
    guardar_preguntas(preguntas)

    return {"mensaje": "Pregunta agregada con éxito!", "pregunta": nueva_pregunta.pregunta}
