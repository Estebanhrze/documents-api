from app.core.database import supabase


class AttachmentService:

    def get_all(self):
        return (
            supabase
            .table("attachments")
            .select("*")
            .execute()
            .data
        )

    def get_by_id(self, attachment_id: str):
        return (
            supabase
            .table("attachments")
            .select("*")
            .eq("id", attachment_id)
            .single()
            .execute()
            .data
        )

    def create(self, attachment: dict):
        return (
            supabase
            .table("attachments")
            .insert(attachment)
            .execute()
            .data
        )

    def update(self, attachment_id: str, attachment: dict):
        return (
            supabase
            .table("attachments")
            .update(attachment)
            .eq("id", attachment_id)
            .execute()
            .data
        )

    def delete(self, attachment_id: str):
        return (
            supabase
            .table("attachments")
            .delete()
            .eq("id", attachment_id)
            .execute()
            .data
        )