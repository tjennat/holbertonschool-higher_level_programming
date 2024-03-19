-- Script that  lists the number of records with the same score in the table second_table
SELECT `score`, COUNT(*) AS `number` From `second_table` GROUP BY `score` ORDER BY `number` DESC;