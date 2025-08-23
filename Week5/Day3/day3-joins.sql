-- SELECT * FROM movies

-- JOINS IN SQL
------- INNER JOIN: SEE ONLY RELATED ROWS
-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM actors
-- INNER JOIN movies
-- ON actors.actor_id = movies.actor_playing_id

------- LEFT JOIN: SEE ALL COLUMNS FROM THE RIGHT

-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM actors
-- LEFT JOIN movies
-- ON actors.actor_id = movies.actor_playing_id

-- INSERT INTO movies (movie_title, movie_story, actor_playing_id)
-- VALUES ('The lord of the rings - The Fellowship of the ring', 'A ring with mysterious powers lands in the hands of a young hobbit, Frodo. Under the guidance of Gandalf, a wizard, he and his three friends set out on a journey and land in the Elvish kingdom.', NULL)

-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM actors
-- RIGHT JOIN movies
-- ON actors.actor_id = movies.actor_playing_id

-- FULL JOIN: SHOWS ALL THE ROWS FROM BOTH TABLES

-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM actors
-- FULL JOIN movies
-- ON actors.actor_id = movies.actor_playing_id

select * from movies

