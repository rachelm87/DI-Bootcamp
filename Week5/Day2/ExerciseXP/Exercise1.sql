-- #EXERCISE 1 - Items and Customers

-- Database: public

-- DROP DATABASE IF EXISTS public;

-- CREATE DATABASE public
--     WITH
--     OWNER = rachel
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'C'
--     LC_CTYPE = 'C'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- Create two tables, add the items to the table. 
CREATE TABLE items(
item_id SERIAL PRIMARY KEY,
item VARCHAR (50) NOT NULL,
price INT NOT NULL
);

CREATE TABLE customers(
 customer_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (50) NOT NULL
);

INSERT INTO customers (first_name, last_name) VALUES
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson');

-- SELECT * FROM customers;

INSERT INTO items (item, price) VALUES
('Small Desk', 100),
('Large Desk', 300),
('Fan', 80);
-- Use SQL to locate all the items. 

SELECT * FROM items;

-- All the items with a price above 80 (80 not included).
SELECT * FROM items WHERE price > 80;

-- All the items with a price below 300. (300 included)
SELECT * FROM items WHERE price <=300;

-- All customers whose last name is ‘Smith’ (What will be your outcome?).
SELECT * FROM customers WHERE last_name = 'Smith';

-- All customers whose last name is ‘Jones’.
SELECT * FROM customers WHERE last_name = 'Jones';

-- All customers whose firstname is not ‘Scott’.
SELECT * FROM customers WHERE first_name <> 'Scott';