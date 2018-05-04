__author__ = 'Ev1g'

from point import Point
import unittest

__all__ = (
    'Car',
    )

class OutOfFuel(Exception):
    """
    Exception raised when not enough fuel for the ride
    can be raised by:
    car.drive()

    """
    pass

class TooMuchFuel(Exception):
    """
    Exception raised when trying to add more fuel to the full tank
    can be raised by:
    car.refill()

    """
    pass

class Car:
    """
    Basic car representation

    Keyword arguments:
    f_capacity     -- max fuel quantity car can handle (int)
    f_consumption  -- fuel needed for 1 distance point (float)
    location       -- position on 2D plane (Point())
    model          -- car model name (string)

    Usage:
    >>> carl = Car(100, 0.5, Point(), 'Mercedes')
    >>> carl.fefill(50)
    >>> carl.drive(x=1, y=2)
    >>> print(carl)
    Mercedes, located at (1, 2) with 49 fuel

    """
    def __init__(self, f_capacity = 60, f_consumption = 0.6, location = Point(), model = 'bmw'):
        self._f_capacity = f_capacity
        self._f_consumption = f_consumption
        self._location = location
        self._model = model
        self._f_amount = 0

    @property
    def f_capacity(self):
        return self._f_capacity

    @property
    def f_consumption(self):
        return self._f_consumption

    @property
    def location(self):
        return self._location

    @property
    def model(self):
        return self._model

    @property
    def f_amount(self):
        return self._f_amount

    def drive(self, destination = None, **kwargs):
        """
        Car replacement to the 'destination' point
        Only works when car has enough fuel for the whole ride
        Otherwise raises OutOfFuel exception

        Arguments:
        destination -- destination point, can be defined by Point() or coordinates (x=1, y=2)

        """
        destination = destination or Point(**kwargs)

        f_need = self.location.distance(destination) * self._f_consumption

        if self._f_amount >= f_need:
            self._location = destination
            self._f_amount -= f_need
        else:
            raise OutOfFuel('Feed me!')


    def refill(self, fuel):
        """
        replenish car's fuel tank
        raises TooMuchFuel exception when adding fuel to the full tank

        Arguments:
        fuel -- amount of fuel to add (int)

        """
        self._f_amount += fuel

        if self._f_amount > self._f_capacity:
            self._f_amount = self._f_capacity
            raise TooMuchFuel("Please, stop! I'm full of fuel")

    def __str__(self):
        return f'{self._model}, located at {self._location} with {self._f_amount} fuel'

class TestCar(unittest.TestCase):
    def test_init(self):
        carl = Car(100, 0.5, Point(), 'Mercedes')
        self.assertEqual(carl.model, 'Mercedes')
        self.assertEqual(carl.f_capacity, 100)
        self.assertEqual(carl.f_consumption, 0.5)
        self.assertEqual(carl.location, Point(0, 0))
        self.assertEqual(carl.f_amount, 0)

    def test_refill_drive(self):
        carl = Car(100, 0.5, Point(), 'Mercedes')
        closeland = Point(1, 2)

        with self.assertRaises(OutOfFuel):
            carl.drive(closeland)

        carl.refill(5)
        carl.drive(closeland)
        self.assertNotEqual(carl.f_amount, 5)
        self.assertEqual(carl.location, closeland)

        with self.assertRaises(OutOfFuel):
            carl.drive(x=10, y=25)

        carl.refill(50)
        carl.drive(x=5, y=5)
        self.assertEqual(carl.location, Point(5, 5))

        with self.assertRaises(TooMuchFuel):
            carl.refill(200)

        self.assertEqual(carl.f_amount, 100)

    def test_str(self):
        carl = Car(100, 0.5, Point(), 'Mercedes')

        self.assertEqual(str(carl), 'Mercedes, located at (0, 0) with 0 fuel')

if __name__ == '__main__':
    unittest.main()
