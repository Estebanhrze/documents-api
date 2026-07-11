class RoleService:

    def get_all(self):
        return [
            {
                "id": 1,
                "name": "Administrador",
                "description": "Acceso total",
                "permissions": "crear,editar,revisar,aprobar,archivar",
                "is_custom": False
            },
            {
                "id": 2,
                "name": "Usuario",
                "description": "Acceso básico",
                "permissions": "crear",
                "is_custom": False
            }
        ]

    def get_by_id(self, role_id: int):
        return {
            "id": role_id,
            "name": "Administrador",
            "description": "Acceso total",
            "permissions": "crear,editar,revisar,aprobar,archivar",
            "is_custom": False
        }

    def create(self, role):
        return {
            "message": "Rol creado correctamente",
            "data": role
        }

    def update(self, role_id: int, role):
        return {
            "message": "Rol actualizado correctamente",
            "id": role_id,
            "data": role
        }

    def delete(self, role_id: int):
        return {
            "message": "Rol eliminado correctamente",
            "id": role_id
        }