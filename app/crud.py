from sqlalchemy.orm import Session
from . import models, schemas


class NoticiaFactory:
    @staticmethod
    def create_noticia(db: Session, noticia: schemas.NoticiaCreate):
        db_noticia = models.Noticia(**noticia.dict())
        db.add(db_noticia)
        db.commit()
        db.refresh(db_noticia)
        return db_noticia

    @staticmethod
    def get_noticia(db: Session, noticia_id: int):
        return db.query(models.Noticia).filter(models.Noticia.id == noticia_id).first()

    @staticmethod
    def get_noticias(db: Session, skip: int = 0, limit: int = 10):
        return db.query(models.Noticia).offset(skip).limit(limit).all()

    @staticmethod
    def update_noticia(db: Session, noticia_id: int, noticia: schemas.NoticiaUpdate):
        db_noticia = db.query(models.Noticia).filter(
            models.Noticia.id == noticia_id).first()
        if db_noticia:
            for key, value in noticia.dict(exclude_unset=True).items():
                setattr(db_noticia, key, value)
            db.commit()
            db.refresh(db_noticia)
        return db_noticia

    @staticmethod
    def delete_noticia(db: Session, noticia_id: int):
        db_noticia = db.query(models.Noticia).filter(
            models.Noticia.id == noticia_id).first()
        if db_noticia:
            db.delete(db_noticia)
            db.commit()
        return db_noticia
