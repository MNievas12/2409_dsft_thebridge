SELECT *
FROM crime_scene_report
WHERE date = 20180115 AND type = 'murder' AND city = 'SQL City';
--Security footage shows that there were 2 witnesses. 
--The first witness lives at the last house on "Northwestern Dr". 
--The second witness, named Annabel, lives somewhere on "Franklin Ave".

SELECT *
FROM person
WHERE address_street_name LIKE '%Northwestern Dr%' 
AND address_number =
	(
	SELECT
	MAX(address_number)
	FROM person
	WHERE address_street_name LIKE '%Northwestern Dr%'
	)
--ORDER BY address_number DESC LIMIT 1;
--14887 Morty Schapiro

SELECT *
FROM person
WHERE name LIKE '%Annabel%' AND address_street_name LIKE '%Franklin Ave%' 
-- 16371 Annabel Miller

SELECT *
FROM interview
WHERE person_id IN (14887, 16371)


SELECT t1.name,
t2.transcript
FROM person t1
INNER JOIN interview t2 ON t1.id = t2.person_id
WHERE 
(t1.address_street_name LIKE '%Northwestern Dr%' 
AND t1.address_number =
	(
	SELECT
	MAX(address_number)
	FROM person
	WHERE address_street_name LIKE '%Northwestern Dr%'
	)
) OR (t1.name LIKE '%Annabel%' AND t1.address_street_name LIKE '%Franklin Ave%');
-- Morty: I heard a gunshot and then saw a man run out. He had a "Get Fit Now Gym" bag. The membership number on the bag started with "48Z". Only gold members have those bags. The man got into a car with a plate that included "H42W".
-- Annabel: I saw the murder happen, and I recognized the killer from my gym when I was working out last week on January the 9th.

SELECT 
	t3.*
FROM 
	get_fit_now_check_in t1
INNER JOIN 
	get_fit_now_member t2 ON t1.membership_id = t2.id
INNER JOIN 
	person t3 ON t2.person_id = t3.id
INNER JOIN 
	drivers_license t4 ON t3.license_id = t4.id
WHERE 
	t1.check_in_date = 20180109 
    AND t1.membership_id LIKE '48Z%'
    AND t4.plate_number LIKE '%H42W%'

-- 67318 Jeremy Bowers es el asesino!!
SELECT *
FROM interview
WHERE person_id = 67318
-- I was hired by a woman with a lot of money. I don't know her name but I know she's around 5'5" (65") or 5'7" (67"). She has red hair and she drives a Tesla Model S. I know that she attended the SQL Symphony Concert 3 times in December 2017.

SELECT
t1.person_id,
t2.name,
t3.car_model,
t3.height,
t3.hair_color,
COUNT(t1.person_id) AS NVeces
FROM facebook_event_checkin t1
INNER JOIN person t2 ON t1.person_id = t2.id
INNER JOIN drivers_license t3 ON t2.license_id = t3.id
WHERE t1.event_name = 'SQL Symphony Concert' 
AND t1.date BETWEEN 20171201 AND 20171231 AND t3.car_model LIKE '%Model S%'
GROUP BY 1,2,3,4,5
HAVING NVeces = 3;

-- 99716 Miranda Priestly La verdadera persona detrás del asesinato!!!








