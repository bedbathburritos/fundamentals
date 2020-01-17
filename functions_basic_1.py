# #1 - will print a return of 5
# def a():
#     return 5
# print(a())

# #2 - will print a return of 10
# def b():
#     return 5
# print(a()+a())

# #3 - will return 5 and exit method before it returns 10.
# def c():
#     return 5
#     return 10
# print(c())

# #4 - will return 5 and exit before printing 10. 10 will not print. 
# def d():
#     return 5
#     print(10)
# print(d())

# #5 - x cannot be assigned to a method that has no return so print will print undefined or none in python speak.
# def e():
#     print(5)
# x = e()
# print(x)

# #6 - nothing will happen because the method isn't returning anything so it will error out when trying to add "nonetypes"
# # def f(b,c):
# #     print(b+c)
# # print(f(1,2) + f(2,3))

# #7 - it will return a string of "25"
# def g(b,c):
#     return str(b)+str(c)
# print(g(2,5))
# #8 - it will print 100 and then return 10 and exit before it returns 7.
# def h():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(h())

# #9 - it will return 7, 14, and 21
# def i(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(i(2,3))
# print(i(5,3))
# print(i(2,3) + i(5,3))

# #10 - it will return 8
# def j(b,c):
#     return b+c
#     return 10
# print(j(3,5))

# #11 - it will print 500, 500, 300, and 500 since the function didn't change the global var of b. 
# b = 500
# print(b)
# def k():
#     b = 300
#     print(b)
# print(b)
# k()
# print(b)

# #12 - it will do the exact same thing because a return doesn't change the global scope of B.
# b = 500
# print(b)
# def l():
#     b = 300
#     print(b)
#     return b
# print(b)
# l()
# print(b)

# #13 - it will print 500, 500, and then set b = to the method which sets b to the return value. so print 300 then 300. 
# b = 500
# print(b)
# def m():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=m()
# print(b)

# #14 - it will print 1, 3, and 2
# def n():
#     print(1)
#     nn()
#     print(2)
# def nn():
#     print(3)
# n()

# #15 - it will print 1, 3, 5, then return 10 and set 10 equal to y
# def o():
#     print(1)
#     x = p()
#     print(x)
#     return 10
# def p():
#     print(3)
#     return 5
# y = o()
# print(y)