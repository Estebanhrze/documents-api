import uuid

from fastapi import HTTPException, status

from app.core.database import supabase
from app.core.security import active_sessions


class AuthService:

    def login(self, credentials: dict):
        response = (
            supabase
            .table("users")
            .select("id, name, email, role_id, password")
            .eq("email", credentials["email"])
            .execute()
        )

        if not response.data:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales inválidas"
            )

        user = response.data[0]

        if user["password"] != credentials["password"]:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales inválidas"
            )

        token = str(uuid.uuid4())
        active_sessions[token] = {
            "id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "role_id": user["role_id"]
        }

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    def logout(self, token: str):
        active_sessions.pop(token, None)
        return {"message": "Sesión cerrada correctamente"}

    def me(self, current_user: dict):
        return current_user