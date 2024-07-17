import random
import copy
from collections import Counter

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)
    
    def draw(self, amount):
        if amount >= len(self.contents):
            drawn_balls = copy.copy(self.contents)
            self.contents.clear()
            return drawn_balls
        
        drawn_balls = []
        for _ in range(amount):
            removed = self.contents.pop(random.randrange(len(self.contents)))
            drawn_balls.append(removed)
        
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    
    for _ in range(num_experiments):
        # Create a deep copy of the hat object for each experiment
        new_hat = copy.deepcopy(hat)
        
        # Draw balls from the hat
        balls_drawn = new_hat.draw(num_balls_drawn)
        
        # Count the number of each color drawn
        drawn_counter = Counter(balls_drawn)
        
        # Check if the actual counts match or exceed the expected counts
        success = all(drawn_counter.get(color, 0) >= count for color, count in expected_balls.items())
        
        if success:
            successes += 1
    
    return successes / num_experiments

# Example usage:
hat = Hat(blue=5, red=4, green=2)

probability = experiment(hat=hat,
                         expected_balls={"red": 1, "green": 2},
                         num_balls_drawn=4,
                         num_experiments=10000)

print(f"Probability: {probability:.4f}")