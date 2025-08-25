#Mini project:
'''Build a simple Biod Generator using user input and print()
'''

name = input("What's your name?: ")
age = int(input("How old are you?: "))
city= input("Which city do you live in?: ")
fact= input("Tell me a fun fact about you: ")

print("\n ----- Here is your biodata -----")
print("Hi, this is", name + ".")
print("I am", age, "years old and I live in ", city + ".")
print("Fun fact about me:", fact + ".")