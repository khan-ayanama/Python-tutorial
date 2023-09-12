# Exception handling
# try except else finally

while True:
    try:
        age = int(input('Enter your age: '))
        break
    except ValueError:
        print('invalid input')
    except:
        print('unexpected error...')


if age < 18:
    print('you can\'t play this game')
else:
    print('you can play this game')
