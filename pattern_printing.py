# Pattern Printing
"""
input = Integer n
Boolean = True or False

True n=5
-----
*
**
***
****

False  n=5
------
****
***
**
*
"""

# print("How many row you want to print")
# one= int(input())
# print("Type 1 Or 0")
# two = int(input())
# new = bool(two)
# if new == True:
#     for i in range(1, one+1):
#         for j in range(1, i+1):
#             print("*", end=" ")
#         print()
# elif new ==False:
#     for i in range(one,0,-1):
#         for j in range(1,i+1):
#             print("*", end=" ")
#         print()


#### Second pattern type

# print("Pattern printing")
# num = int(input("Enter num how may row you want to print"))
# print("Enter 1 or 0")
# bool_val = input("1 for True value or 0 for False : ")
# if bool_val == "1":
#     for i in range(0, num+1):
#         print("*"*int(i))
# if bool_val == "0":
#     for i in range(num, 0, -1):
#         print("*"*int(i))