def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error! Division by zero!"
    else:
        return x / y

while True:
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = addition(num1, num2)
    elif choice == '2':
        result = subtraction(num1, num2)
    elif choice == '3':
        result = multiplication(num1, num2)
    elif choice == '4':
        result = division(num1, num2)
    else:
        print("Invalid input!")
        continue

    # Sonucun ondalık kısmını kaldır ve sonucu int'e çevir
    if isinstance(result, float) and result.is_integer():
        result = int(result)

    print("Result:", result)

    devam_et = input("Do you want to continue? (Y/N): ")
    if devam_et.upper() != 'Y':
        break