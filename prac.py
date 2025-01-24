class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def display_customers(self):
        print(f"\nCustomers of {self.bank_name}:")
        for customer in self.customers:
            customer.display_info()


class Customer:
    def __init__(self, customer_name, customer_id):
        self.customer_name = customer_name
        self.customer_id = customer_id
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def display_info(self):
        print(f"Customer Name: {self.customer_name}, Customer ID: {self.customer_id}")
        for account in self.accounts:
            account.display_info()


class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display_info(self):
        print(f"Account Number: {self.account_number}, Balance: ${self.balance}")


def add_bank(banks):
    bank_name = input("\nEnter the bank name: ")
    bank = Bank(bank_name)
    banks.append(bank)
    print(f"Bank {bank_name} added successfully!")


def add_customer(banks):
    bank_name = input("\nEnter the bank name where you want to add a customer: ")
    for bank in banks:
        if bank.bank_name == bank_name:
            customer_name = input("Enter customer name: ")
            customer_id = input("Enter customer ID: ")
            customer = Customer(customer_name, customer_id)
            bank.add_customer(customer)
            print(f"Customer {customer_name} added to {bank_name}!")
            return
    print("Bank not found!")


def add_account(banks):
    bank_name = input("\nEnter the bank name where you want to add an account: ")
    for bank in banks:
        if bank.bank_name == bank_name:
            customer_id = input("Enter the customer ID to add an account: ")
            for customer in bank.customers:
                if customer.customer_id == customer_id:
                    account_number = input("Enter account number: ")
                    balance = float(input("Enter initial balance: "))
                    account = Account(account_number, balance)
                    customer.add_account(account)
                    print(f"Account {account_number} added for customer {customer.customer_name}!")
                    return
            print("Customer not found!")
            return
    print("Bank not found!")


def display_data(banks):
    if not banks:
        print("No banks available!")
        return
    for bank in banks:
        bank.display_customers()


def main():
    banks = []
    while True:
        print("\nSelect an option:")
        print("1. Add Bank")
        print("2. Add Customer")
        print("3. Add Account")
        print("4. Display Data")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")

        if choice == '1':
            add_bank(banks)
        elif choice == '2':
            add_customer(banks)
        elif choice == '3':
            add_account(banks)
        elif choice == '4':
            display_data(banks)
        elif choice == '5':
            print("Exiting the system...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
