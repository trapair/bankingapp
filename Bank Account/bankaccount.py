

class BankAccount:

    def __init__(self):

        self.balance = 0.0



    def deposit(self, amount):

        if amount > 0:

            self.balance += amount

            print(f"Deposited: ${amount:.2f}")

        else:

            print("Deposit amount must be positive.")



    def withdraw(self, amount):

        if amount > 0:

            if amount <= self.balance:

                self.balance -= amount

                print(f"Withdrew: ${amount:.2f}")

            else:

                print("Insufficient funds.")

        else:

            print("Withdrawal amount must be positive.")



    def check_balance(self):

        print(f"Current balance: ${self.balance:.2f}")



def main():

    account = BankAccount()

    while True:

        print("\nBank Account Management System")

        print("1. Deposit")

        print("2. Withdraw")

        print("3. Check Balance")

        print("4. Exit")

        

        choice = input("Select an option (1-4): ")

        

        if choice == '1':

            amount = float(input("150: "))

            account.deposit(amount)

        elif choice == '2':

            amount = float(input("100: "))

            account.withdraw(4000)

        elif choice == '3':

            account.check_balance(16000)

        elif choice == '4':

            print("Exiting the system.")

            break

        else:

            print("Invalid option. Please choose again.")



if __name__ == "__main__":

    main()





  
 





 
 