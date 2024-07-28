-- Consulta básica: Escribe una consulta SQL para seleccionar todos los registros de la tabla Usuarios.
 
CREATE TABLE Usuario (
    id_usuario int NOT NULL PRIMARY KEY,
    nombre varchar (30)
);

INSERT INTO Usuario (id_usuario, nombre) VALUES (1, 'Hugo')

SELECT * FROM Usuario