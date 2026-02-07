1. Consultas a una sola tabla
Escribe consultas SQL que realicen lo siguiente:
• Obtener todos los registros de la tabla clientes.
    SELECT *
    FROM clientes2

• Obtener el nombre y ciudad de todos los clientes que vivan en "Valparaíso".
    SELECT nombre, ciudad 
    FROM clientes2
    WHERE ciudad = "Valparaíso"

• Obtener el cliente con id = 3.
    SELECT * 
    FROM clientes2
    WHERE id = 3 

• Usar COUNT() para contar cuántos clientes hay en total.
   SELECT COUNT (*) AS total_clientes
   FROM clientes2

• Obtener todas las ciudades distintas en las que hay clientes (DISTINCT).
    SELECT DISTINCT ciudad
    FROM clientes2

• Agrupar clientes por ciudad y contar cuántos hay en cada una.
    SELECT ciudad, 
    COUNT (*)
    FROM clientes2
    GROUP BY ciudad

2. Consultas entre varias tablas
• Obtener todos los pedidos, incluyendo el nombre del cliente.
    SELECT (clientes2.nombre, pedidos.*)
    FROM pedidos
    JOIN clientes2 
    ON clientes2.id = pedidos.cliente_id


• Obtener los pedidos hechos por clientes de "Santiago".
    SELECT pedidos.*
    FROM pedidos
    JOIN clientes2 
    ON clientes2.id = pedidos.cliente_id
    WHERE clientes2.ciudad = 'Santiago'

• Obtener el total de pedidos por cliente (usando GROUP BY).
    SELECT clientes2.id, 
    COUNT (total) AS total_pedidos 
    FROM pedidos
    JOIN clientes2 
    ON clientes2.id = pedidos.cliente_id
    GROUP BY clientes2.id 

• Usar un LEFT JOIN para listar todos los clientes y sus pedidos, incluyendo aquellos que no han hecho
pedidos.
    SELECT clientes2.nombre, pedidos.*
    FROM clientes2 
    LEFT JOIN pedidos 
    ON clientes2.id = pedidos.cliente_id 

• Crear una consulta anidada que muestre los clientes cuyo total de pedidos supera los $100.000.
    SELECT clientes2.nombre
    FROM clientes2
    WHERE clientes2.id IN (
        SELECT cliente_id
        FROM pedidos 
        GROUP BY cliente_id 
        HAVING SUM(total) > 100000
    )
    