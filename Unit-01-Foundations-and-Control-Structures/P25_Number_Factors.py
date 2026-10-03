n = int(input("Enter an integer: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
        count = count + 1
print("Total factors:", count)
 
