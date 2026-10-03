
per = float(input("Enter percentage: "))
if per < 0 or per > 100:
    print("Invalid percentage")
elif per >= 90:
    print("Grade O")
elif per >= 80:
    print("Grade A")
elif per >= 70:
    print("Grade B")
elif per >= 60:
    print("Grade C")
elif per >= 40:
    print("Grade D")
else:
    print("Fail")
