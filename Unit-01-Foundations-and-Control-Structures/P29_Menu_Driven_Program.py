
while True:
    print("1. Prime")
    print("2. Palindrome")
    print("3. Armstrong")
    print("4. Factorial")
    print("5. Fibonacci Series")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        n = int(input("Enter a number: "))
        flag = 0
        if n < 2:
            flag = 1
        for i in range(2, n):
            if n % i == 0:
                flag = 1
                break
        if flag == 0:
            print("Prime number")
        else:
            print("Not a prime number")
    elif choice == 2:
        n = int(input("Enter a number: "))
        temp = n
        rev = 0
        while temp > 0:
            rev = rev * 10 + temp % 10
            temp = temp // 10
        if rev == n:
            print("Palindrome")
        else:
            print("Not a palindrome")
    elif choice == 3:
        n = int(input("Enter a number: "))
        temp = n
        count = 0
        while temp > 0:
            count = count + 1
            temp = temp // 10
        temp = n
        total = 0
        while temp > 0:
            total = total + (temp % 10) ** count
            temp = temp // 10
        if total == n:
            print("Armstrong number")
        else:
            print("Not an Armstrong number")
    elif choice == 4:
        n = int(input("Enter a number: "))
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        print("Factorial:", fact)
    elif choice == 5:
        n = int(input("Enter number of terms: "))
        a = 0
        b = 1
        for i in range(n):
            print(a)
            c = a + b
            a = b
            b = c
    elif choice == 6:
        print("Thank you")
        break
    else:
        print("Invalid choice")
    print()
 
