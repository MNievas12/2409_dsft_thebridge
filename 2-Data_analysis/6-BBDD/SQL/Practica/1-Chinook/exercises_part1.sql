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

--ex8
SELECT
t1.InvoiceId,
t1.InvoiceDate,
SUM(t2.Quantity) AS N_articulos
FROM invoices t1
INNER JOIN invoice_items t2 ON t1.InvoiceId = t2.InvoiceId
WHERE t1.invoiceid = 37
GROUP BY 1,2
--ORDER BY 2 DESC;

SELECT
InvoiceId,
SUM(Quantity) AS N_articulos
FROM invoice_items
WHERE invoiceid IN (37)
GROUP BY 1;

--ex9
SELECT
ar.ArtistId,
ar.Name,
COUNT(t.TrackId)
FROM tracks AS t
INNER JOIN albums AS al ON t.AlbumId = al.AlbumId
INNER JOIN artists AS ar ON al.ArtistId = ar.ArtistId
WHERE ar.Name = 'AC/DC'
GROUP BY 1,2

--ex10
SELECT
InvoiceId,
SUM(Quantity) AS N_articulos
FROM invoice_items
--WHERE invoiceid IN (37)
GROUP BY 1
ORDER BY 2 DESC;

--ex11
SELECT 
billingcountry,
COUNT(invoiceid) AS NFacturas
FROM invoices
GROUP BY 1
ORDER BY 2 DESC

--ex12
SELECT
strftime('%Y', invoicedate) AS Año,
--SUBSTRING(invoicedate, 1, 4) AS Año,
COUNT(invoiceid)
FROM invoices
WHERE Año IN ('2009','2011')
GROUP BY 1

--ex13
SELECT
CAST(strftime('%Y', invoicedate) AS int) AS Año,
--SUBSTRING(invoicedate, 1, 4) AS Año,
COUNT(invoiceid)
FROM invoices
WHERE Año BETWEEN 2009 AND 2011
GROUP BY 1

--ex14
SELECT
SUM(NClientes)
FROM
	(
	SELECT 
	country,
	COUNT(customerid) AS NClientes
	FROM customers
	WHERE Country IN ('Spain', 'Brazil')
	GROUP BY 1
    )
    
--ex15
SELECT *
FROM tracks
WHERE LOWER(Name) LIKE 'you %'