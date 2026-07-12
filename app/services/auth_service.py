from app.core.database import supabase


class AuthService:

    def login(self, credentials: dict):
        response = (
            supabase
            .table("users")
            .select("id, name, email, role_id")
            .eq("email", credentials["email"])
            .execute()
        )

        if not response.data:
            return {
                "message": "Usuario no encontrado"
            }

        user = response.data[0]

        return {
            "message": "Usuario encontrado",
            "user": user
        }

    def logout(self):
        return {
            "message": "Sesión cerrada correctamente"
        }

    def me(self):
        return {
            "message": (
                "Disponible cuando se implemente JWT "
                "en la Fase 4."
            )
        }