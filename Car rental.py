class Car:
    def __init__(self, make, model, year, price_per_day):
        self.make = make
        self.model = model
        self.year = year
        self.price_per_day = price_per_day
        self.rented = False 

    def get_info(self):
        return f"{self.year} {self.make} {self.model} -{self.price_per_day}/day"
    
    def rent_out(self):
        if not self.rented:
            self.rented = True
            return f"you have rented {self.get_info()}"
        else:
            return f"Sorry, {self.get_info()} is already rented."
        
    def return_car(self):
        if self.rented:
            self.rented = False
            return f"you have returned {self.get_info()}"
        else:
            return f"{self.get_info()} was not rented."
        
class Customer:
    def __init__(self,name,license_number):
        self.name = name
        self.license_number = license_number
        self.rented_car = None

    def get_info(self):
        return f"{self.name} - License: {self.license_number}"
        
class Car_rental:
    def __init__(self):
        self.cars = []
        self.customers = []

    def add_car(self, car):
        self.cars.append(car)

    def add_customer(self, customer):
        self.customers.append(customer)

    def rent_car(self, customer, car):
        if car in self.cars and not car.rented:
            if customer in self.customers:
                car.rent_out()
                customer.rented_car = car
                return f"{customer.get_info()} has rented {car.get_info()}"
            else:
                return f"Customer {customer.get_info()} is not registered."
        else:
            return f"Car {car.get_info()} is not available for rent."
        
    def return_car(self, customer):
        if customer in self.customers and customer.rented_car:
            car = customer.rented_car
            car.return_car()
            customer.rented_car = None
            return f"{customer.get_info()} has returned {car.get_info()}"
        else:
            return f"Customer {customer.get_info()} does not have a rented car to return."
        
    def display_available_cars(self):
        available_cars = [car.get_info() for car in self.cars if not car.rented]
        if available_cars:
            return "Available cars:\n" + "\n".join(available_cars)
        else:
            return "No cars available for rent."
system = Car_rental()
car1 = Car("Toyota", "Camry", 2020, 50)
car2 = Car("Honda", "Civic", 2019, 45)
customer1 = Customer("Alice", "A1234567")
customer2 = Customer("Bob", "B7654321")
system.add_car(car1)    
system.add_car(car2)
system.add_customer(customer1)
system.add_customer(customer2)
print(system.display_available_cars())
print(system.rent_car(customer1, car1))
print(system.display_available_cars())
print(system.return_car(customer1))
print(system.display_available_cars())

        
    
    
