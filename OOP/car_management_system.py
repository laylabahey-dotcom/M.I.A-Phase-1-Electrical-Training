#this library + commands to save the textfile to wherever the script is
import os
import json
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, "garage.json")

#OOP 
#similar to defining a struct in C/C++ 
#class definition and functions
class Vehicle:
    #attributes of superclass declared here
    #self points at the class created beforehand
    def __init__(self, car_number, full_name, age, racing_team, speed, capacity):
        self.__car_number = car_number #private information, not available for public viewing
        self.__full_name = full_name
        self.set_age(age) #encapsulation --> protect data, so age can't be -5 or smth like that
        self.__racing_team = racing_team
        self.set_speed(speed) #encapsulation
        self.set_capacity(capacity) #encapsulation
        # type as subclass

    #setters and getters to read and update information thats privated --> encapsulation
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
            print("Age cannot be negative!")
            return
        self.__age = age

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        if speed < 0:
            print("Speed cannot be negative!")
            return
        self.__speed = speed

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity):
        if capacity < 0:
            print("Capacity cannot be negative!")
            return
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

#define subclass of vehicle
class Racer(Vehicle):
    #define all combined attributes
    def __init__(self, car_number, full_name, age, racing_team, speed, capacity, num_completed_races, num_completed_laps):
        #call only superclass attributes
        super().__init__(car_number, full_name, age,racing_team, speed, capacity)
        #set/initialise the subclass specific attributes
        self.num_completed_races = num_completed_races
        self.num_completed_laps = num_completed_laps
    #polymorphism continuation, func passed in superclass redefined here for the subclass
    def get_preformance_score(self):
        return (self.get_speed() * 10) + self.get_capacity()
    #additional attributes of racer car displayed
    def display_info(self):
        super().display_info()
        print(f"Type: Racer")
        print(f"Number of completed races:  {self.num_completed_races}")
        print(f"Number of completed laps:  {self.num_completed_laps}")
        print(f"Preformance score:  {self.get_preformance_score()}")

#repeat as subclass before, just with this subclass' specific attributes & preformance score and display
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
#need an empty list where the vehicles could be stored

#list whose elements aren't the actual information of the vehicles, but they store the pointers that point towards the objects with determined info
garage = []

def check_in_car():
    #user enters car ID
    car_num = int(input("Enter car number:"))
    for vehicle in garage: #could work like a incrementing loop, vehicle as increment and garage as the array
        if vehicle.get_car_number() == car_num: #not vehicle.car_number because it is private, so needs function to fetch it
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

        vehicle = Racer(car_num, full_name, car_age, racing_team, speed, capacity, completed_races, completed_laps)
        #like structural vhdl, just insert items into their respective blocks
    
    elif(car_type.lower() == "supporting"):
        crew_size = int(input("Enter crew size: "))
        reliability = int(input("Enter reliability rate (0-100): "))
        vehicle = SupportVehicle(car_num, full_name, car_age, racing_team, speed, capacity, crew_size, reliability)

        #add the vehicle to the garage list
        garage.append(vehicle)

#display each car in garage with the for-loop
def view_garage():
    for vehicle in garage:
        vehicle.display_info() #method within a class, so i have to call on object to be able to implement it (object = vehicle)

def tune_up():
    found = 0
    car_num = int(input("Enter the number of the car you want to tune up: "))
    for vehicle in garage:
        #find the car through ID
        if vehicle.get_car_number() == car_num:
            #if found, take from user and set all the new values to object
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
            #confirmation message and display the changes
            print("Your new and improved vehicle specs!")
            vehicle.display_info()
            break
    #error message
    if found == 0:
        print("Vehicle ID not found!")

def retire_car():
    found = 0
    car_num = int(input("Enter the number of the car you want to tune up: "))
    #increment vehicle, and when found, the i of that vehicle will be deleted. deleting the pointer of the wanted object
    for i, vehicle in garage:
        if vehicle.get_car_number() == car_num:
            found = 1
            del garage[i]  #delete the index where the car is stored in the list, because the array stores the pointer that points to the objects, not actual objects
            #confirmation message & display the changes
            print("Your new and improved garage!")
            view_garage()
    #error message
    if found == 0:
            print("Vehicle ID not found! Garage unchanged.")  

def find_car():
    found = 0
    choice = int(input("Would you like to 1) search by name or 2) search by car number? (1 or 2): "))

    #choice determination --> name
    if(choice == 1):
        name = input("Enter name of the car: ")
        for vehicle in garage:
            #lower both so that they could  be compared
            if vehicle.get_full_name().lower() == name.lower():
                found = 1
                print("Found your car!")
                vehicle.display_info()
                break
        if found == 0:
            print("Vehicle not found!")
    #choice determination --> ID  
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

def garage_report():
    #total number of cars & sum of all performance
    total_cars = 0
    sum_performance = 0
    
    for vehicle in garage:
        total_cars = total_cars + 1
        sum_performance = sum_performance + vehicle.get_performance_score()
        #get the racing team of current vehicle
        team = vehicle.get_racing_team()
        #start counting how many cars belong to team
        count = 0
        #loop again through garage
        #compare each vehicle with the current team
        for other_vehicle in garage:
            #if this vehicle belongs to same team, increase count 
            if other_vehicle.get_racing_team() == team:
                count = count + 1
        #adter checking every vehicle, print team and count
        print(team, count)
    
    #average of perfomance and output
    average_performance = sum_performance / total_cars
    print(f"Your total sum of cars is {total_cars}\n")
    print(f"Average performance: {average_performance}\n")

#recurring menu
while True:
    print("     WELCOME TO THE BRAND NEW GARAGE MANAGEMENT SYSTEM       \n")
    print("1) Check in a car\n")
    print("2) View Garage\n")
    print("3) Tune-up your car\n")
    print("4) Retire car\n")
    print("5) Find a car\n")
    print("6) See garage report\n")
    print("7) Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Golly! A new car!\n")
        check_in_car()
        print("New car checked in!\n")
    elif choice == 2:
        print("Let's see that garage!\n")
        view_garage()
        print("Isn't it beautiful?")
    elif choice == 3:
        print("Tune up that car!")
        tune_up()
        print("Serious updates done!")
    elif choice == 4:
        print("Want to retire a car? Oh well, let's do it.")
        retire_car()
        print("Always sad to see a car go.")
    elif choice == 5:
        print("I'll find that car for ya!")
        find_car()
        print("Mission accomplished!")
    elif choice == 6:
        print("Of course you wanna see our amazing garage!")
        garage_report()
        print("Garage report delivered!")
    elif choice == 7:
        print("Hope you had a lovely garage experience! Goodbye.")
        break
    else:
        print("Invalid choice!")
        return
