# Understanding class attributes and instance attributes in a class - https://medium.com/@euniceadewusic/understanding-class-and-instance-attributes-in-python-e3ae12eb3e66
# What is __dict__ in python? It is a dictionary containing the object’s attributes (class and instance attr).  

class vehicle():
    # class_attr is a class attribute, we can initialize it using class name. It will be same for all the objects of class vehicle.
    class_attr = "Hi, I am a chatbot, will tell you details of different vehicles!"
    model_year = 2024

    def __init__(self, color): # color is instance attribute.
        self.color = color

    def car_features(self, brand, wheels, fuel_type): 
        self.brand = brand
        self.wheels = wheels
        self.fuel_type = fuel_type

    def get_all_features(self):
        print(f"All vehicle models are from year {vehicle.model_year}!")
        print(f"Welcome, we have {self.brand} for you! Here's the description..")
        print(f"Vehicle color is {self.color}.")
        print(f"Vehicle has {self.wheels} number of wheels.")
        print(f"Vehicle's fuel type is {self.fuel_type}.")

def main():
    obj1 = vehicle("black")
    class_var = vehicle.class_attr
    print(class_var)
    obj2 = vehicle("pink")
    obj1.car_features("Audi", 4, "Petrol")
    obj2.car_features("Toyota", 4, "Diesel")
    obj1.get_all_features()
    obj2.get_all_features()
    print("Below are the class attribute names and their values..")
    print(vehicle.__dict__)
    print("Below are the instance(obj1) attribute names and their values..")
    print(obj1.__dict__)

if __name__ == "__main__":
    main()
