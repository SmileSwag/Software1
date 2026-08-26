import random

points = int(input("How many random points to generate? "))

points_inside_circle = 0
count = 0

while count < points:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    if x**2 + y**2 < 1:
        points_inside_circle += 1
        
    count += 1

pi_approximation = 4 * points_inside_circle / points
print(f"Approximation of pi: {pi_approximation}")