#OOP 
class Vehicle:
    def __init__(self, car_number, full_name, age, racing_team, speed, capacity):
        self.__car_number = car_number
        self.__full_name = full_name
        self.set_age(age) #encapsulation --> protect data, so age can't be -5 or smth like that
        self.__racing_team = racing_team
        self.set_speed(speed) #encapsulation
        self.set_capacity(capacity) #encapsulation
        # type as subclass

    def get_age(self):
        return self.__age

    def set_age(self, age):
        while True: 
            age = int(input("Enter age: "))
            if age => 0:
                break
            print("Age cannot be negative!")
        self.__age = age

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        while True: 
            speed = int(input("Enter speed: "))
            if speed => 0:
                break
            print("Speed cannot be negative!")
        self.__speed = speed

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity):
        while True: 
            capacity = int(input("Enter capacity: "))
            if capacity => 0:
                break
            print("Capacity cannot be negative!")
        self.__capacity = capacity

class Racer(Vehicle):
    def __init__(self, car_number, full_name, age, racing_team, speed, capacity, num_completed_races, num_completed_laps):
        super().__init__(car_number, full_name, age,racing_team, speed, capacity)
        self.num_completed_races = num_completed_races
        self.num_completed_laps = num_completed_laps

class SupportVehicle(Vehicle):
    def __init__(self, car_number, full_name, age, racing_team, speed, capacity, crew_size, reliability_rating):
        super().__init__(car_number, full_name, age,racing_team, speed, capacity)
        self.crew_size = crew_size
        self.reliability_rating = reliability_rating


 


