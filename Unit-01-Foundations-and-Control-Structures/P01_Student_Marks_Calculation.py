Mark1 = int(input("Enter the mark of the 1st subject:"))
Mark2 = int(input("Enter the mark of the 2nd subject:"))
Mark3 = int(input("Enter the mark of the 3rd subject:"))
Mark4 = int(input("Enter the mark of the 4th subject:"))
Mark5 = int(input("Enter the mark of the 5th subject:"))

Total = Mark1 + Mark2 + Mark3 + Mark4 + Mark5
Average = Total / 5
Percentage = (Total / 500) * 100

print("Total marks of the five subjects= ", Total)
print("Total Average of the five subjects= ", Average)
print("Total percentage of the five subjects= ", Percentage ,"%")
