message = input("enter your message here:")

a = "harry"

if (a.lower() in message.lower()):
    print("yes this message is talking about harry")
else:
    print("no this message is not talking about harry")