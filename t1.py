# # n = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # result = [num+3 for num in n if num % 3 == 0]
# # print(*result)
# # def all_aboard(a, *args, **kw):
# #     print(a, args, kw)


# # all_aboard(4, 7, 3, 0, x=10, y=64)
# # def all_aboard(a,b, *args, **kw):
# #     print(a,b, args, kw)


# # all_aboard(4, 7, 3, 0, x=10, y=64)
# # def foo(a, b=4, **c):
# #     print(a, b, c)


# # foo(20, c=12)
# # a, b, c = map(int, input().split())
# # print(*(a, b, c))
# # def outer_function(a, b):
# #     def inner_function(c, d):
# #         return c + d
# #     return inner_function(a, b)


# # result = outer_function(5, 10)
# # print(result)
# def a_function(a_parameter):
#     a_variable = 15
#     return a_parameter
# a_function(10)
# print(a_variable)
# a=[0]*100
# print(*a)
# numbers = list(range(20))
# print(*numbers)
n = [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 9]
print(*n[::-1])
