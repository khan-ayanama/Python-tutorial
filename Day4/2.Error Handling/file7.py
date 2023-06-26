# excercise 1

def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError as err:
        # print("you can't divide a number by zero")
        print(err)
    except TypeError as err:
        print('number must be int or float')
    except:
        print('unexpected error')


# print(divide(10, 0))
print(divide(10, '5'))
