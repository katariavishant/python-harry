def sumOfNaturalNumbers(n):
    if n<1:
        return 0 
    return n + sumOfNaturalNumbers(n-1)

a = int(input("1 + 2 + ...... + n , enter the value of n: "))

print(sumOfNaturalNumbers(a))