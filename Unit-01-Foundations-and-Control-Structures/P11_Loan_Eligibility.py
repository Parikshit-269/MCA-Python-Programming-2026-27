age = int(input("Enter age: "))
income = float(input("Enter monthly income: "))
score = int(input("Enter credit score: "))
if age >= 21 and age <= 60 and income >= 25000 and score >= 700:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
