def main():
    a = 3
    b = 9
    while a <= b:
        if a % 2 == 1:
            print('a is ' + str(a))
            pass
        else:
            print('b is ' + str(b))
            for i in range(b - a):
                print('a * i + b = ' + str(a * i + b))
                pass
            pass
        a += 1
        b -= 1
        pass
    return 0

main()