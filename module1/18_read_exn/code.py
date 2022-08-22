def f(x):
    if (x == 7):
        raise ValueError("f(7) is illegal")
    return (x+3)*2
def g(x,y):
    if (not isinstance(x,int)):
        raise TypeError("x must be an int in g(x,y)")
    return x + f(y)
def h(x,y):
    try:
        return g(x,y-3)
    except ValueError as e:
        print(e)
        return 42
    pass
def main():
    for (i,j) in [(1,2), ('hello', 4), (3,10), (4,3)]:
        try:
            print("i= " + str(i) + " j = " + str(j))
            print(str(h(i,j)))
        except TypeError as e:
            print(e)
            pass
        pass
    pass

