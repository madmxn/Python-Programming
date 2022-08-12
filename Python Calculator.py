import time
choice = "yes"
while choice == "yes":

    print("[1] - Addition")
    time.sleep(0.5)
    print("[2] - Subtraction")
    time.sleep(0.5)
    print("[3] - Multiplication")
    time.sleep(0.5)
    print("[4] - Division")
    time.sleep(0.5)
    print("[5] - Exit")
    time.sleep(1)
    option = int(input("Enter the number of the operator you will use: "))

    if option == 1:
        print("You have selected addition.")
        time.sleep(1)
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        answer = num1 + num2
        print(num1, "+", num2, "=", answer)
    elif option == 2:
        print("You have selected subtraction.")
        time.sleep(1)
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        answer = num1 - num2
        print(num1, "-", num2, "=", answer)
    elif option == 3:
        print("You have selected multiplication.")
        time.sleep(1)
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        answer = num1 * num2
        print(num1, "x", num2, "=", answer)
    elif option == 4:
        print("You have selected division.")
        time.sleep(1)
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        answer = num1 / num2
        print(num1, "÷", num2, "=", answer)
    elif option == 5:
        exit()
    else:
        option != 1 or 2 or 3 or 4
        print("You have entered an invalid option.")
    choice = input("Would you like to do another opteration: (yes/no) : ").lower()

