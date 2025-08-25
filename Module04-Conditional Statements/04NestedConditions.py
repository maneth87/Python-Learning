#Nested conditionals

#age = 18
#has_ticket = False
while True:
    #get age and ticket status from user
    age = int(input("Enter your age: ")) #convert input to integer
    has_ticket_input = input("Do you have a ticket? (yes/no): ").strip().lower() #convert input to lowercase and remove any extra spaces
    has_ticket = True if has_ticket_input == "yes" else False #convert to boolean       


    if age >= 18: #outer condition
        if has_ticket: #inner condition 
            print("Welcome to the concert!") #if both conditions are true
        else:
            print("You need a ticket to enter.") #if outer condition is true but inner condition is false
    else:#outer condition is false
        print("You must be at least 18 years old to enter.") #if outer condition is false
