__author__ = 'Ev1g'

import unittest
from math import hypot

__all__ = (
    'Point',
    )


class Point:

    '''
    Representation of point in 2D
    
    Keyword arguments:
    (x, y) - point coordinates (default 0, 0)
    supported type - integer

    Usage:
    >>> a = Point()
    >>> a
    (0, 0)
    >>> b = Point(1,3)
    >>> a != b
    true
    >>>a.distance(b)
    3.16

    '''

    def __init__(self, x = 0, y = 0):

        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def distance(self, other):
        """
        Calculates the distance between two points, 
        takes the second point as a parameter.

        returns float .2

        """
        return round(hypot(self.x - other.x, self.y - other.y), 2)

    def __str__(self):
        return f'({self.x}, {self.y})'

class TestPoint(unittest.TestCase):
    def test_init(self):
        a = Point(1, 2)
        self.assertEqual(a.x, 1)
        self.assertEqual(a.y, 2)

    def test_equality(self):
        a = Point(1, 2)
        b = Point()

        self.assertTrue(a != b)
        self.assertFalse(a == b)

        b.x = 1
        b.y = 2

        self.assertTrue(a == b)
        self.assertFalse(a != b)

    def test_distance(self):
        a = Point(1, 2)
        b = Point(2, 3)
        self.assertEqual(a.distance(b), 1.41)

    def test_str(self):
        a = Point(1, 2)
        self.assertEqual(str(a), '(1, 2)')

if __name__ == '__main__':
    unittest.main()
