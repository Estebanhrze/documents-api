from supabase import Client, create_client

from app.core.config import settings

# Cliente general con permisos públicos/RLS de Supabase.
supabase: Client = create_client(
    settings.SUPABASE_URL,
    settings.SUPABASE_PUBLISHABLE_KEY,
)

# Solo el servidor utiliza esta clave para escribir en el bucket privado.
supabase_storage: Client = create_client(
    settings.SUPABASE_URL,
    settings.SUPABASE_SERVICE_ROLE_KEY,
)