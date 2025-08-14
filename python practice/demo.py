n = int(input("Enter a number: "))
fact = 1

if n < 0:
    print("Factorial of a negative number doesn't exist.")
else:
    for i in range(1, n + 1):
        fact *= i
    print(f"Factorial of {n} = {fact}")
