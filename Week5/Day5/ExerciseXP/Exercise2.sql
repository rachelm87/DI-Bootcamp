--EXERCISE2

Task 1: update some film anguages

UPDATE film
SET language_id = 5   -- French
WHERE title ILIKE '%love%'
  AND language_id = 1;  -- English

-- Task 2: Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
-- Answer: Just the "Address ID". Cannot insert a new customer without a valid address. 

-- Task 3: We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
DROP TABLE customer_review  /* was easy because no other tables depended on it*/

-- Task 4: Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
SELECT COUNT(*) FROM rental WHERE return_date IS NULL

-- Task 5: Find the 30 most expensive movies which are outstanding

SELECT film.title, film.replacement_cost, rental.return_date FROM film 
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.film_id = rental.inventory_id
WHERE rental.return_date IS NULL
ORDER BY film.replacement_cost DESC
Limit 30 

-- Task 6: Help my friend!
/*names and sumo*/
SELECT film.film_id, film.title, film.description
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.first_name = 'Penelope'
  AND actor.last_name = 'Monroe'
  AND film.description ILIKE '%sumo%'

/*A short documentary (less than 1 hour long), rated “R”.*/

SELECT title FROM film WHERE length < 60 AND rating = 'R' AND description ILIKE '%documentary%'

/* The 3rd film : Matthew Mahan rented paid over $4.00 for the rental returned it between the 28th of July and the 1st of August, 2005.*/

SELECT film.title
FROM film
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
JOIN customer ON rental.customer_id = customer.customer_id
JOIN payment ON rental.rental_id = payment.rental_id
WHERE customer.first_name = 'Matthew'
  AND customer.last_name = 'Mahan'
  AND payment.amount > 4.00
  AND rental.return_date BETWEEN '2005-07-28' AND '2005-08-01'

/*4th Film: His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.*/
SELECT film.title, film.description, film.replacement_cost
FROM film
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
JOIN customer ON rental.customer_id = customer.customer_id
WHERE customer.first_name = 'Matthew'
  AND customer.last_name = 'Mahan'
  AND (film.title ILIKE '%boat%' OR film.description ILIKE '%boat%')
ORDER BY film.replacement_cost DESC;
