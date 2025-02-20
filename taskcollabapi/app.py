from fastapi import FastAPI

from taskcollabapi import router

app = FastAPI()

# route creation
router.create_router(app)
