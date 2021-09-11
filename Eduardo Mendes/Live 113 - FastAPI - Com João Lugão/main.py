from fastapi import FastAPI
from typing import List, Dict, Any, Optional
from pydantic import BaseModel

app = FastAPI()

a_fazer: List[Dict[str, Any]] = [
    {
        "id": 1,
        "titulo": "Fazer live",
        "descricao": "Fazer live no canal do Edu",
        "Status": "A fazer"
    },
    {
        "id": 2,
        "titulo": "Ligar stream",
        "Status": "A fazer"
    },
    {
        "id": 3,
        "titulo": "Pentear o cabelo (ou raspar)",
        "Status": "A fazer"
    }
]

class ModelDoItem(BaseModel):
    id: int
    titulo: str
    status: Optional[str]

@app.get('/')
def hello_world():
    """
    View raiz
    :return: {"ola": "mundo"}
    """
    return {"ola": "mundo"}

@app.get('/a-fazer', response_model=List[ModelDoItem])
def listar_a_fazer():
    """
   View que retorna lista de itens a fazer
    """
    return a_fazer