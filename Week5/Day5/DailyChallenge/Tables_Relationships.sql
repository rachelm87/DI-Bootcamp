-- Part I 

CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
)

INSERT INTO customer (first_name, last_name)
VALUES 
  ('John', 'Doe'),
  ('Jerome', 'Lalu'),
  ('Lea', 'Rive');



CREATE TABLE customer_profile (
    customer_id INT PRIMARY KEY,
    isLoggedIn BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (customer_id) REFERENCES customer(id)
);

INSERT INTO customer_profile (customer_id, isLoggedIn) VALUES
(1, TRUE),
(2, FALSE);

/* find name of all customers who are logged in*/
SELECT customer.first_name FROM customer
JOIN customer_profile ON customer.id = customer_profile.customer_id
WHERE customer_profile.isLoggedIN = TRUE;

/*All the customers first_name and isLoggedIn columns, incl those without profile**/

SELECT customer.first_name, customer_profile.isLoggedIn
FROM customer
LEFT JOIN customer_profile 
  ON customer.id = customer_profile.customer_id;

/*Count those not logged in*/
SELECT COUNT(*) FROM customer
JOIN customer_profile ON customer.id = customer_profile.customer_id
WHERE customer_profile.isLoggedIn = FALSE;

-- PART II
/*Create book table*/
CREATE TABLE Book (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(50) NOT NULL
)

INSERT INTO tablesrelationships.book (title, author) VALUES 
('Alice In Wonderland', 'Lewis Carroll'),
  ('Harry Potter', 'J.K Rowling'),
  ('To kill a mockingbird', 'Harper Lee');

CREATE TABLE tablesrelationships.student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    age INT CHECK (age <= 15)
);

INSERT INTO tablesrelationships.student (name, age) VALUES 
('John', 12),
  ('Lera', 11),
  ('Patrick', 10),
  ('Bob', 14);

CREATE TABLE tablesrelationships.library (
    book_fk_id INT,
    student_fk_id INT,
    borrowed_date DATE,
    PRIMARY KEY (book_fk_id, student_fk_id, borrowed_date),
    FOREIGN KEY (book_fk_id) REFERENCES tablesrelationships.book(book_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (student_fk_id) REFERENCES tablesrelationships.student(student_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

/* add new records */
INSERT INTO tablesrelationships.library (book_fk_id, student_fk_id, borrowed_date)
SELECT b.book_id, s.student_id, DATE '2022-02-15'
FROM tablesrelationships.book b
JOIN tablesrelationships.student s ON s.name = 'John'
WHERE b.title = 'Alice In Wonderland';

INSERT INTO tablesrelationships.library (book_fk_id, student_fk_id, borrowed_date)
SELECT b.book_id, s.student_id, DATE '2021-03-03'
FROM tablesrelationships.book b
JOIN tablesrelationships.student s ON s.name = 'Bob'
WHERE b.title = 'To Kill a Mockingbird';

INSERT INTO tablesrelationships.library (book_fk_id, student_fk_id, borrowed_date)
SELECT b.book_id, s.student_id, DATE '2021-05-23'
FROM tablesrelationships.book b
JOIN tablesrelationships.student s ON s.name = 'Lera'
WHERE b.title = 'Alice In Wonderland';

INSERT INTO tablesrelationships.library (book_fk_id, student_fk_id, borrowed_date)
SELECT b.book_id, s.student_id, DATE '2021-08-12'
FROM tablesrelationships.book b
JOIN tablesrelationships.student s ON s.name = 'Bob'
WHERE b.title = 'Harry Potter';

/*Display the data*/

SELECT * FROM tablesrelationships.library

SELECT student.name, book.title, library.borrowed_date
FROM tablesrelationships.library
JOIN tablesrelationships.student ON library.student_fk_id = student.student_id
JOIN tablesrelationships.book ON library.book_fk_id = book.book_id
ORDER BY library.borrowed_date;

SELECT AVG(student.age)FROM tablesrelationships.library JOIN tablesrelationships.student 
ON library.student_fk_id = student.student_id
JOIN tablesrelationships.book ON library.book_fk_id = book.book_id
WHERE book.title = 'Alice In Wonderland';

/*delete a student from the student table*/

DELETE FROM tablesrelationships.student
WHERE name = 'Bob';
