class Customer:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    def __str__(self):
        return f"{self.name} {self.surname} {self.email}"

# Database class to manage customer records
class Database:
    def __init__(self):
        self.customer_records = {}

    # Method to add a customer record to the database
    def add_customer(self, customer_id, customer):
        self.customer_records[customer_id] = customer

    # Method to delete a customer record from the database
    def delete_customer(self, customer_id):
        if customer_id in self.customer_records:
            del self.customer_records[customer_id]
            print("Customer record successfully deleted.")
        else:
            print("Customer not found!!")

    # Method to update a customer record in the database
    def update_customer(self, customer_id, new_record):
        if customer_id in self.customer_records:
            self.customer_records[customer_id] = new_record
        else:
            print("Customer not found!")

    # Method to search for a customer record in the database
    def search_customer(self, customer_id):
        if customer_id in self.customer_records:
            return self.customer_records[customer_id]
        else:
            return None

    # Method to list all customer records in the database
    def list_customers(self):
        print("Customers:")
        for customer_id, customer in self.customer_records.items():
            print(f"Customer ID: {customer_id}, {customer}")


# Database management class that inherits from the Database class
class DatabaseManagement(Database):
    def __init__(self):
        super().__init__()

    # Method to add a new customer record to the database
    def add_customer(self):
        name = input("Customer name: ")
        surname = input("Customer surname: ")
        email = input("Customer email address: ")
        customer_id = name + "-" + surname
        customer = Customer(name, surname, email)
        super().add_customer(customer_id, customer)


def main_menu():
    print("----- Database Management ----- ")
    print("1. Add Customer Record")
    print("2. Update Customer Record")
    print("3. Search Customer Record")
    print("4. Delete Customer Record")
    print("5. List All Customer Records")
    print("6. Exit")


customer_database = DatabaseManagement()

while True:
    main_menu()
    choice = input("Select an option (1-6): ")

    if choice == "1":
        customer_database.add_customer()
    elif choice == "2":
        customer_id = input("Enter the ID of the customer you want to update: ")
        customer = customer_database.search_customer(customer_id)
        if customer:
            name = input("Customer name: ")
            surname = input("Customer surname: ")
            email = input("Customer email address: ")
            new_record = Customer(name, surname, email)
            customer_database.update_customer(customer_id, new_record)
        else:
            print("Customer not found.")
    elif choice == "3":
        customer_id = input("Enter the ID of the customer you want to search for: ")
        customer = customer_database.search_customer(customer_id)
        if customer:
            print("Customer Information:")
            print(customer)
        else:
            print("Customer not found.")
    elif choice == "4":
        customer_id = input("Enter the ID of the customer you want to delete: ")
        customer_database.delete_customer(customer_id)
    elif choice == "5":
        customer_database.list_customers()
    elif choice == "6":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
