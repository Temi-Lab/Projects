num1 = input("Enter the first number: ")
oper = input("Enter the operation: ")
num2 = input("Enter the second number: ")

if oper == "+":
    try:
        print(float(num1)+float(num2))
    except:
        print("Not a valid number")
elif oper == "-":
    try:
        print(float(num1)-float(num2))
    except:
        print("Not a valid number")
elif oper == "/":
    try:
        print(float(num1)/float(num2))
    except:
        print("Not a valid number")
elif oper == "*":
    try:
        print(float(num1)*float(num2))
    except:
        print("Not a valid number")
elif oper == "**":
    try:
        print(float(num1)**float(num2))
    except:
        print("Not a valid number")
else:
    print("invalid operator")
