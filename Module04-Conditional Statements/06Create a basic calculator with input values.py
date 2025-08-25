
#Basic Calculator with Input Values
#This program performs basic arithmetic operations based on user input. 

while True:
    try:
        num1= float(input("Enter first number: "))#convert input to float   
        num2= float(input("Enter second number: "))#convert input to float
        operation = input("Enter operation (+, -, *, /): ") #get operation from user

        if operation == "+": #check if operation is addition
            result = num1 + num2 #perform addition  
            print(f"{num1} + {num2} = {result}") #print result
        elif operation == "-": #check if operation is subtraction   
            result = num1 - num2 #perform subtraction
            print(f"{num1} - {num2} = {result}") #print result
        elif operation == "*":  #check if operation is multiplication
            result = num1 * num2 #perform multiplication
            print(f"{num1} * {num2} = {result}") #print result  
        elif operation == "/": #check if operation is division
            if num2 != 0: #check if denominator is not zero
                result = num1 / num2 #perform division
                print(f"{num1} / {num2} = {result}") #print result  
            else:
                print("Error: Division by zero is not allowed.") #print error message if denominator is zero
        else:
            print("Invalid operation. Please enter one of +, -, *, /.") #print error message if operation is invalid    
    except ValueError:
        print("Invalid input. Please enter a valid number.") #print error message if input is invalid   


#end of the program
