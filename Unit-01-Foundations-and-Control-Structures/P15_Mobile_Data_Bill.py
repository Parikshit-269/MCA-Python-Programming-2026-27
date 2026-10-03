gb = float(input("Enter data used in GB: "))
if gb <= 5:
    bill = gb * 20
elif gb <= 10:
    bill = 5 * 20 + (gb - 5) * 15
else:
    bill = 5 * 20 + 5 * 15 + (gb - 10) * 10
print("Total bill:", bill)
 
