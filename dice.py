import random 

class Dice:
    
    def __init__(self, sides=6, times=1):
        """
        makes a die of any size and stores a number of times to roll it. Defaults to six sided and once
        """
        self.sides = sides
        # self.roll_total = self.roll(sides, times)
        self.times = times
        # self.roll = random.randint(1,sides)
        
    def roll(self):
        """
        rolls a dice of number of sides, 'sides' a number of times, 'times'.
        """
        return sum(random.randint(1, self.sides) for _ in range(self.times))