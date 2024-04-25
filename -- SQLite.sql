-- SQLite
SELECT name FROM sqlite_master WHERE type='table';

SELECT * FROM onlyflans_djweb_product;
SELECT * FROM onlyflans_djweb_contact;
SELECT * FROM auth_user;




-- UPDATE onlyflans_djweb_product
-- SET imagen = REPLACE(imagen, 'media/img/productos/', '')
INSERT INTO onlyflans_djweb_product (nombre, descripcion, imagen, slug, is_private, flan_uuid) VALUES ('Chocolate Blanco', 'Un flan tan suave y cremoso que te hará decir \"¡Ay caramba!\"', 'chocolate_blanco.jpg', 'chocolate-blanco', 0, 'nuevo-uuid-7');
INSERT INTO onlyflans_djweb_product (nombre, descripcion, imagen, slug, is_private, flan_uuid) VALUES ('De la Abuela', 'El flan tradicional de la abuela... pero sin las galletas de soda.', 'de_la_abuela.jpg', 'de-la-abuela', 0, 'nuevo-uuid-8');
INSERT INTO onlyflans_djweb_product (nombre, descripcion, imagen, slug, is_private, flan_uuid) VALUES ('Café', 'Porque nada dice \"Buenos días\" como un flan con sabor a café.', 'cafe.jpg', 'cafe', 0, 'nuevo-uuid-9');

UPDATE onlyflans_djweb_product SET flan_uuid = '4971ae2c-b0c2-43c1-967f-a857348d26a7' WHERE nombre = 'Basico';
UPDATE onlyflans_djweb_product SET flan_uuid = 'de66eb7f-f215-40fb-bbb0-0b30b6d275ce' WHERE nombre = 'Chocolate';
UPDATE onlyflans_djweb_product SET flan_uuid = 'd59479aa-b3e4-458b-a63d-9d8d3f2f0123' WHERE nombre = 'Premium';
UPDATE onlyflans_djweb_product SET flan_uuid = 'ead81813-c271-47be-9958-d89085f32b3f' WHERE nombre = 'Familiar';
UPDATE onlyflans_djweb_product SET flan_uuid = '129105a0-0f43-47b2-a957-b673afc8c3ac' WHERE nombre = 'Helado';

UPDATE onlyflans_djweb_product SET flan_uuid = '4d40a83f-6522-4458-95b6-80590f7501f7' WHERE nombre = 'Chocolate Blanco';
UPDATE onlyflans_djweb_product SET flan_uuid = '11656c31-65dc-482d-917b-2e81e7fcf4fa' WHERE nombre = 'De la Abuela';
UPDATE onlyflans_djweb_product SET flan_uuid = 'cbd6d828-79da-4637-a881-5106d7313b84' WHERE nombre = 'Café';

UPDATE onlyflans_djweb_product SET descripcion = 'Porque nada dice "Buenos días" como un flan con sabor a café.' WHERE nombre = 'Café';

UPDATE onlyflans_djweb_product SET is_private = 1 WHERE slug IN ('cafe', 'chocolate-blanco', 'premium');

