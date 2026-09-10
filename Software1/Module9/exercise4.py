import random
class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours
def race(cars):
    race_continues=True
    while race_continues:
        for car in cars:
            car.accelerate(random.randint(-10,15))
            car.drive(1)
            
            if car.travelled_distance >= 10000:
                race_continues=False
                break
    for car in cars:
        print(f"Car {car.license_plate} has travelled {car.travelled_distance} km at a speed of {car.current_speed} km/h.")
    return



       



car1=Car("ABC-123", 142)
car2=Car("DEF-456", 150)
race([car1, car2])