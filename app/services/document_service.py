from app.core.database import supabase


class DocumentService:

    def get_all(self):
        return (
            supabase
            .table("documents")
            .select("*")
            .execute()
            .data
        )

    def get_by_id(self, document_id: str):
        return (
            supabase
            .table("documents")
            .select("*")
            .eq("id", document_id)
            .single()
            .execute()
            .data
        )

    def create(self, document: dict):
        return (
            supabase
            .table("documents")
            .insert(document)
            .execute()
            .data
        )

    def update(self, document_id: str, document: dict):
        return (
            supabase
            .table("documents")
            .update(document)
            .eq("id", document_id)
            .execute()
            .data
        )

    def delete(self, document_id: str):
        return (
            supabase
            .table("documents")
            .delete()
            .eq("id", document_id)
            .execute()
            .data
        )