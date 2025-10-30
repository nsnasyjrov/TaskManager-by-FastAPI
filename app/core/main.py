import uvicorn
from fastapi import FastAPI
from app.api.routes import project_router
from fastapi import FastAPI, Request
from app.core.database import get_db, AsyncSession, Container


def create_application():
    app = FastAPI(title="Test app")
    @app.middleware("http")
    async def attach_container(request: Request, call_next):
        async for db in get_db():
            request.state.container = Container(db)
            response = await call_next(request)
            return response


    app.include_router(project_router)
    return app

def start():
    uvicorn.run("run:app", host="127.0.0.1", port=8000, reload=True)