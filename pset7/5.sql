SELECT title, year FROM movies WHERE "Harry Potter" =  (SELECT substr(title, 1, 12)) ORDER BY year ASC;
