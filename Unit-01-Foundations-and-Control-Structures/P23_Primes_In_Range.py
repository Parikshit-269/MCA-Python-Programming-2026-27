start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
count = 0
for n in range(start, end + 1):
    if n < 2:
        continue
    flag = 0
    for i in range(2, n):
        if n % i == 0:
            flag = 1
            break
    if flag == 0:
        print(n)
        count = count + 1
print("Total prime numbers:", count)
 
