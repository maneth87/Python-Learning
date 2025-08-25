#gettin input from user

name=input("What is your name?: ")
gender=input("Gender? F/M: ")
# print with f-string
print(f"Hello {name}! Nice to meet you.")
#print with concatenation
print("Your input gender is ",gender)

# convert to uppercase

upperCase = name.upper()
print ("Print Upper:",upperCase)
#convert string to lowercase
print("Print Lower:",upperCase.lower())