basic = float(input("Enter basic salary: "))
da = basic * 20 / 100
hra = basic * 10 / 100
gross = basic + da + hra
if gross > 50000:
    tax = gross * 10 / 100
else:
    tax = gross * 5 / 100
net = gross - tax
print("DA:", da)
print("HRA:", hra)
print("Gross salary:", gross)
print("Tax:", tax)
print("Net salary:", net)
