print("="*30)
print("        MATHEMATICAL CALCULATOR (MC)           ")
print("="*30)
print("  Available Operators: | + | - | * | / | ^ | % |            ")
print("  Available Commands:   C (Clear)   OFF (Exit)            ")
print("="*30)

while True:
    print()
    command = input("Enter number or command: ")

    if command == "OFF":
        print()
        print("="*30)
        print("     Calculator Turned OFF             ")
        print("="*30)
        break

    if command == "C":
        print()
        print("="*30)
        print("        Screen Cleared!             ")
        print("="*30)
        continue

    num1 = float(command)
    operator = input("Enter operator: ")
    num2 = float(input("Enter second number: "))

    print()
    print("-"*30)

    if operator == "+":
        result = num1 + num2
        print(" ", num1, "+", num2, "=", result)

    elif operator == "-":
        result = num1 - num2
        print(" ", num1, "-", num2, "=", result)

    elif operator == "*":
        result = num1 * num2
        print(" ", num1, "*", num2, "=", result)

    elif operator == "/":
        if num2 == 0:
            print("Divsion  By Zero (0) Is Impossible")
        else:
            result = num1 / num2
            print(" ", num1, "/", num2, "=", result)

    elif operator == "^":
        result = num1 ** num2
        print(" ", num1, "^", num2, "=", result)

    elif operator == "%":
        result = num1 % num2
        print(" ", num1, "%", num2, "=", result)

    else:
        print("Invalid Operator!")
        print("Available Operators: | + | - | * | / | ^ | % |")

    print("-"*30)
    print("  (Type C To Clear Screen, OFF To Exit, Or Enter A Number To continue)  ")
