def getSize(x):
    if x < 16:
        return x
    if x < 32:
        return x/2
    if x < 64:
        return x/3
    if x < 128:
        return x/5
    if x < 256:
        return x/9
    if x < 512:
        return x/17
    if x < 1024:
        return x/33
    if x < 2048:
        return x/65
    if x < 4096:
        return x/128
    return x/255
