class Chel:
    def __init__(self, name='Chel'):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, chel):
        self.passengers.append(chel)

    def print_passengers_names(self):
        if self.passengers != []:
            print(f'Names of {self.brand} passengers:')
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f'There are no passengers in {self.brand}')

nick = Chel('Nick')
john = Chel('John')
car = Auto('Mercedes')
car.add_passenger(nick)
car.add_passenger(john)
car.print_passengers_names()
mikhail = Chel('Mikhail')
oleg = Chel('Oleg')
car_bmw = Auto('BMW')
car_bmw.add_passenger(mikhail)
car_bmw.add_passenger(oleg)
car_bmw.print_passengers_names()

car_opel = Auto('Opel')
car_opel.print_passengers_names()