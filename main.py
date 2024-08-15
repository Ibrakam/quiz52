from fastapi import FastAPI
from api.user_api import user_router
from db import Base, engine
Base.metadata.create_all(engine)


app = FastAPI(docs_url="/")
app.include_router(user_router)



