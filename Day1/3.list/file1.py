##################  FUNCTIONS   ###################

# Function for adding two number
def add_two(a, b):
    return a+b


# print(add_two(5, 4))

fname = 'ayan'
lname = 'khan'

# print(add_two(fname, lname))


# Function inside Function

def greater(a, b):
    if a > b:
        return a
    return b


def new_greatest(a, b, c):
    return greater(greater(a, b), c)


ans = new_greatest(10, 20, 39)
# print(ans)

# Is Palindrome


def is_palindrome(name):
    if name[::-1] == name:
        return 1
    return 0


ans = is_palindrome('namsan')
print(ans)
