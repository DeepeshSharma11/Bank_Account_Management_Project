
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: {amount}. New balance: {self.balance}.")
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance: {self.balance}.")

if __name__ == "__main__":
    account_holder_name = input("Enter the account holder's name: ")
    initial_balance = float(input("Enter the initial balance: "))
    account = BankAccount(account_holder_name, initial_balance)

    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            deposit_amount = float(input("Enter amount to deposit: "))
            account.deposit(deposit_amount)
        elif choice == '2':
            withdraw_amount = float(input("Enter amount to withdraw: "))
            account.withdraw(withdraw_amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Exiting the banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

