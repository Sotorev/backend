from sqlalchemy import Column, Integer, String, Text, Date
from .database import Base


class Noticia(Base):
    __tablename__ = "noticias"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    descripcion = Column(Text, nullable=False)
    autor = Column(String(100))
    fecha_publicacion = Column(Date)
    categoria = Column(String(50))
    contenido = Column(Text)
    fuente = Column(String(255))
    enlace = Column(String(255))
