marks = int(input("enter your marks:"))

if (marks >= 90):
    print("your grade is Ex")
elif (marks >= 80 and marks < 90):
    print("your grade is A")
elif (marks >= 70 and marks < 80):
    print("your grade is B")
elif (marks >= 60 and marks < 70):
    print("your grade is C")
elif (marks >= 50 and marks < 60):
    print("your grade is D")
elif (marks < 50 and marks >= 0):
    print("your grade is F")
else:
    print("Invalid marks entered you are dumb as hell!!")
