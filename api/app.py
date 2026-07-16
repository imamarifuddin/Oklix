"""
Oklix REST API Application.
"""

from fastapi import FastAPI

from api.exceptions import unhandled_exception_handler
from api.middleware import log_requests
from api.routes import router
from api.version import (
    CONTACT,
    DESCRIPTION,
    LICENSE,
    NAME,
    VERSION,
)

tags_metadata = [
    {
        "name": "System",
        "description": "System information, health checks, and version endpoints.",
    },
    {
        "name": "Optimization",
        "description": "Decision Intelligence optimization endpoints.",
    },
]

app = FastAPI(
    title=NAME,
    version=VERSION,
    description=DESCRIPTION,
    contact=CONTACT,
    license_info=LICENSE,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    openapi_tags=tags_metadata,
    servers=[
        {
            "url": "http://localhost:8000",
            "description": "Local Development",
        }
    ],
)

# Register middleware
app.middleware("http")(log_requests)

# Register exception handler
app.add_exception_handler(
    Exception,
    unhandled_exception_handler,
)

# Register routes
app.include_router(router)