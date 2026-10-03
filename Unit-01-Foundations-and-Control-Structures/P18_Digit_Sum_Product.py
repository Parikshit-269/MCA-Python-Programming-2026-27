n = int(input("Enter an integer: "))
s = 0
p = 1
while n > 0:
    digit = n % 10
    s = s + digit
    p = p * digit
    n = n // 10
print("Sum of digits:", s)
print("Product of digits:", p)
 
