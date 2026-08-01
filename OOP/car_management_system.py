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

   def get_racing_team(self):
        return self.__racing_team

    def set_racing_team(self, racing_team):
        self.__racing_team = racing_team

    def get_full_name(self):
        return self.__full_name

    def set_full_name(self, full_name):
        self.__full_name = full_name

    def get_car_number(self):
        return self.__car_number

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0:
            break
        print("Age cannot be negative!")
        self.__age = age

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        if speed < 0:
            break
        print("Speed cannot be negative!")
        self.__speed = speed

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity):
        if capacity < 0:
            break
        print("Capacity cannot be negative!")
        self.__capacity = capacity
        
    #polymorphism, define preformance score function in vehicle class and then let each subclass calculate it differently
    def get_preformance_score(self):
        pass
    #polymorphism, define display and let each subclass display different attributes
    def display_info(self):
        print(f"Car Number: {self.__car_number}")
        print(f"Full Name: {self.__full_name}")
        print(f"Age: {self.get_age()}")
        print(f"Racing Team: {self.__racing_team}")
        print(f"Speed: {self.get_speed()}")
        print(f"Capacity: {self.get_capacity()}")

class Racer(Vehicle):
    def __init__(self, car_number, full_name, age, racing_team, speed, capacity, num_completed_races, num_completed_laps):
        super().__init__(car_number, full_name, age,racing_team, speed, capacity)
        self.num_completed_races = num_completed_races
        self.num_completed_laps = num_completed_laps
    def get_preformance_score(self):
        return (self.get_speed() * 10) + self.get_capacity()
    #additional attributes of racer car displayed
    def display_info(self):
        super().display_info()
        print(f"Type: Racer")
        print(f"Number of completed races:  {self.num_completed_races}")
        print(f"Number of completed laps:  {self.num_completed_laps}")
        print(f"Preformance score:  {self.get_preformance_score()}")

class SupportVehicle(Vehicle):
    def __init__(self, car_number, full_name, age, racing_team, speed, capacity, crew_size, reliability_rating):
        super().__init__(car_number, full_name, age,racing_team, speed, capacity)
        self.crew_size = crew_size
        self.reliability_rating = reliability_rating
    def get_preformance_score(self):
        return (self.get_speed() * 5) + (self.get_capacity() * 5)
    #additional attributes of support car displayed
    def display_info(self):
        super().display_info()
        print(f"Type: Support Vehicle")
        print(f"Crew size:  {self.crew_size}")
        print(f"Reliability rating:  {self.reliability_rating}")
        print(f"Preformance score: {self.get_preformance_score()}" )


#Start operations
#Check in A Car

#need an empty list where the vehicles could be stored
garage = []

def check_in_car():
    car_num = int(input("Enter car number:"))
    for Vehicle in garage: #could work like a incrementing loop, vehicle as increment and garage as the array
        if Vehicle.get_car_number() == car_num: #not vehicle.car_number because it is private, so needs function to fetch it
            print("Car number must be unique!")
            return

    full_name = input("Enter full name: ")
    car_age = int(input("Enter the car age: "))
    racing_team = input("Enter racing team name: ")
    speed = int(input("Enter speed of car: "))
    capacity = int(input("Enter capacity of car: "))

    car_type = input("Enter car type (racer/supporting): ")
    if(car_type.lower() == "racer"):
        completed_laps = int(input("Enter number of completed laps: "))
        completed_races = int(input("Enter number of completed races: "))

        Vehicle = Racer(car_num, full_name, car_age, racing_team, speed, capacity, completed_races, completed_laps)
        #like structural vhdl
    
    elif(car_type.lower() == "supporting"):
        crew_size = int(input("Enter crew size: "))
        reliability = int(input("Enter reliability rate (0-100): "))
        Vehicle = SupportVehicle(car_num, full_name, car_age, racing_team, speed, capacity, crew_size, reliability)

        #add the vehicle to the garage list
        garage.append(Vehicle)


def view_garage():
        for vehicle in garage:
            vehicle.display_info() #method within a class, so i have to call on object to be able to implement it (object = vehicle)

def tune_up():
    found = 0
    car_num = int(input("Enter the number of the car you want to tune up: "))
    for vehicle in garage:
        if vehicle.get_car_number() == car_num:
            found = 1
            vehicle.display_info()
            print("Enter your changes now!")
            full_name = input("Enter full name: ")
            vehicle.set_full_name(full_name)
            car_age = int(input("Enter the car age: "))
            vehicle.set_age(car_age)
            racing_team = input("Enter racing team name: ")
            vehicle.set_racing_team(racing_team)
            speed = int(input("Enter speed of car: "))
            vehicle.set_speed(speed)
            capacity = int(input("Enter capacity of car: "))
            vehicle.set_capacity(capacity)
            print("Your new and improved vehicle specs!")
            vehicle.display_info()
            break
    if found == 0:
        print("Vehicle ID not found!")

def retire_car():
    found = 0
    car_num = int(input("Enter the number of the car you want to tune up: "))
    for i, vehicle in garage:
        if vehicle.get_car_number() == car_num:
            found = 1
            del garage[i]  #delete the index where the car is stored in the list, because the array stores the pointer that points to the objects, not actual objects
            print("Your new and improved garage!")
            view_garage()
    if found == 0:
            print("Vehicle ID not found! Garage unchanged.")  

def find_car():
    found = 0
    choice = int(input("Would you like to 1) search by name or 2) search by car number? (1 or 2): "))

    if(choice == 1):
        name = input("Enter name of the car: ")
        for vehicle in garage:
            if vehicle.get_full_name().lower() == name.lower():
                found = 1
                print("Found your car!")
                vehicle.display_info()
                break
        if found == 0:
            print("Vehicle not found!")
    elif(choice == 2):
        car_num = int(input("Enter the number of the car: "))
        for vehicle in garage:
            if vehicle.get_car_number() == car_num:
                found = 1
                print("Found your car!")
                vehicle.display_info()
                break
        if found == 0:
            print("Vehicle not found!")
