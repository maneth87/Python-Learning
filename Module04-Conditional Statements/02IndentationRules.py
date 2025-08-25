#the if, elif,else statements are used for decision making in Python.

#if condition
    #logic
#elif condition2
    #logic
#else
    #logic

temperature = 20
if temperature > 30:
    print("It's a hot")#this statemment is belong to if block
#print("It's a hot")#this statement is not correctly indented indentation, it's getting error:IndentationError: expected an indented block after 'if' statement on line 11
elif temperature > 20:
    print("It's warm")#this statemment is belong to elif block
else:
    print("It's cold")#this statemment is belong to else block