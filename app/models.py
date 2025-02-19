from pydantic import BaseModel

class Query(BaseModel):
    query: str
   
class Response(BaseModel):
    query: str
    suggestion: str

class NewFAQ(BaseModel):
    pregunta: str
    respuesta: str
