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
        for doc in response.data:
            doc_status = doc["current_status"]
            counts[doc_status] = counts.get(doc_status, 0) + 1

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
            .order("logged_at", desc=True)
            .limit(50)
            .execute()
        )
        return {
            "total": len(response.data),
            "recent_logs": response.data
        }
