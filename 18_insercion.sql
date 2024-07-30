-- Inserción de datos: Escribe una consulta SQL para insertar un solo registro en la tabla Usuarios...

CREATE TABLE Usuario (
    id_usuario int NOT NULL PRIMARY KEY,
    nombre varchar (30)
);

INSERT INTO Usuario (id_usuario, nombre) VALUES (1, 'Hugo')