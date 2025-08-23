--Exercise 2
-- Select the columns from the “customer” table.
SELECT * FROM customer;

-- Display the names (first_name, last_name) using an alias named “full_name”.
SELECT first_name || ' ' || last_name AS full_name FROM customer;

-- Get all the dates that accounts were created (there should be no duplicates).
SELECT DISTINCT create_date FROM customer; 

-- Get all the customer details in descending order by their first name.
SELECT * FROM customer ORDER BY first_name DESC; 

-- Get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.
SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate ASC;

-- Get the address and the phone number of all customers living in the Texas district. 
SELECT address, phone FROM address WHERE district = 'Texas';

-- Retrieve all movie details where the movie id is either 15 or 150.
SELECT * FROM FILM WHERE film_id = 15 OR film_id = 150; 


-- Check if your favorite movie exists in the database get the film ID, title, description, length and the rental rate from the “film” table.
SELECT film_id, title, description, length, rental_rate FROM film WHERE title = 'Mrs. Doubtfire'; 

-- If can't find, check if spelling error and return film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie.
SELECT film_id, title, description, length, rental_rate FROM film WHERE title ILIKE 'Mr%'; 

-- Find the 10 cheapest movies.
SELECT title, rental_rate FROM film ORDER BY rental_rate ASC LIMIT 10;

-- FIND the next 10 cheapest movies.
SELECT title, rental_rate FROM film ORDER BY rental_rate ASC LIMIT 10 OFFSET 10;


-- join the data in the customer table and the payment table,  get the first name and last name from the curstomer table, and amount and the date of every payment made by a customer, ordered by their id (from 1 to…).
SELECT customer.first_name, customer.last_name, payment.payment_date, payment.amount FROM customer 
INNER JOIN payment on  customer.customer_id = payment.customer_id ORDER BY payment.customer_id ASC;

-- You need to check your inventory. Write a query to get all the movies which are not in inventory.
SELECT film.title FROM film LEFT OUTER JOIN inventory
On film.film_id = inventory.film_id WHERE inventory.film_id IS NULL;

-- Write a query to find which city is in which country.
SELECT city.city, country.country FROM City JOIN country ON city.country_id = country.country_id ORDER BY country.country ASC;

-- Bonus
SELECT staff.staff_id, customer.customer_id, customer.first_name, customer.last_name, payment.amount, payment.payment_date FROM payment 
JOIN customer ON customer.customer_id = payment.customer_id
JOIN staff ON staff.staff_id = payment.staff_id
 ORDER BY  staff.staff_id ASC; 