--Exercise  / Part I

/* Create a new database and table with columns */

CREATE TABLE ex_restaurant.Menu_Items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(30) NOT NULL,
    item_price SMALLINT DEFAULT 0
);

SELECT * FROM ex_restaurant.Menu_Items