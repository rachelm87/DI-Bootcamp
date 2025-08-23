-- DAILY CHALLENGE
-- Count the number
SELECT COUNT(*) FROM actors;

-- Remind myself how many are in the table anyway
-- SELECT * FROM actors
-- Try to add a new actor with some blank fields. What do you think the outcome will be ?

INSERT INTO Actors (first_name, last_name, age, number_oscars)
VALUES('Emma','Watson', NULL, NULL); 
-- Expected outcome would be that any items requiring a not null would not execute

