from com.sppt.errorhandling.CustomException import MyCustomException


class Car:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}'


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def delete_cars(self, car):
        raise NotImplementedError("We can't delete cars from the garage yet...")  # <-- throw an inbuild error

    def add_cars(self, car):
        if not isinstance(car, Car):
            raise MyCustomException(
                f'You Tried to add a `{car.__class__.__name__}` to garage but u can only add `Car` objects',
                777)
        self.cars.append(car)

if __name__== '__main__':
        garage = Garage()
        car = Car('Ford', 'Fiesta')
        garage.add_cars(car)
        print(f"Garage len:{len(garage)}")
        garage.add_cars('Fiesta')
        print(f"Garage len:{len(garage)}")

        error = MyCustomException("My Custom exception", 400)
        print(f"Exception:{error.__doc__}") # <--- __doc__ reads the documentation message from the


