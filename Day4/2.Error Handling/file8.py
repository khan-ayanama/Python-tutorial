# python custom exceptions
# Q - Why custom exceptions ?
# A - To increase readability of code

# custom exception
class NameTooShortError(ValueError):
    pass


def validate(name):
    if len(name) < 8:
        raise NameTooShortError('name to short')


print(validate('Ayan'))
