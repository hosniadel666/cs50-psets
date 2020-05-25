    -- SELECT movie_id FROM stars WHERE person_id IN (136, 307) GROUP BY stars.movie_id HAVING COUNT(*) = 2;
        SELECT title FROM movies WHERE id IN( SELECT movie_id FROM stars  WHERE stars.person_id IN (SELECT id FROM people WHERE name = "Helena Bonham Carter" OR name = "Johnny Depp")
                                    GROUP BY stars.movie_id HAVING COUNT(*) = 2);

