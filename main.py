from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles # Importar StaticFiles para servir archivos estáticos
from fastapi.openapi.docs import get_swagger_ui_html # Importar función para personalizar Swagger UI

from routes.containers import router as containers_router # Importar el router de contenedores

# 1. Desactivar docs predeterminados al crear la app
app = FastAPI(docs_url=None, redoc_url=None)

# Montar carpeta estática
app.mount("/static", StaticFiles(directory="static"), name="static") # Montar la carpeta "static" para servir archivos estáticos
app.title = "INFOPORT - API" # Personalizar el título de la documentación
app.version = "1.0.0" # Personalizar la versión de la documentación
app.description = "API para gestionar movimientos de contenedores"  # Personalizar la descripción de la documentación

@app.get("/docs", include_in_schema=False) # Personalizar la ruta de Swagger UI
async def custom_swagger_ui_html(): # Función para servir Swagger UI personalizado
    return get_swagger_ui_html(
        openapi_url=app.openapi_url, # URL del esquema OpenAPI
        title=app.title, # Título de la documentación
        swagger_favicon_url="/static/favicon.png" # Ruta a tu favicon personalizado
    )


app.openapi_tags = [
    {
        "name": "Movimiento de Contenedores",
        "description": "Rutas para gestionar movimientos de contenedores",
    },                                  
]

app.swagger_ui_parameters = {
    "syntaxHighlight": {"theme": "obsidian",}
}


app.include_router(containers_router)