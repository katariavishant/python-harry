# import sys

# # Remove the limit (be careful, printing huge numbers may freeze your program)
# sys.set_int_max_str_digits(0)

# a = 4 * (10**10)
# print(a)   # now it will print the giant number

a = int(input("Enter a number: "))

i = 1
b = 1
while i<=a:
    b = b*i
    i = i+1
print(f"the factorial of {a} is {b}")