#James Moore
#SDEV220-50P
#Module 3 Lab - Case Study: Lists, Functions, and Classes

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        # Initialize the super class attribute
        super().__init__(vehicle_type)
        # Initialize Automobile specific attributes
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print("\n--- Vehicle Information ---")
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

def main():
    # Set vehicle type to "car" as requested
    v_type = "car"
    
    print(f"Enter the details for your {v_type}:")
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    doors = input("Number of doors (2 or 4): ")
    roof = input("Type of roof (solid or sun roof): ")

    # Create the Automobile object
    my_car = Automobile(v_type, year, make, model, doors, roof)

    # Output the data
    my_car.display_info()

if __name__ == "__main__":
    main()