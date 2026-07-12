from app.core.database import supabase


class ApprovalFlowService:

    def get_all(self):
        return (
            supabase
            .table("approval_flows")
            .select("*")
            .execute()
            .data
        )

    def get_by_id(self, approval_id: str):
        return (
            supabase
            .table("approval_flows")
            .select("*")
            .eq("id", approval_id)
            .single()
            .execute()
            .data
        )

    def create(self, approval: dict):
        return (
            supabase
            .table("approval_flows")
            .insert(approval)
            .execute()
            .data
        )

    def update(self, approval_id: str, approval: dict):
        return (
            supabase
            .table("approval_flows")
            .update(approval)
            .eq("id", approval_id)
            .execute()
            .data
        )

    def delete(self, approval_id: str):
        return (
            supabase
            .table("approval_flows")
            .delete()
            .eq("id", approval_id)
            .execute()
            .data
        )