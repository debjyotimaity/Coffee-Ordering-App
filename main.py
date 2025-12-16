class Coffee:
    # Initialize coffee with name and price
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    # Initialize order with empty list
    def __init__(self):
        self.items = []

    # Add coffee to order
    def add_item(self, coffee):
        self.items.append(coffee)
        print(f"Added {coffee.name} to your order.")

    # Calculate total price
    def total(self):
        return sum(item.price for item in self.items)

    # Show order summary
    def show_order(self):
        if not self.items:
            print("No items in order.")
            return
        print("\nYour Order:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ${item.price}")
        print(f"Total: ${self.total()}\n")

    # Handle checkout process
    def checkout(self):
        if not self.items:
            print("Your cart is empty.")
            return
        self.show_order()

        confirm = input("Proceed to checkout?(yes/no):").strip().lower()
        if confirm == 'yes':
            print("Order Confirmed! Thank You.")
            self.items.clear()
        else:
            print("Checkout Cancelled.")

# Display menu and handle user input
def main():
    menu = [
        Coffee("Espresso", 2.5),
        Coffee("Latte", 3.5),
        Coffee("Cappuccino", 3.0),
        Coffee("Americano", 2.0),
    ]
    order = Order() # Corrected: Call the class constructor

    # User transaction
    while True: # Corrected: 'True' with capital T
        print("\n-----Coffee Menu-----")
        for i, coffee in enumerate(menu, 1):
            print(f"{i}. {coffee.name} - ${coffee.price}")
        print("5. View Order") # Corrected indentation
        print("6. Checkout")   # Corrected indentation
        print("7. Exit")       # Corrected indentation

        choice = input("Choose an option: ")
        if choice in ['1', '2', '3', '4']:
            order.add_item(menu[int(choice) - 1])
        elif choice == '5': # Corrected indentation
            order.show_order()
        elif choice == '6': # Corrected indentation
            order.checkout() # Corrected: Typo 'checout' to 'checkout'
        elif choice == '7': # Corrected indentation
            print("Thanks for visiting. Goodbye!")
            break
        else: # Corrected indentation to match if/elif
            print("Invalid choice. Try again.")

if __name__ == "__main__": # Corrected: spaces and '=='
    main()
