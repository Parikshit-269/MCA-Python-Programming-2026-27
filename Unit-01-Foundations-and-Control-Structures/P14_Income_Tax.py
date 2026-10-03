income = float(input("Enter annual income: "))
if income <= 300000:
    tax = 0
elif income <= 700000:
    tax = (income - 300000) * 5 / 100
elif income <= 1000000:
    tax = 400000 * 5 / 100 + (income - 700000) * 10 / 100
elif income <= 1500000:
    tax = 400000 * 5 / 100 + 300000 * 10 / 100 + (income - 1000000) * 15 / 100
else:
    tax = 400000 * 5 / 100 + 300000 * 10 / 100 + 500000 * 15 / 100 + (income - 1500000) * 20 / 100
print("Tax payable:", tax)
