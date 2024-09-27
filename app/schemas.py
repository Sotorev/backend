from pydantic import BaseModel
from typing import Optional
from datetime import date


class NoticiaBase(BaseModel):
    titulo: str
    descripcion: str
    autor: Optional[str] = None
    fecha_publicacion: Optional[date] = None
    categoria: Optional[str] = None
    contenido: Optional[str] = None
    fuente: Optional[str] = None
    enlace: Optional[str] = None


class NoticiaCreate(NoticiaBase):
    pass


class NoticiaUpdate(NoticiaBase):
    pass


class Noticia(NoticiaBase):
    id: int

    class Config:
        orm_mode = True
