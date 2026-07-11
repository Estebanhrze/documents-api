class DocumentVersionService:

    def get_all(self):
        return [
            {
                "id": 1,
                "document_id": 1,
                "version_number": "1.0",
                "file_path": "/uploads/documents/doc-001-v1.pdf",
                "file_format": "PDF",
                "file_size_kb": 256,
                "change_summary": "Versión inicial"
            },
            {
                "id": 2,
                "document_id": 1,
                "version_number": "1.1",
                "file_path": "/uploads/documents/doc-001-v1.1.pdf",
                "file_format": "PDF",
                "file_size_kb": 278,
                "change_summary": "Corrección de formato"
            }
        ]

    def get_by_id(self, version_id: int):
        return {
            "id": version_id,
            "document_id": 1,
            "version_number": "1.0",
            "file_path": "/uploads/documents/doc-001-v1.pdf",
            "file_format": "PDF",
            "file_size_kb": 256,
            "change_summary": "Versión inicial"
        }

    def create(self, version):
        return {
            "message": "Versión creada correctamente",
            "data": version
        }

    def update(self, version_id: int, version):
        return {
            "message": "Versión actualizada correctamente",
            "id": version_id,
            "data": version
        }

    def delete(self, version_id: int):
        return {
            "message": "Versión eliminada correctamente",
            "id": version_id
        }