print("Welcome to the simple calculator!")
operator = input("What operation would you like to use today?\nYou can choose one of the 4 following operators: Addition/Add, Subtraction/Subtract, Multiplication/Multiply, Division/Divide.\n")
operator = operator.lower() #Convert to lower case in case input is not lower case

print(operator)

fullOperators = "addition add subtraction subtract multiplication multiply division divide"

#If operator is invalid
try:
    fullOperators.index(operator)
except ValueError:
    print("You have selected an invalid operator. Please try again.")
    operator = input("What operation would you like to use today?\nYou can choose one of the 4 following options: Addition/Add, Subtraction/Subtract, Multiplication/Multiply, Division/Divide.\n")


#Get the first number of the calculation
while True:
    firstNumber = input("What would you like your second number to be?\n")
    if firstNumber.isdigit() == False: #Check if it is a number
        print("You did not enter a number. Please try again.")
    else:
        break
firstNumber = int(firstNumber) #Convert it to an int

#Get the second number of the calculation
while True:
    secondNumber = input("What would you like your second number to be?\n")
    if secondNumber.isdigit() == False: #Check if it is a number
        print("You did not enter a number. Please try again.")
    else:
        break
secondNumber = int(secondNumber) #Convert it to an int

#Addition
if operator == "addition" or operator == "add":
    print("The answer to " + str(firstNumber) + " + " + str(secondNumber) + " is:")
    print(firstNumber + secondNumber)
#Subtraction
elif operator == "subtraction" or operator == "subtract":
    print("The answer to " + str(firstNumber) + " - " + str(secondNumber) + " is:")
    print(firstNumber - secondNumber)
#Multiplication
elif operator == "multiplication" or operator == "multiply":
    print("The answer to " + str(firstNumber) + " x " + str(secondNumber) + " is:")
    print(firstNumber * secondNumber)
#Devision
elif operator == "division" or operator == "divide":
    print("The answer to " + str(firstNumber) + " / " + str(secondNumber) + " is:")
    print(firstNumber / secondNumber)