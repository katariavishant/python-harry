


def greatestOfNumber():
    a = int(input("enter number a: "))
    b = int(input("enter number b: "))
    c = int(input("enter number c: "))
    if a>b and a>c:
        print(f"number a is the greatest")
    elif b>a and b>c:
        print("number b is the greatest")
    else:
        print("number c is the greatest")

greatestOfNumber()