# print fibonacci sequence

def fibonacci_sequence(n):
    a = 0
    b = 1
    print(a, b)
    for i in range(n):
        new_num = a+b
        print(new_num)
        a = b
        b = new_num


fibonacci_sequence(10)
