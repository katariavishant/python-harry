# for i in range(1,5,2):
#     a = i*
#     print(f"*")

'''
for n = 3
  *
 ***
*****

for n = 5
    *
   ***
  *****
 *******
*********

'''
n = int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" " *(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")


'''
#another way to do it

n = int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" " *(n-i),end="")
    print("*"*(2*i-1))
    
'''
