num = input("Enter a number whose factorial is to be calculated: ")
try:
    num = int(num)
    if num < 0:
        print("Factorial of negative numbers is not defined!")
    elif num == 0:
        print("Factorial of 0 is always 1.")
    else:
        f = 1
        factors = []
        for i in range(num, 0, -1):
            f *= i
            if num%i == 0:
                factors.append(i)
        print("Factors of", num, "are", factors[::-1])
        print("Factorial of", num, "is", f)
except ValueError:
    print("Error: Please enter a whole number!")
