from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/noticias/", response_model=schemas.Noticia)
def create_noticia(noticia: schemas.NoticiaCreate, db: Session = Depends(get_db)):
    return crud.NoticiaFactory.create_noticia(db=db, noticia=noticia)


@app.get("/noticias/{noticia_id}", response_model=schemas.Noticia)
def read_noticia(noticia_id: int, db: Session = Depends(get_db)):
    db_noticia = crud.NoticiaFactory.get_noticia(db=db, noticia_id=noticia_id)
    if db_noticia is None:
        raise HTTPException(status_code=404, detail="Noticia no encontrada")
    return db_noticia


@app.get("/noticias/", response_model=list[schemas.Noticia])
def read_noticias(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.NoticiaFactory.get_noticias(db=db, skip=skip, limit=limit)


@app.put("/noticias/{noticia_id}", response_model=schemas.Noticia)
def update_noticia(noticia_id: int, noticia: schemas.NoticiaUpdate, db: Session = Depends(get_db)):
    return crud.NoticiaFactory.update_noticia(db=db, noticia_id=noticia_id, noticia=noticia)


@app.delete("/noticias/{noticia_id}", response_model=schemas.Noticia)
def delete_noticia(noticia_id: int, db: Session = Depends(get_db)):
    return crud.NoticiaFactory.delete_noticia(db=db, noticia_id=noticia_id)
