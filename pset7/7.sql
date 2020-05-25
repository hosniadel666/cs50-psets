--SELECT COUNT(rating) FROM ratings WHERE movie_id IN
--(SELECT id FROM movies WHERE year = 2010);
SELECT COUNT(title) FROM movies WHERE id IN
(SELECT id FROM movies WHERE year = 2010);