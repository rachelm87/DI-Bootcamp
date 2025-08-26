from menu_item import MenuItem
from menu_manager import MenuManager

#create a function that shows the user a list of options (i.e. menu)

def show_user_menu():
    print("Select the corresponding letter from one of the following options:\n"
          "View an Item (V)\n"
          "Add an Item (A)\n"
          "Delete an Item (D)\n"
          "Update an Item (U)\n"
          "Show the Menu (S)\n"
          "Exit (E)\n")

    action = input("> ").strip().upper()

    if action == "V":
        view_item()
    elif action == "A":
        add_item_to_menu()
    elif action == "D":
        remove_item_from_menu()
    elif action == "U":
        update_item_from_menu()
    elif action == "S":
        show_restaurant_menu()
    elif action == "E":
        print("Bye!")
        show_restaurant_menu()
    else:
        print("This is not correct. Try Again.")

def view_item():
    name = input("Input the menu item you want to see: ").strip()
    item = MenuManager.get_by_name(name)
    if item:
        print(f"Yes, we have: {item.name} at ({item.price})")
    else:
        print(f"There is no {name} on the menu")
#adds new item
def add_item_to_menu(): 
    name = input("Add a new item to our menu: ").strip()
    price = input("Enter item price (number) - whole numbers only: ").strip()
    try:
        price = int(price)
    except ValueError:
        print("Try again - whole numbers only.")
        return

    item = MenuItem(name, price)
    item.save()
    print("Item was added successfully.")

#removes and calls 
def remove_item_from_menu():
    name = input("What item do you want to remove from the menu: ").strip()
    item = MenuItem(name, 0)
    item.delete()
    print("Item was deleted successfully.")

#updates with new price
def update_item_from_menu(): 
    old_name = input("Enter the current item name: ").strip()
    item = MenuManager.get_by_name(old_name)
    if not item:
        print("Item not found.")
        return

    new_name = input("Enter the new name: ").strip()
    new_price_str = input("Enter the new price (number): ").strip()
    try:
        new_price = int(new_price_str)
    except ValueError:
        print("Price must be a whole number.")
        return

    item.update(new_name, new_price)
    print("Item was updated successfully.")
#shows all items
def show_restaurant_menu():
    items = MenuManager.all_items()
    print("Current restaurant menu:")
    for i in items:
        print(f"- {i.name} ({i.price})")

#calls the user menu
if __name__ == "__main__":
    show_user_menu()
