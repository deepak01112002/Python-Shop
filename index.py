class Snack:
    def __init__(self, snack_id, name, price, availability):
        self.snack_id = snack_id
        self.name = name
        self.price = price
        self.availability = availability

    def update_availability(self, availability):
        self.availability = availability

    def __str__(self):
        return f"Snack ID: {self.snack_id}, Name: {self.name}, Price: {self.price}, Availability: {self.availability}"

class Inventory:
    def __init__(self):
        self.snacks = []

    def add_snack(self, snack):
        self.snacks.append(snack)

    def remove_snack(self, snack_id):
        for snack in self.snacks:
            if snack.snack_id == snack_id:
                self.snacks.remove(snack)
                break

    def update_snack_availability(self, snack_id, availability):
        for snack in self.snacks:
            if snack.snack_id == snack_id:
                snack.update_availability(availability)
                break

    def record_snack_sale(self, snack_id):
        for snack in self.snacks:
            if snack.snack_id == snack_id:
                if snack.availability == "yes":
                    snack.update_availability("no")
                    print(f"Snack {snack.name} sold!")
                else:
                    print(f"Snack {snack.name} is not available for sale.")
                break

    def display_inventory(self):
        for snack in self.snacks:
            print(snack)

def display_menu():
    print("========= Snack Inventory Management =========")
    print("1. Add a snack")
    print("2. Remove a snack")
    print("3. Update snack availability")
    print("4. Record snack sale")
    print("5. Display inventory")
    print("0. Exit")
    print("==============================================")

def get_snack_details():
    snack_id = input("Enter snack ID: ")
    name = input("Enter snack name: ")
    price = input("Enter snack price: ")
    availability = input("Is the snack available? (yes/no): ")
    return snack_id, name, price, availability

def main():
    inventory = Inventory()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            snack_id, name, price, availability = get_snack_details()
            snack = Snack(snack_id, name, price, availability)
            inventory.add_snack(snack)
            print("Snack added to inventory.")

        elif choice == "2":
            snack_id = input("Enter the snack ID to remove: ")
            inventory.remove_snack(snack_id)
            print("Snack removed from inventory.")

        elif choice == "3":
            snack_id = input("Enter the snack ID to update availability: ")
            availability = input("Enter the new availability (yes/no): ")
            inventory.update_snack_availability(snack_id, availability)
            print("Snack availability updated.")

        elif choice == "4":
            snack_id = input("Enter the snack ID sold: ")
            inventory.record_snack_sale(snack_id)

        elif choice == "5":
            inventory.display_inventory()

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

        print()

if __name__ == "__main__":
    main()
