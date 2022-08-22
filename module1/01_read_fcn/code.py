def another_function(a):
    b = a
    a += 2
    print('a is ' + str(a))
    print('b is ' + str(b))
    print('a + b is ' + str(a + b))
    return b

def main():
    x = 5
    y = another_function(x)
    print('y is ' + str(y))
    return 0

main()
