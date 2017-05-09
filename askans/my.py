def normalChar(c):
    s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    n = len(s)
    for i in range(0, n):
        if (c == s[i]):
            return True
    return False


def normalString(s):
    n = len(s)
    if n == 0:
        return False
    for i in range(0, n):
        c = s[i]
        if (normalChar(c) == False):
            return False
    return True