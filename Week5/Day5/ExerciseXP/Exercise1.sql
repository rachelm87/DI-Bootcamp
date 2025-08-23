-- Exercise 1: DVD Rental

-- 1. Get a list of all the languages, from the language table.
SELECT name FROM Language; 

-- 2 list of all films joined with their languages – select the following details : film title, description, and language name.

SELECT film.title, film.description, language.name FROM film
JOIN language ON film.language_id = language.language_id;

/* 
get all languages, even if no films in that language
*/

SELECT language.name, film.title, film.description FROM language
LEFT JOIN film ON language.language_id = film.language_id;

/* 
New table called new_film with the following columns : id, name. Add some new films to the table.
*/

-- CREATE TABLE new_film (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(100) NOT NULL
-- );

-- INSERT INTO new_film (name) VALUES
-- ('Mrs. Doubtfire'),
-- ('Stand By Me'),
-- ('An Affair to Remember'),
-- ('The Boondock Saints');

-- SELECT * FROM NEW_FILM

-- Create a new table

-- CREATE TABLE customer_review (
--     review_id SERIAL PRIMARY KEY,
--     film_id INT NOT NULL,
--     language_id INT NOT NULL,
--     title VARCHAR(100) NOT NULL,
--     score SMALLINT NOT NULL CHECK (score BETWEEN 1 AND 10),
--     review_text TEXT NOT NULL,
--     last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
--     FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE,
--     FOREIGN KEY (language_id) REFERENCES language(language_id) ON UPDATE CASCADE
-- );

-- INSERT INTO customer_review (film_id, language_id, title, score, review_text)
-- VALUES
-- (1, 1, 'Boondock Saints 1999', 9, 'Never gets old, very well written, excellent plot and action, and great cast.'),
-- (4, 1, 'Mrs. Doubtfire (1993)', 7, 'Mrs. Doubtfire is great fun. Strictly speaking, it is not a top example of movie making, but it offers two hours of undeniably solid entertainment.');

-- DELETE FROM new_film
-- WHERE name = 'The Boondock Saints';

SELECT * FROM new_film