import sys

def func():
    num = int(sys.argv[1])
    if num == 0:
        print("I'm Zero.")
    elif num % 2 == 0:
        print ("I'm Even.")
    else:
        print("I'm Odd.")
    
if len(sys.argv) == 2:
    if sys.argv[1].isnumeric():
        func()
    else:
        print("AssertionError: argument is not an integer")
elif len(sys.argv) > 2:
    print("AssertionError: more than one argument are provided")