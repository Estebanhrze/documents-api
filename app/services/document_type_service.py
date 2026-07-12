from app.core.database import supabase


class DocumentTypeService:

    def get_all(self):
        response = (
            supabase
            .table("document_types")
            .select("*")
            .execute()
        )
        return response.data

    def get_by_id(self, document_type_id: int):
        response = (
            supabase
            .table("document_types")
            .select("*")
            .eq("id", document_type_id)
            .single()
            .execute()
        )
        return response.data

    def create(self, document_type: dict):
        response = (
            supabase
            .table("document_types")
            .insert(document_type)
            .execute()
        )
        return response.data

    def update(self, document_type_id: int, document_type: dict):
        response = (
            supabase
            .table("document_types")
            .update(document_type)
            .eq("id", document_type_id)
            .execute()
        )
        return response.data

    def delete(self, document_type_id: int):
        response = (
            supabase
            .table("document_types")
            .delete()
            .eq("id", document_type_id)
            .execute()
        )
        return response.data