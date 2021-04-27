'''
This is a calculator
And also another way to do comments
'''
try:
    FirstNumber= float(input("Enter your first number:"))
    operation = input("Enter what operation you want:")
    SecondNuumber = float(input("Enter your second number:"))
    if operation == "+":
        print( FirstNumber + SecondNuumber )
    elif operation == "-":
        print( FirstNumber - SecondNuumber )
    elif operation == "/":
        print( FirstNumber /SecondNuumber )
    elif operation == "*":
        print( FirstNumber* SecondNuumber )
    else:
        print("Error! Invalid operation")
except ZeroDivisionError as err:
    print(err)
