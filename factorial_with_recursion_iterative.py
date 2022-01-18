# # # find factorial with iteration method ?
# # # n!= n * n-1 * n-2 * n-3......1
# # # n! = n * (n-1)!
# def factorial_iterative(n):
#     """
#
#     :param n: Integer
#     :return: n * n-1 * n-2 * n-3.....1
#     """
#     fac = 1
#     for i in range(n):
#         fac = fac*(i+1)
#     return fac
#
#
# number = int(input("Enter the number"))
# print("Factorial Using Iterative Method", factorial_iterative(number))


#### find factorial using recursive method.

def factorial_recursive(n):
    """

    :param n:
    :return:
    """
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

number = int(input("Enter then number"))
print("factorial Using Iterative method", factorial_recursive(number))