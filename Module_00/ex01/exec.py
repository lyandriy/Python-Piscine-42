import sys

def func():
    s = ' '.join(sys.argv[1:])
    c = s[::-1]
    v = c.swapcase()
    return v

if len(sys.argv) != 1:
    str_line = func()
    print(str_line)
