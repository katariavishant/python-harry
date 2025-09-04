n = int(input("Tell which number table to write in reverse order: "))

for i in range(1,11):
    print(f"{n} X {11 - i} = {n*(11 - i)}")