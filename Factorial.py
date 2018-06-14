import math
ans = int(input("Which Way do u wants to calculate Factorial: 1 or 2 [Type 1 or 2]"))
def No_1():
 if ans == 1:
    n = int(input("Enter ur Number: "))
    factorial_1 = math.factorial(n)
    print("Factorial of ur Number is: ", factorial_1)
def No_2():
    if ans == 2:
        n = int(input("Enter ur Number: "))
        factorial_2 = 1
        for i in range(2, n+1):
            factorial_2 *= i
        print("Factorial of ur Number is: ", factorial_2)
No_1()
No_2()