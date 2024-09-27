CREATE TABLE noticias (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descripcion TEXT NOT NULL,
    autor VARCHAR(100),
    fecha_publicacion DATE,
    categoria VARCHAR(50),
    contenido TEXT,
    fuente VARCHAR(255),
    enlace VARCHAR(255)
);
