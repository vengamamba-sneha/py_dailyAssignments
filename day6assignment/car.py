class Vehicle:
    def __init__(self,model,brand,year):
        self.year=year
        self.model=model
        self.brand=brand
    def display_vehicle_info(self):
        print(self.model,self.brand,self.year)
    def start_engine(self):
        print('engine started yayyyy')
class Car(Vehicle):
    def __init__(self, model,brand,year,seat_capacity):
        super().__init__(model,brand,year)
        self.seat_capacity=seat_capacity
    def display_car_info(self):
        print(self.seat_capacity)
    def opentruck(self):
        print('open trunck')
class Electric_car(Car):
    def __init__(self, model, brand, year, seat_capacity,charge):
        super().__init__(model, brand, year, seat_capacity)
        self.battery_capacity=charge
    def display_elecar_info(self):
        print(self.battery_capacity)
e=Electric_car('sth','nissan',3333,4,77)
e.display_vehicle_info()
e.start_engine()
e.display_car_info()
e.opentruck()
e.display_elecar_info()
        
