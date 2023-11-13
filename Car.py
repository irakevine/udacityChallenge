

class Car:
    def __init__(self, brand_name, model, manu_year):
        self.brand_name = brand_name
        self.model = model
        self.manu_year = manu_year

    def car_details(self):
        print(f"Brand: {self.brand_name}, Model: {self.model}, Manufacture Year: {self.manu_year}")

    def get_brand(self):
        return self.brand_name

    def get_model(self):
        return self.model
