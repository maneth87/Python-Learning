#project: Grading System:

while True:  #infinite loop
    try:
            
        marks = int(input("Enter your marks(0-100): "))  #get marks from user and convert to integer  
        if marks<0 or marks>100:  #check if marks are valid
            print("Invalid marks. Please enter marks between 0 and 100.")  #if marks are invalid, print this message
            continue  #restart the loop if marks are invalid
        elif marks>=90:#check if marks are 90 or above
            print("Your grade is A+")
        elif marks>=80:#check if marks are 80 or above
            print("Your grade is A")
        elif marks>=70: #check if marks are 70 or above
            print("Your grade is B+")
        elif marks>=60:#check if marks are 60 or above
            print("Your grade is B")    
        elif marks>=50:#check if marks are 50 or above
            print("Your grade is C")    

        else:#if marks are below 50
            print("You are fail. Better luck next time!")   
    except ValueError:
        print("Invalid input. Please enter a valid number between 0 and 100.")
       # break #exit the loop if input is invalid