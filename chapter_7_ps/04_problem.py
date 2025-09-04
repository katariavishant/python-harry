# a = int(input("Enter a number: "))
# i = 2
# while i<a and i>1 :
    
#     if a%i==0:
#         print("Not a prime number")
#         i=i+1
#         break
#     elif a==1 or a ==2:
#         print("Prime number")
#         i=i+1
#         break
#     elif a<=0:
#         print("Enter a valid positive number")
#         i=i+1
#         break
#     else:
#         print("Prime number")
#         i=i+1


a = int(input("Enter a number: "))

for i in range(2,a):
    if a%i==0:
        print("Not a prime number")
        break
else:
    print("Prime number")
    
    
