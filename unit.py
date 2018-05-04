__author__ = 'Ev1g'

import unittest

__all__ = (
    'Unit',
    )

class UnitIsDead(Exception):
    """
    Exception raised when trying to disturb the dead unit
    Can be raised by the validator self._ensure_unit_is_alive

    """
    pass

class Unit:
    """
    Basic battle-game unit representation

    Keyword arguments:
    name   -- unit name (string)
    hp     -- unit hit points (int)
    damage -- amount of damage the unit can deal in hit points (int)

    Usage:
    >>> human = Unit('Varian', 100, 20)
    >>> orc = Unit("Gul'dan", 70, 50)
    >>> human.attack(orc)
    >>> print(human)
    Varian, 75 hp, 20 dmg
    >>> print(orc)
    Gul'dan, 50 hp, 50 dmg

    """
    def __init__(self, name, hp, damage):
        self._name = name
        self._hp = hp
        self._hp_limit = hp
        self._dmg = damage

    def _ensure_is_alive(self):
        """
        Cheking unit availability to action
        Raises exception when unit is dead

        """
        if self._hp == 0:
            raise UnitIsDead('What is dead may never die')

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @property
    def hp_limit(self):
        return self._hp_limit

    @property
    def dmg(self):
        return self._dmg

    def add_hp(self, hp):
        """
        Healing itself

        Arguments:
        hp -- amount of healing in hit points (int)

        Dead can not be healed
        Can not add more than hp_limit
        """
        self.ensure_is_alive()

        self._hp += hp
        if self._hp > self._hp_limit:
            self._hp = self._hp_limit

    def take_damage(self, dmg):
        """
        Suffering damage

        Arguments:
        dmg -- amount of damage in hit points (int)

        Dead can not be damaged(any longer)
        """
        self._ensure_is_alive()

        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0

    def attack(self, enemy):
        """
        Dealing damage (self.dmg)

        Arguments:
        enemy -- damage reciever (Unit)

        Dead can not attack
        Be ready to suffer a counter_attack
        """
        self._ensure_is_alive()

        enemy.take_damage(self._dmg)
        enemy.counter_attack(self)

    def counter_attack(self, enemy):
        """
        Dealing damage (self.dmg/2)
        Automatically attack back the agressor

        Arguments:
        hp -- amount of healing in hit points (int)

        Dead can not attack
        """
        self._ensure_is_alive()

        enemy.take_damage(self._dmg/2)

    def __str__(self):
        return f'{self._name}, {self._hp} hp, {self._dmg} dmg'

class TestUnit(unittest.TestCase):
    def test_init(self):
        orc = Unit('Thrall', 100, 20)
        self.assertEqual(orc.name, 'Thrall')
        self.assertEqual(orc.hp, 100)
        self.assertEqual(orc.dmg, 20)

    def test_exception(self):
        human = Unit('Varian', 100, 20)
        human.take_damage(100)

        with self.assertRaises(UnitIsDead):
            human.take_damage(1)

    def test_attack(self):
        human = Unit('Varian', 100, 20)
        orc = Unit("Gul'dan", 70, 50)

        human.attack(orc)

        self.assertEqual(orc.hp, 50)
        self.assertEqual(human.hp, 75)

    def test_add_hp(self):
        dummy = Unit('Dummy', 5, 0)

        dummy.take_damage(3)
        dummy.add_hp(10)

        self.assertEqual(dummy.hp, 5)

        dummy.take_damage(5)

        with self.assertRaises(UnitIsDead):
            dummy.add_hp(10)

    def test_str(self):
        orc = Unit('Thrall', 100, 20)

        self.assertEqual(str(orc), 'Thrall, 100 hp, 20 dmg')

if __name__ == '__main__':
    unittest.main()
