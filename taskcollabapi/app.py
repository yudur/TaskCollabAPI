from fastapi import FastAPI

from taskcollabapi import router
from taskcollabapi.errors.handler import setup_error_handlers

app = FastAPI()

# Configure the global error handler
setup_error_handlers(app)

# route creation
router.create_router(app)
