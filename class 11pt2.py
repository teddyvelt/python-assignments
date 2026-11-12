class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def full_name(self):
        name= str(self.year) + self.make
        return(name + self.model).title()

    def read_odometer(self):
        print("miles:"+str(self.odometer))

    def update_odometer(self, miles):
        if miles >= self.odometer:
            self.odometer = miles
        else: print("no rollback!")
    def add_miles(self, more):
        self.odometer += more

my_car = car("toyota", "camry", 2020)

my_car.odometer = 23
my_car.update_odometer = 100
my_car.add_miles = 250