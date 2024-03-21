-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT genre, COUNT(*) AS number_of_shows
FROM hbtn_0d_tvshows
GROUP BY genre
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;