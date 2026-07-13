from app.core.database import supabase


class ReportService:

    def documents_by_status(self):
        response = (
            supabase
            .table("documents")
            .select("current_status")
            .execute()
        )

        counts = {}

        for document in response.data:
            status = document["current_status"]
            counts[status] = counts.get(status, 0) + 1

        return {
            "total": len(response.data),
            "by_status": counts
        }

    def pending_approvals(self):
        response = (
            supabase
            .table("approval_flows")
            .select("*")
            .eq("status", "pending")
            .execute()
        )

        return {
            "total_pending": len(response.data),
            "items": response.data
        }

    def audit_summary(self):
        response = (
            supabase
            .table("audit_logs")
            .select("*")
            .order("created_at", desc=True)
            .limit(50)
            .execute()
        )

        return {
            "total": len(response.data),
            "recent_logs": response.data
        }