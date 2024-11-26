--ex3
SELECT *
FROM tracks
WHERE composer = 'AC/DC';

SELECT DISTINCT composer
FROM tracks;


SELECT * 
FROM artists
WHERE name = 'AC/DC'
-- ArtistId = 1

SELECT * 
FROM albums
WHERE ArtistId = 1
-- AlbumId IN (1,4)

SELECT * 
FROM tracks
WHERE AlbumId IN (1,4)


SELECT t.TrackId, t.Name AS TrackName, al.Title, t.Composer, ar.Name AS ArtistName
FROM tracks AS t
INNER JOIN albums AS al ON t.AlbumId = al.AlbumId
INNER JOIN artists AS ar ON al.ArtistId = ar.ArtistId
WHERE ar.Name = 'AC/DC'

--ex4
SELECT 
--firstname || ' ' || lastname AS NombreCompleto,
CONCAT(firstname, ' ' , lastname) AS NombreCompleto,
customerid AS ID,
country AS Pais
FROM customers
WHERE country <> 'USA';

--ex5
SELECT
--firstname || ' ' || lastname AS NombreCompleto,
CONCAT(firstname, ' ', lastname) AS NombreCompleto,
--city || ' ' || state || ' ' || Country AS Direccion,
CONCAT(city, ' ',state,' ', Country) AS Direccion,
email
FROM employees
WHERE title = 'Sales Support Agent';

--ex6
SELECT DISTINCT
billingcountry
FROM invoices;

SELECT billingcountry,
COUNT(invoiceid)
FROM invoices
GROUP BY billingcountry
ORDER BY 2 DESC

--ex7
SELECT 
State,
COUNT(customerid) AS NClientes
FROM customers
WHERE country = 'USA'
GROUP BY State
ORDER BY 2 DESC;

