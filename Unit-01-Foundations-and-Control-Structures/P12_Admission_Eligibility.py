maths = float(input("Enter marks in Mathematics: "))
physics = float(input("Enter marks in Physics: "))
chemistry = float(input("Enter marks in Chemistry: "))
per = (maths + physics + chemistry) / 300 * 100
print("Percentage:", per)
if maths >= 50 and physics >= 50 and chemistry >= 50 and per >= 60:
    print("Eligible for admission")
else:
    print("Not eligible for admission")
