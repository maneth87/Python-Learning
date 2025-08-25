#loop control statements: break, continue, pass
#break: exit the loop
#continue: skip the current iteration and move to the next iteration    
#pass: do nothing

#break statement
print("Break statement example:")
for i in range(1,10 ): #from 1 to 9
    if i==5:
        break #exit the loop when i is 5
    print("Count is:",i) #print the current count
print("Explaination of break statement: when i is 5, the loop will exit and the print statement will not be executed for i=5 and any value after that. The result will be from 1 to 4 only.")

#continue statement: skip the current iteration and move to the next iteration
print("Continue statement example:")
for i in range(1,10 ): #from 1 to 9
    if i==5:
       continue #skip the current iteration when i is 5
    print("Count is:",i) #print the current count
print("Explaination of continue statement: when i is 5, the loop will skip the print statement for i=5 only and move to the next iteration. The result will be from 1 to 9 except 5.")  
#pass statement: do nothing
print("Pass statement example:")
for i in range(1,10 ): #from 1 to 9
    if i==5:
       pass #do nothing when i is 5
    print("Count is:",i) #print the current count   
print("Explaination of pass statement: when i is 5, the loop will do nothing and move to the next iteration. The result will be from 1 to 9 including 5.")  

#Note: break and continue can be used in both for and while loops, pass can be used in any block of code.