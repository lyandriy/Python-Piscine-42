from time import sleep

def ft_progress(lst):
   print()
 
def example_one():
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)
    
def example_two():
    listy = range(3333)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        sleep(0.005)
    print()
    print(ret)
   
if __name__ == "__main__":
    example_one()
    example_two()