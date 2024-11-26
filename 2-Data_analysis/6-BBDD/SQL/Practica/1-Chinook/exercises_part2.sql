--ex1
SELECT
t1.FirstName || ' ' || t1.LastName AS NombreCliente,
t2.InvoiceId,
t2.InvoiceDate,
t2.BillingCountry
FROM customers t1
INNER JOIN invoices t2 ON t1.CustomerId = t2.CustomerId
WHERE t1.Country = 'Brazil'

--ex2
SELECT
t1.FirstName || ' ' || t1.LastName AS NombreEmpleado,
t3.*
FROM employees t1
INNER JOIN customers t2 ON t1.EmployeeId = t2.SupportRepId
INNER JOIN invoices t3 ON t2.CustomerId = t3.CustomerId
WHERE t1.title = 'Sales Support Agent';

--ex3
SELECT
t1.FirstName || ' ' || t1.LastName AS NombreEmpleado,
t2.FirstName || ' ' || t2.LastName AS NombreCliente,
SUM(t3.Total) AS VVentas,
COUNT(t3.Total) AS NCompras
FROM employees t1
INNER JOIN customers t2 ON t1.EmployeeId = t2.SupportRepId
INNER JOIN invoices t3 ON t2.CustomerId = t3.CustomerId
WHERE t1.title = 'Sales Support Agent'
GROUP BY 1,2
ORDER BY 3 DESC;

--ex4
SELECT t1.*,
t2.Name AS NombreCancion
FROM invoice_items t1
INNER JOIN tracks t2 ON t1.TrackId = t2.TrackId

--ex5
SELECT
t1.TrackId,
t1.Name AS NombreCancion,
t2.Name AS NombreFormato,
t3.Name AS NombreGenero,
t4.Title AS TituloAlbum
FROM tracks t1
INNER JOIN media_types t2 ON t1.MediaTypeId = t2.MediaTypeId
INNER JOIN genres t3 ON t1.GenreId = t3.GenreId
INNER JOIN albums t4 ON t1.AlbumId = t4.AlbumId

--ex6
SELECT 
t2.PlaylistId,
t2.Name,
COUNT(t1.trackid) AS NCanciones
FROM playlist_track t1
INNER JOIN playlists t2 ON t1.PlaylistId = t2.PlaylistId
GROUP BY 1,2
ORDER BY 3 DESC

--ex7
SELECT
t1.EmployeeId,
t1.FirstName || ' ' || t1.LastName AS NombreEmpleado,
COUNT(DISTINCT t2.CustomerId) AS NClientes,
COUNT(t3.InvoiceId) AS NCompras,
SUM(t3.Total)AS VVentas
FROM employees t1
INNER JOIN customers t2 ON t1.EmployeeId = t2.SupportRepId
INNER JOIN invoices t3 ON t2.CustomerId = t3.CustomerId
WHERE t1.title = 'Sales Support Agent'
GROUP BY 1,2
ORDER BY VVentas DESC
;


--ex8
SELECT
t1.EmployeeId,
t1.FirstName || ' ' || t1.LastName AS NombreEmpleado,
COUNT(DISTINCT t2.CustomerId) AS NClientes,
COUNT(t3.InvoiceId) AS NCompras,
SUM(t3.Total)AS VVentas
FROM employees t1
INNER JOIN customers t2 ON t1.EmployeeId = t2.SupportRepId
INNER JOIN invoices t3 ON t2.CustomerId = t3.CustomerId
WHERE t1.title = 'Sales Support Agent' AND strftime('%Y', t3.InvoiceDate) = '2009'
GROUP BY 1,2
ORDER BY VVentas DESC
;

--ex9
SELECT 
t1.ArtistId,
t1.Name AS NombreArtista,
SUM(t5.Total) AS VVentas,
COUNT(DISTINCT t5.invoiceid) AS NFacturas
FROM artists t1
INNER JOIN albums t2 ON t1.ArtistId = t2.ArtistId
INNER JOIN tracks t3 ON t2.AlbumId = t3.AlbumId
INNER JOIN invoice_items t4 ON t3.TrackId = t4.TrackId
INNER JOIN invoices t5 ON t4.InvoiceId = t5.InvoiceId
GROUP BY 1,2
ORDER BY 3 DESC
LIMIT 3

