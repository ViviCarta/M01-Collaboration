"""Author: Venise Saron
Professor: Ray Storer
Subject: SDEV 220
Last Revised: 2-5-2024
File Name: M03_Lab
Module #: M03 Lab - Case Study: Lists, Functions, and Classes
Github URL: https://github.com/ViviCarta/M01-Collaboration.git
Purpose: This app takes user input about a car's
specifications and outputs the data in a format.
"""

# Create a superclass called Vehicle which contains an attribute for a vehicle type
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    # Formatted string function
    def show_string(self):
        print(f"Vehicle type: {self.vehicle_type}")


# Create a class called Automobile that will inherit the attributes from the superclass
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    # Formatted string function utilizing the newline character
    def show_string(self):
        super().show_string()
        print(f"Year: {self.year}"
              f"\nMake: {self.make}"
              f"\nModel: {self.model}"
              f"\nNumber of doors: {self.doors}"
              f"\nType of roof: {self.roof}")


# Main function that outputs prompts to store data for Automobile class
def main():
    vehicle_type = input("Enter the vehicle type (e.g., car, truck, plane, boat, broomstick): ")
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")

    car = Automobile(vehicle_type, year, make, model, doors, roof)

    # Outputs the user's input using the formatted string plus a heading title
    print("\nVehicle Information")
    car.show_string()


# The entry point for program execution
if __name__ == "__main__":
    main()