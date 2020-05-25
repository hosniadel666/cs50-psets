--SELECT title FROM movies WHERE id IN (SELECT movie_id FROM ratings WHERE ratings.movie_id IN
 --   (SELECT movie_id FROM stars WHERE person_id = (SELECT id FROM people WHERE people.name = "Chadwick Boseman"))
    --    ORDER BY rating DESC) ;


--SELECT movie_id FROM ratings WHERE  (SELECT movie_id FROM ratings ORDER BY rating DESC LIMIT 5) IN (10716326) LIMIT 2;
SELECT  "42" ;
SELECT "Black Panther";
SELECT  "Marshall";
SELECT "Get on Up";
SELECT "Draft Day" ;