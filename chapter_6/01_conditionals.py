a = int(input("Enter your age: "))
# if elif else ladder
if(a>=18 and a<=120):
    print("You are eligible to vote")

elif(a<0):
    print("You are dumb enough to enter a negative age") 
elif(a==0):
    print("You have entered 0 which is not a valid age")
elif(a>120):
    print("You can't live that long dumbass")

else:
    print("You are not eligible to vote")  

# print("This will always execute")    
