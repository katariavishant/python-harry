a = int(input("enter maths marks:"))
b = int(input("enter science marks:"))
c = int(input("enter english marks:"))

mathsPercentage = (a/100)*100
sciencePercentage = (b/100)*100 
englishPercentage = (c/100)*100

totalPercentage = ((a+b+c)/300)*100

if (mathsPercentage >=33 and sciencePercentage >=33 and englishPercentage >=33):
    if (totalPercentage >= 40):
        print("You have passed in all subject and also the exam") 
    else:
        print("You have passed in all subjects but failed the exam")
elif (mathsPercentage <=33 and sciencePercentage <=33 and englishPercentage <=33):
    print("You have failed in maths only")
elif (mathsPercentage >=33 and sciencePercentage <=33 and englishPercentage >=33):
    print("You have failed in science only")
elif (mathsPercentage >=33 and sciencePercentage >=33 and englishPercentage <=33):
    print("You have failed in english only")
elif (mathsPercentage <=33 and sciencePercentage <=33 and englishPercentage >=33):
    print("You have failed in maths and science")
elif (mathsPercentage <=33 and sciencePercentage >=33 and englishPercentage <=33):
    print("You have failed in maths and english")
elif (mathsPercentage >=33 and sciencePercentage <=33 and englishPercentage <=33):
    print("You have failed in science and english")
else:
    print("You have failed in all subjects")