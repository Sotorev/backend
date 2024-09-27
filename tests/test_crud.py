from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app, get_db
from app.database import Base
import pytest

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={
                       "check_same_thread": False})
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


@pytest.fixture
def test_noticia():
    return {
        "titulo": "Test Titulo",
        "descripcion": "Test Descripcion",
        "autor": "Test Autor",
        "categoria": "Test Categoria",
        "contenido": "Test Contenido",
        "fuente": "Test Fuente",
        "enlace": "http://test.com"
    }


def test_create_noticia(test_noticia):
    response = client.post("/noticias/", json=test_noticia)
    assert response.status_code == 200
    assert response.json()["titulo"] == test_noticia["titulo"]


def test_get_noticia():
    response = client.get("/noticias/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_update_noticia(test_noticia):
    response = client.put("/noticias/1", json={
        "titulo": "Updated Titulo",
        "descripcion": "string",
        "autor": "string",
        "fecha_publicacion": "2024-09-27",
        "categoria": "string",
        "contenido": "string",
        "fuente": "string",
        "enlace": "string"
    })
    assert response.status_code == 200
    assert response.json()["titulo"] == "Updated Titulo"


def test_delete_noticia():
    response = client.delete("/noticias/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
