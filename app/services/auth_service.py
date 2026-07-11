class AuthService:

    def login(self, credentials):
        return {
            "message": "Inicio de sesión exitoso",
            "access_token": "fake-jwt-token",
            "token_type": "bearer",
            "user": {
                "id": 1,
                "name": "Administrador",
                "email": "admin@documentex.com",
                "role": "Administrador"
            }
        }

    def logout(self):
        return {
            "message": "Sesión cerrada correctamente"
        }

    def me(self):
        return {
            "id": 1,
            "name": "Administrador",
            "email": "admin@documentex.com",
            "role": "Administrador"
        }