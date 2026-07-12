from app.core.database import supabase


class DocumentVersionService:

    def get_all(self):
        return (
            supabase
            .table("document_versions")
            .select("*")
            .execute()
            .data
        )

    def get_by_id(self, version_id: str):
        return (
            supabase
            .table("document_versions")
            .select("*")
            .eq("id", version_id)
            .single()
            .execute()
            .data
        )

    def create(self, version: dict):
        return (
            supabase
            .table("document_versions")
            .insert(version)
            .execute()
            .data
        )

    def update(self, version_id: str, version: dict):
        return (
            supabase
            .table("document_versions")
            .update(version)
            .eq("id", version_id)
            .execute()
            .data
        )

    def delete(self, version_id: str):
        return (
            supabase
            .table("document_versions")
            .delete()
            .eq("id", version_id)
            .execute()
            .data
        )