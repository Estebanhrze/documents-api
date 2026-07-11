from app.core.database import supabase


class RoleService:

    def get_all(self):
        return (
            supabase
            .table("roles")
            .select("*")
            .execute()
            .data
        )

    def get_by_id(self, role_id: int):
        return (
            supabase
            .table("roles")
            .select("*")
            .eq("id", role_id)
            .single()
            .execute()
            .data
        )

    def create(self, role: dict):
        return (
            supabase
            .table("roles")
            .insert(role)
            .execute()
            .data
        )

    def update(self, role_id: int, role: dict):
        return (
            supabase
            .table("roles")
            .update(role)
            .eq("id", role_id)
            .execute()
            .data
        )

    def delete(self, role_id: int):
        return (
            supabase
            .table("roles")
            .delete()
            .eq("id", role_id)
            .execute()
            .data
        )