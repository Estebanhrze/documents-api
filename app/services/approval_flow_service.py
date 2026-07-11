class ApprovalFlowService:

    def get_all(self):
        return [
            {
                "id": 1,
                "document_id": 1,
                "version_id": 1,
                "step_order": 1,
                "assigned_to": 2,
                "action": "Revisión",
                "status": "Pendiente",
                "comments": None
            },
            {
                "id": 2,
                "document_id": 1,
                "version_id": 1,
                "step_order": 2,
                "assigned_to": 3,
                "action": "Aprobación",
                "status": "Pendiente",
                "comments": None
            }
        ]

    def get_by_id(self, approval_id: int):
        return {
            "id": approval_id,
            "document_id": 1,
            "version_id": 1,
            "step_order": 1,
            "assigned_to": 2,
            "action": "Revisión",
            "status": "Pendiente",
            "comments": None
        }

    def create(self, approval):
        return {
            "message": "Flujo de aprobación creado correctamente",
            "data": approval
        }

    def update(self, approval_id: int, approval):
        return {
            "message": "Flujo de aprobación actualizado correctamente",
            "id": approval_id,
            "data": approval
        }

    def delete(self, approval_id: int):
        return {
            "message": "Flujo de aprobación eliminado correctamente",
            "id": approval_id
        }