class Car:
    def __init__(self, color, speed=0):
        self.color = color
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        print(f"현재 속도: {self.speed}km/h")

    def brake(self):
        self.speed -= 10
        print(f"현재 속도: {self.speed}km/h")

my_car = Car("red")
my_car.accelerate()
my_car.brake()

your_car = Car("blue", 30)
your_car.accelerate ()
