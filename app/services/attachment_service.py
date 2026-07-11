class AttachmentService:

    def get_all(self):
        return [
            {
                "id": 1,
                "document_id": 1,
                "version_id": 1,
                "file_name": "procedimiento.pdf",
                "file_path": "/uploads/documents/procedimiento.pdf",
                "file_type": "evidencia"
            },
            {
                "id": 2,
                "document_id": 2,
                "version_id": 1,
                "file_name": "manual_iso.pdf",
                "file_path": "/uploads/documents/manual_iso.pdf",
                "file_type": "anexo"
            }
        ]

    def get_by_id(self, attachment_id: int):
        return {
            "id": attachment_id,
            "document_id": 1,
            "version_id": 1,
            "file_name": "procedimiento.pdf",
            "file_path": "/uploads/documents/procedimiento.pdf",
            "file_type": "evidencia"
        }

    def create(self, attachment):
        return {
            "message": "Adjunto creado correctamente",
            "data": attachment
        }

    def update(self, attachment_id: int, attachment):
        return {
            "message": "Adjunto actualizado correctamente",
            "id": attachment_id,
            "data": attachment
        }

    def delete(self, attachment_id: int):
        return {
            "message": "Adjunto eliminado correctamente",
            "id": attachment_id
        }