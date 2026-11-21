"""
Criação do arquivo principal, aqui é o motor, onde toda a aplicação parte começa. O servidor inicia e reconhece as rotas.
"""

from fastapi import FastAPI
from app.api.routes.health import router as saude_router

app = FastAPI(title= "FIPE System API", version= "1.0.0")

app.include_router(saude_router, tags=["Monitoramento"])