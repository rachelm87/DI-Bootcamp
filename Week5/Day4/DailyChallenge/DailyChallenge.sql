--SQL Puzzle

CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
)

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar');

SELECT * FROM FirstTab

CREATE TABLE SecondTab (
    id integer 
)

INSERT INTO SecondTab VALUES
(5),
(NULL);


SELECT * FROM SecondTab

--QUESTIONS: 
-- Q1: It's 0 or unknown since i can't do anything with null
SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id IS NULL);	
-- Q2: 2 because the second tab is 5 and there are only two numbers in teh first tab that are not 5 or "null"
    SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id = 5);
-- Q3: since 5, null in second, i can't do anything with that, so 0/unknown.
	SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN (SELECT id FROM SecondTab);
-- Q4: 2 because the second tab result is 5 and its checking which are not 5 / null
	SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id IS NOT NULL);

