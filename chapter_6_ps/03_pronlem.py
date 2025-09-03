a = "Make a lot of money"
b = "buy now"
c = "subscribe this"
d = "click this"

message = input("enter your comment:")

if(a in message) or (b in message) or (c in message) or (d in message):
    print("This is a spam message")

else:
    print("This is not a spam message")