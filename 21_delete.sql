--Eliminar registros: Escribe una consulta SQL para eliminar un usuario específico de la tabla Usuarios...


CREATE TABLE Usuario (
    id_usuario int NOT NULL PRIMARY KEY,
    nombre varchar (30)
);

INSERT INTO Usuario (id_usuario, nombre) VALUES (1, 'Hugo')
INSERT INTO Usuario (id_usuario, nombre) VALUES (2, 'Pedro')

SELECT * FROM Usuario

UPDATE Usuarios
SET nombre = 'Juan Perez'
WHERE id_usuario = 1


SELECT * FROM Usuario

DELETE FROM Usuario WHERE id_usuario = 1