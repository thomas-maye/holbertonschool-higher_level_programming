#!/usr/bin/env python3
"""A module that creates a mystical Dragon"""


class SwimMixin:
    def swim(self):
        """A method that prints: The creature swims!"""
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        """A method that prints: The creature flies!"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        """A method that prints: The dragon roars!"""
        print("The dragon roars!")


if __name__ == "__main__":
    draco = Dragon()
    draco.fly()
    draco.swim()
    draco.roar()