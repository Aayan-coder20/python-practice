n = int(input("Enter Number: "))
if n < 0:
    print(f"Factorial of {abs(n)} is Not Defined")
else:
    f = 1
    for i in range(1, n + 1):
        f *= i
    print(f"Factorial of {n} is {f}")
