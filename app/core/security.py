from hmac import compare_digest
from typing import Annotated

from fastapi import Header, HTTPException, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.config import settings

security = HTTPBearer()
optional_security = HTTPBearer(auto_error=False)

active_sessions: dict[str, dict] = {}


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Security(security),
) -> dict:
    token = credentials.credentials
    user = active_sessions.get(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o sesión expirada",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


def get_upload_user(
    credentials: HTTPAuthorizationCredentials | None = Security(optional_security),
    internal_key: Annotated[
        str | None,
        Header(alias="X-Documentex-Internal-Key"),
    ] = None,
    internal_user_id: Annotated[
        str | None,
        Header(alias="X-Documentex-User-Id"),
    ] = None,
) -> dict:
    """Accepts an API session or the trusted Django server-to-server request."""
    if internal_key is not None:
        if not compare_digest(internal_key, settings.DJANGO_API_SHARED_SECRET):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Credencial interna no válida.",
            )
        if not internal_user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Falta identificar al usuario que carga el archivo.",
            )
        return {"id": internal_user_id}

    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Se requiere autenticación.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = credentials.credentials
    user = active_sessions.get(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o sesión expirada",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user