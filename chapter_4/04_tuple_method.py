a = (1,45,69,69,"vishant","lakshay","kushagra")
print(a)

count = a.count(69) #count how many times 69 is present in the tuple
print("The count of 69 is:", count)

index = a.index(69) #gives the index of the first occurence of 69
print("The index of 69 is:", index)

print(45 in a) #checks if 45 is present in the tuple or not, returns boolean value
print(len(a)) #gives the length of the tuple