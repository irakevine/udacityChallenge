
from Car import Car

# Creating an instance of the Car class
my_car = Car(brand_name="Toyota", model="Camry", manu_year=2022)

# Accessing and printing car details using the car_details method
my_car.car_details()

# Accessing and printing brand and model using getter methods
brand = my_car.get_brand()
model = my_car.get_model()

print(f"Brand from getter method: {brand}")
print(f"Model from getter method: {model}")
