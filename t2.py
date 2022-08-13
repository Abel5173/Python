# print(0)
# assert 'h' != 'w'
# print(1)
# assert False
# print(2)
# assert True
# print(3)
# temp = -10
# assert temp >= 0, 'Colder than absolute zero'
def my_func(x):
    assert x > 0, "Error!"
    print(x)


my_func(-10)
