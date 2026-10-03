n = int(input("Enter number of students: "))
total = 0
highest = 0
lowest = 100
passed = 0
failed = 0
above = 0
for i in range(n):
    m = float(input("Enter marks of student " + str(i + 1) + ": "))
    total = total + m
    if m > highest:
        highest = m
    if m < lowest:
        lowest = m
    if m >= 40:
        passed = passed + 1
    else:
        failed = failed + 1
    if m > 75:
        above = above + 1
print("Class average:", total / n)
print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Passed students:", passed)
print("Failed students:", failed)
print("Students scoring above 75%:", above)
 
