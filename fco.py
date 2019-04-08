# def my_func(arg):
#     return arg
#
# def arg_func():
#     print('I\'m function')

# my_func(arg_func)()

# my_func = lambda arg: arg

def fco():
    return lambda n: n + 1

# print(fco)

num_100 = 100
num_101 = fco()(num_100)