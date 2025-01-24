class Menu:
    def __init__(self):
        self.menu_items = {
            "1": {"name": "Samosa", "price": 20},
            "2": {"name": "Burger", "price": 50},
            "3": {"name": "Vada Pav", "price": 30},
            "4": {"name": "Shake", "price": 40}
        }

    def display_menu(self):
        print("Menu:")
        for key, value in self.menu_items.items():
            print(f"{key}. {value['name']} - ₹{value['price']}")

    def get_order(self):
        order = input("Enter the number of the item you'd like to order: ")
        if order in self.menu_items:
            print(f"You've ordered {self.menu_items[order]['name']}.")
        else:
            print("Invalid order. Please try again.")

    def run(self):
        while True:
            self.display_menu()
            self.get_order()
            cont = input("Would you like to order again? (yes/no): ")
            if cont.lower() != "yes":
                break


if __name__ == "__main__":
    menu = Menu()
    menu.run()