from app.core.database import supabase


class AuditService:

    def get_all(self):
        return (
            supabase
            .table("audit_logs")
            .select("*")
            .execute()
            .data
        )

    def get_by_id(self, audit_id: str):
        return (
            supabase
            .table("audit_logs")
            .select("*")
            .eq("id", audit_id)
            .single()
            .execute()
            .data
        )

    def create(self, audit: dict):
        return (
            supabase
            .table("audit_logs")
            .insert(audit)
            .execute()
            .data
        )

    def delete(self, audit_id: str):
        return (
            supabase
            .table("audit_logs")
            .delete()
            .eq("id", audit_id)
            .execute()
            .data
        )