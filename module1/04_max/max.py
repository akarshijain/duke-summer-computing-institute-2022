def max(num1, num2):
    # check if num1 is greater than num2
    if (num1 > num2):
        # if so, your answer is num1
        return num1
        # otherwise, your answer is num2
    else:
        return num2
    pass

def main():
    print('max(42, -69) is ' + str(max(42, -69)))
    print('max(33, 0) is ' + str(max(33, 0)))
    print('max(0.123, 0.223) is ' + str(max(0.123, 0.223)))
    # print the max of -0.123 and -0.223
    print ('max(-0.123, -0.223) is ' + str(max(-0.123, -0.223)))

    return 0

main()