# def function():
#     print("Subscribe now")
#
# func2 = function1
# def function1
#     func2()

# def funcret(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
# a = funcret(1)
# print(a)
#
# def executor(func):
#     func("this")
#
# executor(print)
#
def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec

# @dec1
def who_is_upendra():
    print("Upendra is a good boy")

who_is_upendra = dec1(who_is_upendra)
who_is_upendra()