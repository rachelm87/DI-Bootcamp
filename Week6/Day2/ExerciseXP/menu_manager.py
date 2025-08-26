#Exercise 1 - Continued

from menu_item import get_connection, MenuItem

#create a class method to get one item

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT item_name, item_price FROM ex_restaurant.Menu_Items WHERE item_name = %s",
            (name,)
        )
        row = cursor.fetchone()
        connection.close()

        if row:
            item_name, item_price = row
            return MenuItem(item_name, item_price)
        return None
   #create a class method to get all items 
    @classmethod
    def all_items(cls):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT item_name, item_price FROM ex_restaurant.Menu_Items")
        rows = cursor.fetchall()
        connection.close()

        items = [MenuItem(item_name, item_price) for item_name, item_price in rows]
        return items
    

    