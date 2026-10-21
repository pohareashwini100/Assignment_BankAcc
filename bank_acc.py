class BankAccount:
    def __init__(self):
        self.balance = 5000

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be greater than zero.")

            elif amount > self.balance:
                raise ValueError("Insufficient balance.")

            else:
                self.balance -= amount
                print("Withdrawal successful!")
                print("Remaining balance:", self.balance)

        except ValueError as e:
            print(e)


acc = BankAccount()

W_Amt = int(input("Enter withdrawal amount: "))

acc.withdraw(W_Amt) 