#logical conditions use and, or, not

'''
if you are 18 years old and has ID then you can vote.
'''
while True:
    try:
        age = int(input("Enter your age: "))#get age from user and convert to integer
        hasID = input("Do you have an ID? (yes/no): ").strip().lower()#get ID status from user and convert to lowercase and remove any extra spaces
        if age>=18 and hasID == "yes":#check if age is 18 or older and has ID
            print("You can vote.")#if both conditions are true, print this message      
        else:
            print("You cannot vote.")#if any of the conditions is false, print this message

        #break #exit the loop if input is valid
    except ValueError:
        print("Invalid input. Please enter a valid age.")   