class DocumentService:

    def get_all(self):
        return [
            {
                "id": 1,
                "doc_number": "DOC-001",
                "title": "Procedimiento de Calidad",
                "classification": "Interno",
                "document_type_id": 2,
                "current_status": "Vigente",
                "created_by": 1
            },
            {
                "id": 2,
                "doc_number": "DOC-002",
                "title": "Manual ISO 17025",
                "classification": "Confidencial",
                "document_type_id": 1,
                "current_status": "En Revisión",
                "created_by": 2
            }
        ]

    def get_by_id(self, document_id: int):
        return {
            "id": document_id,
            "doc_number": "DOC-001",
            "title": "Procedimiento de Calidad",
            "classification": "Interno",
            "document_type_id": 2,
            "current_status": "Vigente",
            "created_by": 1
        }

    def create(self, document):
        return {
            "message": "Documento creado correctamente",
            "data": document
        }

    def update(self, document_id: int, document):
        return {
            "message": "Documento actualizado correctamente",
            "id": document_id,
            "data": document
        }

    def delete(self, document_id: int):
        return {
            "message": "Documento eliminado correctamente",
            "id": document_id
        }