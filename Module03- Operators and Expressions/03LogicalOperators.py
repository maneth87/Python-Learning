#Logical operators  : and, or, not
#and : True if both the operands are true
#or  : True if either of the operands is true   
#not : True if operand is false (negation)


#and operator
print("----And operator--- ")
print("5>3 and 10>5 is",5>3 and 10>5) #True and True = True
print("5>3 and 10<5 is",5>3 and 10<5) #True and False = False 

#or operator
print("----Or operator--- ")
print("5>3 or 10>5 is",5>3 or 10>5) #True or True = True
print("5>3 or 10<5 is",5>3 or 10<5) #True or False = True
print("5<3 or 10<5 is",5<3 or 10<5) #False or False = False 

#not operator
print("----Not operator--- ")
print("not(5>3) is",not(5>3)) #not True = False
print("not(5<3) is",not(5<3)) #not False = True
