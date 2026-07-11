class AuditService:

    def get_all(self):
        return [
            {
                "id": 1,
                "user_id": 1,
                "document_id": 1,
                "action": "CREAR",
                "from_status": None,
                "to_status": "Borrador",
                "detail": "Documento creado",
                "ip_address": "127.0.0.1"
            },
            {
                "id": 2,
                "user_id": 2,
                "document_id": 1,
                "action": "APROBAR",
                "from_status": "En Revisión",
                "to_status": "Vigente",
                "detail": "Documento aprobado",
                "ip_address": "127.0.0.1"
            }
        ]

    def get_by_id(self, audit_id: int):
        return {
            "id": audit_id,
            "user_id": 1,
            "document_id": 1,
            "action": "CREAR",
            "from_status": None,
            "to_status": "Borrador",
            "detail": "Documento creado",
            "ip_address": "127.0.0.1"
        }

    def create(self, audit):
        return {
            "message": "Registro de auditoría creado correctamente",
            "data": audit
        }

    def delete(self, audit_id: int):
        return {
            "message": "Registro de auditoría eliminado correctamente",
            "id": audit_id
        }