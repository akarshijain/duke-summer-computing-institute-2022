# do not ever try to encrypt data this way for
# real! This is easily broken
def caesarCipher(fname, key):
    with open(fname) as f:
        for line in f:
            ans=''
            for c in line:
                if c.isalpha():
                    base= ord('A') if c.isupper() else ord('a')
                    c= ord(c)-base
                    c = c + key
                    c = c  % 26
                    c = c + base
                    c = chr(c)
                    pass
                if (c != '\n'):
                    ans=ans+c
                pass
            print(ans)
            pass
        pass
    pass


