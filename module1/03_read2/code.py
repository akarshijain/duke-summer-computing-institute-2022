def anotherFunction(a, b):
    answer = 42
    x = 0
    print('In anotherFunction({}, {})'.format(a, b))
    while b > a:
        print('a = {}, b = {}'.format(a, b))
        answer = answer + (b - a)
        b -= x
        a += x // 2
        x += 1
        pass
    return answer

def someFunction(x, y):
    a = x + y
    if x < y:
        for i in range(x):
            print('In the loop with i = {}, a = {}'.format(i, a))
            a = a + x
            pass
        pass
    else:
        y = anotherFunction(y, a + 4)
        pass
    return a * y

def main():
    x = 2
    a = someFunction(x, 3)
    print('a = ' + str(a))
    print('x = ' + str(x))
    b = someFunction(3, x)
    print('b = ' + str(b))
    print('x = ' + str(x))
    return 0

main()