pin = int(input("Enter PIN: "))
balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))
if pin != 1234:
    print("Wrong PIN")
elif amount <= 0:
    print("Invalid amount")
elif amount > balance:
    print("Insufficient balance")
else:
    balance = balance - amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)
