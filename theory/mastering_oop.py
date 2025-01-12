# 📌 Brief Overview
# Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects," which can contain both data (attributes) and methods (functions).
# It focuses on organizing code into reusable blueprints called classes, which define the structure and behavior of the objects created from them.

# Key Concepts of OOP:

# Classes and Objects:
# Class: A blueprint or template that defines the attributes and methods that the objects created from it will have.
# Object: An instance of a class, representing a specific entity with its own unique data. Multiple objects can be created from the same class.

# Attributes and Methods:
# Attributes: Characteristics or properties of an object (e.g., color, size, name).
# Methods: Actions or behaviors that an object can perform (e.g., drive, speak, calculate).

# The Four Pillars of OOP:
# Encapsulation: Bundling data and methods that operate on that data within a single unit (class). It also involves restricting direct access to some of the object's components for data protection.
# Abstraction: Hiding complex implementation details and exposing only the necessary functionality to the user.
# Inheritance: Creating new classes from existing ones, allowing code reuse and the extension of functionalities.
# Polymorphism: The ability to use a single interface or method to represent different underlying forms (e.g., different objects can have a method with the same name but behave differently).

# Why Use OOP?
# Modularity: OOP allows for better organization of code by breaking it down into (reusable) pieces (classes and objects).
# Reuse: Once we build a class, we can reuse it to create multiple objects, reducing redundancy.
# Scalability: Reusing code enables us to scale applications more efficiently.
# Maintenance: OOP makes it easier to update specific instances of an object rather than modifying the entire catalog of data, or the entire codebase.

# Classes & Objects
# Classes: The blueprint that outlines the attributes and functionality of an object.
# Look at strings, dictionaries, lists. These are all classes in Python with their own methods and attributes.
# Objects: Unique instances of a class, created based on the blueprint.

# Let's create our own class!

class Car:
    pass


my_car = Car()
print(type(my_car))  # Output: <class '__main__.Car'>


# Attributes
#  define the qualities of our objects and are stored in variables within a class.

# Class Attributes: Shared by all instances of the class. They are defined directly within the class body, outside any methods.
# Instance Attributes: Attributes that may vary between different instances. They are defined within a special method called __init__(), which is used to initialize the object when it is created.

class Car:
    # Class Attribute
    wheels = 4

    def __init__(self, make, model):
        # Instance Attributes
        self.make = make
        self.model = model


# Creating instances of the Car class
car1 = Car('Toyota', 'Corolla')
car2 = Car('Honda', 'Civic')

print(car1.wheels)  # Output: 4
print(car1.make)  # Output: Toyota
print(car2.model)  # Output: Civic


# Understanding the __init__ Method
# The __init__ method is a special method in Python used to initialize new objects when they're created.
# It is our class constructor, responsible for adding attributes to an object when creating a new instance of a class.

class Car:
    def __init__(self, make, model, year):
        # Instance Attributes
        self.make = make  # The make of the car (e.g., 'Toyota')
        self.model = model  # The model of the car (e.g., 'Corolla')
        self.year = year  # The year of manufacture (e.g., 2020)


# Creating instances of the Car class
car1 = Car('Toyota', 'Corolla', 2020)
car2 = Car('Honda', 'Civic', 2018)

# Accessing the instance attributes
print(car1.make)  # Output: Toyota
print(car1.model)  # Output: Corolla
print(car1.year)  # Output: 2020

print(car2.make)  # Output: Honda
print(car2.model)  # Output: Civic
print(car2.year)  # Output: 2018


# Instance Methods
# Are functions defined within a class that describe the behaviors or actions that an object created from the class can perform.

class Car:
    def __init__(self, make, model, mileage=0):
        # Instance attributes
        self.make = make
        self.model = model
        self.mileage = mileage

    # Instance method to display car information
    def display_info(self):
        return f"{self.make} {self.model}, Mileage: {self.mileage} miles"

    # Instance method to update the mileage
    def drive(self, miles):
        self.mileage += miles
        return f"Drove {miles} miles. Total mileage is now {self.mileage} miles."


# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 10000)

# Calling instance methods
print(my_car.display_info())  # Output: Toyota Corolla, Mileage: 10000 miles
print(my_car.drive(150))  # Output: Drove 150 miles. Total mileage is now 10150 miles


# Exercise: Create a Person Class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to greet the person
    def greet(self):
        return f"Hello, my name is {self.name}!"

    # Method to simulate a birthday
    def have_birthday(self):
        self.age += 1
        return f"Happy Birthday! You are now {self.age} years old."


# Creating an instance of Person
person1 = Person("Alice", 25)

# Using the methods
print(person1.greet())  # Output: Hello, my name is Alice!
print(person1.have_birthday())  # Output: Happy Birthday! You are now 26 years old.
