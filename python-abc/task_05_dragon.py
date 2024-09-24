#!/usr/bin/env python3
"""A module that create a mystical Dragon"""


class SwimMixin:
    def swim(self):
        """A method that prints : The dragon is swimming"""
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        """A method that prints : The dragon is flying"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        """A method that prints : The dragon is roaring"""
        print("The creature roars!")
