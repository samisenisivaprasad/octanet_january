class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transaction_history = []

class ATM:
    def __init__(self):
        self.users = {
            '123456': User('123456', '1234'),
            '789012': User('789012', '5678')
        }
        self.current_user = None

    def login(self, user_id, pin):
        user = self.users.get(user_id)
        if user and user.pin == pin:
            self.current_user = user
            return True
        else:
            print("Invalid user ID or PIN. Please try again.")
            return False

    def display_menu(self):
        print("\n1. Transactions History")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Quit")

    def perform_transaction_history(self):
        print("\nTransaction History:")
        for transaction in self.current_user.transaction_history:
            print(transaction)

    def perform_withdraw(self, amount):
        if amount > 0 and amount <= self.current_user.balance:
            self.current_user.balance -= amount
            self.current_user.transaction_history.append(f"Withdrawal: ${amount}")
            print(f"Withdrawal successful. Current balance: ${self.current_user.balance}")
        else:
            print("Invalid amount or insufficient funds.")

    def perform_deposit(self, amount):
        if amount > 0:
            self.current_user.balance += amount
            self.current_user.transaction_history.append(f"Deposit: ${amount}")
            print(f"Deposit successful. Current balance: ${self.current_user.balance}")
        else:
            print("Invalid amount.")

    def perform_transfer(self, recipient_id, amount):
        recipient = self.users.get(recipient_id)
        if recipient and amount > 0 and amount <= self.current_user.balance:
            self.current_user.balance -= amount
            recipient.balance += amount
            self.current_user.transaction_history.append(f"Transfer to {recipient.user_id}: ${amount}")
            recipient.transaction_history.append(f"Transfer from {self.current_user.user_id}: ${amount}")
            print(f"Transfer successful. Current balance: ${self.current_user.balance}")
        else:
            print("Invalid recipient, amount, or insufficient funds.")

    def run_atm(self):
        print("Welcome to the ATM!")
        user_id = input("Enter your user ID: ")
        pin = input("Enter your PIN: ")

        if self.login(user_id, pin):
            while True:
                self.display_menu()
                choice = input("Enter your choice (1-5): ")

                if choice == '1':
                    self.perform_transaction_history()
                elif choice == '2':
                    amount = float(input("Enter withdrawal amount: $"))
                    self.perform_withdraw(amount)
                elif choice == '3':
                    amount = float(input("Enter deposit amount: $"))
                    self.perform_deposit(amount)
                elif choice == '4':
                    recipient_id = input("Enter recipient's user ID: ")
                    amount = float(input("Enter transfer amount: $"))
                    self.perform_transfer(recipient_id, amount)
                elif choice == '5':
                    print("Thank you for using the ATM. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")

# Example usage
atm = ATM()
atm.run_atm()