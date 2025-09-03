a = int(input("Enter a number 1: "))
b = int(input("Enter a number 2: "))
c = int(input("Enter a number 3: "))
d = int(input("Enter a number 4: "))

# if(a>b>c>d):
#     print(str(a) + " is the greatest")
# elif(b>a>c>d):
#     print(str(b) + " is the greatest")

# elif(c>a>b>d):
#     print(str(c) + " is the greatest")
# elif(d>a>b>c):
#     print(str(d) + " is the greatest")

if (a>b and a>c and a>d):
    print(f"{a} is the greatest")

elif (b>a and b>c and b>d):
    print(f"{b} is the greatest")

elif (c>a and c>b and c>d):
    print(f"{c} is the greatest")   
else:
    print(f"{d} is the greatest")