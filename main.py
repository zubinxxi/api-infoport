from fastapi import FastAPI
from routes.home import router as router_home
from routes.movies import router as movies_router

app = FastAPI()
app.title = "Mi API con FastAPI"
app.version = "1.0.0"
app.description = "Esta es una API de ejemplo creada con FastAPI"
app.license_info = {
    "name": "MIT License",
    "url": "https://opensource.org/licenses/MIT",
}

app.openapi_tags = [
    {
        "name": "Home",
        "description": "Rutas de inicio y bienvenida",
    },
    {
        "name": "Movies",
        "description": "Rutas relacionadas con películas",
    },                                  
]
app.include_router(router_home)
app.include_router(movies_router)