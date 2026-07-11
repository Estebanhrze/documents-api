class DocumentTypeService:

    def get_all(self):
        return [
            {
                "id": 1,
                "name": "Normativa",
                "description": "Documentos normativos"
            },
            {
                "id": 2,
                "name": "Procedimiento",
                "description": "Procedimientos internos"
            },
            {
                "id": 3,
                "name": "Registro",
                "description": "Registros del sistema"
            },
            {
                "id": 4,
                "name": "Instructivo",
                "description": "Instructivos de trabajo"
            }
        ]

    def get_by_id(self, document_type_id: int):
        return {
            "id": document_type_id,
            "name": "Normativa",
            "description": "Documentos normativos"
        }

    def create(self, document_type):
        return {
            "message": "Tipo de documento creado correctamente",
            "data": document_type
        }

    def update(self, document_type_id: int, document_type):
        return {
            "message": "Tipo de documento actualizado correctamente",
            "id": document_type_id,
            "data": document_type
        }

    def delete(self, document_type_id: int):
        return {
            "message": "Tipo de documento eliminado correctamente",
            "id": document_type_id
        }