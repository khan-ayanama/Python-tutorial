# make flexible functions

# *operator
# *args

# primitive method of function for two argument
# def total(a,b):
#     return a+b

# print(total(7,4))

# for unlimited arguments ----> arguments get changes into tuple
def all_total(*args):
    total = 0
    for i in args:
        total += i
    return total


print(all_total(1, 2, 3, 4, 5))
