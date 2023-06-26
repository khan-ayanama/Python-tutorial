# else and finally clause in exception handling

while True:
    try:
        number = int(input('enter a number : '))
    except ValueError:
        print("you didn't entered integer")
    except:
        print('unexpected error')
    else:
        # It will execute when try is successfull
        print(f'user input = {number}')
        break
    finally:
        # It will always execute
        print('finally block')
