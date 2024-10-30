num_1 = int(input("Enter the first value: "))
num_2 = int(input("Enter the second value: "))

opr = input("Enter your operator: ")

if opr == "+": 
    print(f"Sum of two numbers = {num_1 + num_2}")
elif opr == "-":
    print(f"Difference = {num_1 - num_2}")
elif opr == "*":
    print(f"Multiplication = {num_1 * num_2}")
elif opr == "/":
    if num_2 == 0:
        print("Error: Division by zero is undefined.")
    else:
        print(f"Division = {num_1 / num_2}")
elif opr == "%":
    if num_2 == 0:
        print("Error: Modulo by zero is undefined.")
    else:
        print(f"Modulo = {num_1 % num_2}")
else: 
    print("Not a valid operator.")
