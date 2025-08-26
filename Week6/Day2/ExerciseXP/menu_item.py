import psycopg2

#Exercise 1
#set up connection: 

def get_connection():
    return psycopg2.connect(
        database="bootcamp",
        user="rachel",
        password="rachelrd",
        host="localhost",
        port="5432"
    )

## create Class called MenuItem

class MenuItem:
    def __init__(self, name, price):
        self.name = name ##string
        self.price = price ##int


# #create methods to save, delete, update
    def save(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO ex_restaurant.Menu_Items(item_name, item_price) 
                       VALUES (%s, %s)''',
                       (self.name, self.price)
        )
        connection.commit()
        connection.close()
        print(f"{self.name} with {self.price} was successfully saved")

    def delete(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('''DELETE from ex_restaurant.Menu_Items WHERE item_name =%s''',
                       (self.name,) #because it's a tuple, needs a comma
        )
        connection.commit()
        connection.close()
        print(f"{self.name} was successfully deleted")


    def update(self, update_name, update_price):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute ('''UPDATE ex_restaurant.Menu_Items
                        SET item_name =%s, item_price = %s
                        WHERE item_name = %s''',
                        (update_name, update_price, self.name,)
    )
        
        connection.commit()
        connection.close()
        self.name = update_name
        self.price = update_price
        print(f"{self.name} and {self.price} was successfully updated")


def get_menu():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM ex_restaurant.Menu_Items")
    rows = cursor.fetchall()
    connection.close()

    print("Table Updates: ")
    for row in rows:
        print(row)