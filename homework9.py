class Car:
    def __init__(self, maximum_speed: int, registration_number: str):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.travelled_distance = 0
        self.speed = 0
    def get_maximum_speed(self):
        return self.maximum_speed
    def get_registration_number(self):
        return self.registration_number
    def get_travelled_distance(self):
        return self.travelled_distance
    def get_speed(self):
        return self.speed
    def accelerate(self, change):
        self.speed += change
        if self.speed > self.maximum_speed:
            self.speed = self.maximum_speed
        if self.speed < 0:
            self.speed = 0
    def drive(self, hours: float):
        self.travelled_distance += self.speed * hours




car = Car(142, "ABC-123")
print(car.get_maximum_speed())
print(car.get_registration_number())
print(car.get_travelled_distance())
print(car.get_speed())
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(car.get_speed())
car.accelerate(-200)
print(car.get_speed())
car.accelerate(60)
car.travelled_distance = 2000
car.drive(1.5)
print(f"{car.get_travelled_distance():.1f}")

import random
cars = []
for i in range(1, 11):
    max_speed = random.randint(100, 200)
    number = f"ABC{i}"
    cars.append(Car(max_speed, number))

race_finished = False
hour = 0
while not race_finished:
    hour += 1
    for car in cars:
        a = -10
        b = 15
        change2 = random.randint(-10, 15)
        # could not put in -10 and 15 manually because it only shows (-10, b: 15)
        car.accelerate(change2)
        car.drive(1)
        if car.get_travelled_distance() >= 10000:
            race_finished = True

print(f"{'Registration Number':<23} {'Max Speed':<10} {'Current Speed':<15} {'Travelled Distance':<10}")
print("-" * 70)
for car in cars:
    print(f"{car.get_registration_number():<23} {car.get_maximum_speed():<10} "
          f"{car.get_speed():<14} {car.get_travelled_distance():<18.0f}")

