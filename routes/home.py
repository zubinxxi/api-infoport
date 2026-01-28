from fastapi import APIRouter


# Ejecutamos APIRouter asignandolo a la variable router
router = APIRouter()


# Definimos las rutas con lo decoradores
@router.get("/", tags=["Home"], summary="Ruta de inicio", description="Esta ruta devuelve un mensaje de bienvenida")
def home():
   return {"mensaje":"Hola, Saludos!!!"}
