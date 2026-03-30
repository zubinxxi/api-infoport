from fastapi import APIRouter


# Ejecutamos APIRouter asignandolo a la variable router
router = APIRouter()


# Definimos las rutas con lo decoradores
@router.get("/movement-container", tags=["Movimiento de Contenedores"])
def get_movement_container():
   return {"page_title":"Movimiento de contenedores"}