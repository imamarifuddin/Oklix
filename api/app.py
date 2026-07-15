from fastapi import FastAPI

from api.exceptions import unhandled_exception_handler
from api.middleware import log_requests
from api.routes import router
from api.version import DESCRIPTION, NAME, VERSION

app = FastAPI(

    title=NAME,

    description=DESCRIPTION,

    version=VERSION,

    contact={
        "name": "Oklix",
    },

    license_info={
        "name": "MIT",
    },

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