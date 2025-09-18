num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ").strip()
match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero."
    case _:
        print("Invalid operation. Please choose +, -, * or /.")

print( f"The result is {result}" if type(result) != str else result)