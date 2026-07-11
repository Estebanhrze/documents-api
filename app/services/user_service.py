class UserService:

    def get_all(self):
        return [
            {
                "id": 1,
                "name": "Administrador",
                "email": "admin@documentex.com",
                "role_id": 1,
                "mfa_enabled": False,
                "is_active": True
            },
            {
                "id": 2,
                "name": "Juan Ect",
                "email": "juan@documentex.com",
                "role_id": 2,
                "mfa_enabled": True,
                "is_active": True
            }
        ]

    def get_by_id(self, user_id: int):
        return {
            "id": user_id,
            "name": "Administrador",
            "email": "admin@documentex.com",
            "role_id": 1,
            "mfa_enabled": False,
            "is_active": True
        }

    def create(self, user):
        return {
            "message": "Usuario creado correctamente",
            "data": user
        }

    def update(self, user_id: int, user):
        return {
            "message": "Usuario actualizado correctamente",
            "id": user_id,
            "data": user
        }

    def delete(self, user_id: int):
        return {
            "message": "Usuario eliminado correctamente",
            "id": user_id
        }