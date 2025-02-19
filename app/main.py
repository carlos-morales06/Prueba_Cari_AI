from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import router

app = FastAPI(title="FAQ API", description="Sistema de sugerencias basado en preguntas frecuentes")

# Incluir los endpoints desde routers.py
app.include_router(router, prefix="/faq", tags=["Preguntas Frecuentes"])

# Servir archivos estáticos (frontend)
app.mount("/", StaticFiles(directory="static", html=True), name="static")
