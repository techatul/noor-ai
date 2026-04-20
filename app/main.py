from fastapi import FastAPI, Depends, HTTPException, Security
from app.api.v1.endpoints.chat import router as chat_router
from fastapi.security.api_key import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import getAppConfig

app = FastAPI()

app_config = getAppConfig()
api_key_name = app_config.APP_API_KEY_NAME

api_key_header = APIKeyHeader(name="X-API-Key")
async def validate_api_key(key: str = Security(api_key_header)):
    if key != api_key_name:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return key

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict later
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    chat_router,
    prefix="/api/v1",
    tags=["api"],
    dependencies=[Depends(validate_api_key)]
)
