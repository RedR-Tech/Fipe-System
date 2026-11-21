"""
Aqui é onde monitora-se a saúde do sistema.
"""

from fastapi import APIRouter

router = APIRouter()

@router.get("/saude")
def verificar_saude_sistema():
    return {"status": "online", "application": "FIPE System API"}