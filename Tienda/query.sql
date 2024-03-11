
CREATE database TiendaAxM
Use TiendaAxM


CREATE TABLE Productos (
    ID INT PRIMARY KEY IDENTITY(1,1),
    Nombre NVARCHAR(100) NOT NULL,
    Precio DECIMAL(10,2) NOT NULL,
    Descripcion NVARCHAR(255),
    URLImagen NVARCHAR(255),
    Marca NVARCHAR(100),
    Categoria NVARCHAR(100)
);

select * from Productos

-- Insertar productos ficticios en la tabla Productos
INSERT INTO Productos (Nombre, Precio, Descripcion, URLImagen, Marca, Categoria)
VALUES ('Samsung Galaxy M12', 599.99, 'Smartphone de última generación con cámara de alta resolución', 'https://storage.comprasmartphone.com/smartphones/samsung-galaxy-m12.png', 'XYZ Electronics', 'Electrónicos'),
       ('Puma X One Piece', 89.99, 'Colaboracion con One Piece', 'https://statics.whentocop.fr/one_piece_puma_suede_luffy_gear_5_396524_01_54c84798a9.webp', 'ABC Sports', 'Ropa'),
	   ('One Piece Tomo 1', 19.99, 'Libro de ciencia ficción que narra emocionantes aventuras en el Mar', 'https://cdnx.jumpseller.com/japan-market-chile/image/33097562/resize/540/540?1678731587', 'Cosmos Publishing', 'Otros'),
       ('Play 5', 49.99, 'Consola', 'https://gmedia.playstation.com/is/image/SIEPDC/ps5-product-thumbnail-01-en-14sep21?$facebook$', 'Classic Films', 'Otros');


UPDATE Productos
SET Precio = 40
WHERE Nombre = 'Samsung Galaxy M12';


