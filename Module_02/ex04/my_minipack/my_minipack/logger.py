import time
from random import randint
import os

def log(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        times = end - start
        user = os.getenv("USER", "unknown")
        with open('machine.log', 'a') as file:
            if times > 1:
                file.write(f"({user})Running: {func.__name__.replace('_', ' ').title():<19}[ exec-time = {times:.3f} s ]\n")    
            elif times < 1:
                 file.write(f"({user})Running: {func.__name__.replace('_', ' ').title():<19}[ exec-time = {times:.3f} ms ]\n")   
            file.close()
        return ret
    return wrapper

class CoffeeMachine():
    
    water_level = 100
    
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False
        
    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
            
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")
        
if __name__ == "__main__":
    
    machine = CoffeeMachine()
    
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)