from pydantic import BaseModel, Field


class UploadResponse(BaseModel):
    file_path: str = Field(description="Ruta estable del archivo dentro del bucket de Supabase.")
    file_name: str
    file_type: str
    file_size_kb: int


class SignedUrlResponse(BaseModel):
    signed_url: str = Field(description="Enlace temporal para descargar un archivo privado.")