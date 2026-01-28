from fastapi import APIRouter


# Ejecutamos APIRouter asignandolo a la variable router
router = APIRouter()


# Definimos las rutas con lo decoradores
@router.get("/movies", tags=["Movies"])
def get_movies():
   return {"mensaje":"Lista de películas"}