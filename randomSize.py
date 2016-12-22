def getSize(x):
    if x < 32:
        return x
    if x < 64:
        return x/3
    if x < 128:
        return x/6
    if x < 256:
        return x/12
    if x < 512:
        return x/24
    if x < 1024:
        return x/48
    return x/96
