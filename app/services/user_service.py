from app.core.database import supabase


class UserService:

    def get_all(self):
        response = (
            supabase
            .table("users")
            .select("*")
            .execute()
        )
        return response.data

    def get_by_id(self, user_id: str):
        response = (
            supabase
            .table("users")
            .select("*")
            .eq("id", user_id)
            .single()
            .execute()
        )
        return response.data

    def create(self, user: dict):
        response = (
            supabase
            .table("users")
            .insert(user)
            .execute()
        )
        return response.data

    def update(self, user_id: str, user: dict):
        response = (
            supabase
            .table("users")
            .update(user)
            .eq("id", user_id)
            .execute()
        )
        return response.data

    def delete(self, user_id: str):
        response = (
            supabase
            .table("users")
            .delete()
            .eq("id", user_id)
            .execute()
        )
        return response.data