n = int(input("Enter an integer: "))
temp = n
count = 0
while temp > 0:
    count = count + 1
    temp = temp // 10
temp = n
total = 0
while temp > 0:
    digit = temp % 10
    total = total + digit ** count
    temp = temp // 10
if total == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
