# num = 7
# print(num)
# # ######################
# num = 3.14
# print(num)
# # ######################
# num1 = 7
# num2 = 3.14
# Sum = num1 + num2
# print(Sum)
# # #####################
# name = "Gal"
# print(name)
# # #####################
# Name = input("Please enter a name: " )
# print(Name)
# # #####################
# Number = int(input("Please enter a number: "))
# print(Number)
# print(type(Number)) 
# # ######################
# num1 = int(input("Please enter the first number: "))
# num2 = int(input("Please enter the second number: "))
# Sum = num1 + num2
# print(Sum)
# ######################
# num1 = int(input("Please enter the first number: "))
# num2 = int(input("Please enter the second number: "))
# res = num1 > num2
# print(res)
# ######################
# num1 = int(input("Please enter the first number: "))
# num2 = int(input("Please enter the second number: "))
# print(num1 + num2 if num1 < num2 else(num1 * num2 if num1 == num2 else num1 - num2))
# # #######################
number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))
print("\n")
print("------------------------------")
print("\n")
print("C A L C U L A T I O N S")
print("\n")
print("------------------------------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4.  Division")
print("5. Floor Division")
print("6. Modulus")
print("7. Exponent")
print("\n")
print("------------------------------")
print("\n")
choice = int(input("Enter your choice [1-7]: "))
match choice:
    case 1: 
        print(number1 + number2)
    case 2:
        print(number1 - number2)
    case 3:
        print(number1 * number2)
    case 4:
        if number2 != 0:
            print(number1 / number2)
    case 5:
        if number2 != 0:
            print(number1 // number2)
    case 6: 
        print(number1 % number2)
    case 7:
        print(number1^number2)
                           
                    
