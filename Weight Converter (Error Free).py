# Variables
pound = ["pounds", "L", "Pounds", "l", "pound", "Pounds"]
kilograms = ["kilograms", "K", "Kilograms", "k", "kilogram", "kilograms"]

# functions

# Asks the user to enter again if he/she did not type one of the specified options
def enter_again():
    print("Please enter one of the specified options")
    lbs_or_kg = str(input("Is the Wieght in Pounds(L) or Kiligrams(K): "))

    if lbs_or_kg.isnumeric():
        print("Has to be text")
        lbs_or_kg = str(input("Is the Wieght in Pounds(L) or Kiligrams(K): "))
        converter(lbs_or_kg)
    else:
        converter(lbs_or_kg)


# Converts the weight
def converter(type):
    if type.isnumeric():
        print("Has to be text")
        type = str(input("Is the Wieght in Pounds(L) or Kiligrams(K): "))
        converter(lbs_or_kg)
    else:
        if type in pound:
           print("Your weight is "+ str(round(weight / 2.205, 2))+" in kilogr ams")
        elif type in kilograms:
            print("Your weight is "+ str(round(weight * 2.205, 2))+" in pounds.") 
        else:
            enter_again()
            


# Recieves the weight
try:
    weight = float(input("Weight: "))
except:
    print("Please enter a number")
    weight = float(input("Weight: "))

# Asks if the entered number is in pounds or kiligrams
lbs_or_kg = str(input("Is the Wieght in Pounds(L) or Kiligrams(K): "))

# Converts
if lbs_or_kg.isnumeric():
    print("Has to be text")
    lbs_or_kg = str(input("Is the Wieght in Pounds(L) or Kiligrams(K): "))
    converter(lbs_or_kg)
else:
    converter(lbs_or_kg)

