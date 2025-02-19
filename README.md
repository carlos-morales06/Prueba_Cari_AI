Descripción de la Aplicación.

Esta aplicación es una API REST desarrollada con FastAPI que permite a los asesores de una empresa recibir
sugerencias automáticas basadas en preguntas frecuentes. La información se almacena en un archivo JSON,
evitando la necesidad de una base de datos.

Características Principales.
Búsqueda de preguntas frecuentes: Devuelve respuestas automáticas basadas en la consulta del usuario.
Historial de consultas: Permite visualizar las consultas anteriores y sus respuestas.
Agregar nuevas preguntas y respuestas: Los asesores pueden enriquecer la base de conocimiento.
Interfaz web: Una página simple permite interactuar con la API sin necesidad de herramientas externas.

Estructura del Proyecto.
1. Módulo principal (main.py)
Este archivo define los endpoints de la API utilizando FastAPI y maneja la lógica de consulta,
búsqueda y almacenamiento de datos.
2. Módulo de manejo de datos (data_handler.py)
Encargado de leer y escribir en el archivo JSON que almacena las preguntas y respuestas.
3. Archivo JSON (faqs.json)
Contiene las preguntas frecuentes y sus respuestas en formato estructurado.
4. Interfaz Web (templates/index.html)
Una página HTML simple que permite a los asesores interactuar con la API de manera visual.

Paso a Paso para Poner en Marcha la Aplicación

1. Clonar el Repositorio - 
git clone <https://github.com/carlos-morales06/Prueba_Cari_AI> - 
cd Prueba_Cari_AI
2. Crear un Entorno Virtual
Windows:
python -m venv venv
venv\Scripts\activate
3. Instalar Dependencias
pip install -r requirements.txt
4. Ejecutar el Servidor
uvicorn app.main:app --reload
5. Probar la API
Abrir el navegador y acceder a la documentación interactiva:
http://127.0.0.1:8000/docs
