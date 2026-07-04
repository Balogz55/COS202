print("================================================")
print("        MATHEMATICAL CALCULATOR (MC)           ")
print("================================================")
print("  Operations: | + | - | * | / | ^ | % |            ")
print("  Commands:   C (Clear)   OFF (Exit)            ")
print("================================================")

while True:
    print()
    command = input("Enter number or command: ")

    if command == "OFF":
        print()
        print("================================================")
        print("     Calculator Turned OFF             ")
        print("================================================")
        break

    if command == "C":
        print()
        print("================================================")
        print("             Screen Cleared!                    ")
        print("================================================")
        continue

    num1 = float(command)
    operator = input("Enter operator (+, -, *, /, //, ^, %): ")
    num2 = float(input("Enter second number: "))

    print()
    print("------------------------------------------------")

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
            print("  ERROR: Cannot divide by zero!")
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
        print("  ERROR: Unknown operator!")

    print("------------------------------------------------")
    print("  (Type C To Clear, OFF To Exit, Or Enter A Number To continue)  ")
