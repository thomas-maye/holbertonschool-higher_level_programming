#!/usr/bin/env python3
"""A module that defines a class FlyingFish"""


class Fish:
    def swim(self):
        """A method that prints : The fish is swimming"""
        print("The fish is swimming")

    def habitat(self):
        """A method that prints : The fish lives in water"""
        print("The fish lives in water")


class Bird:
    def fly(self):
        """A method that prints : The bird is flying"""
        print("The bird is flying")

    def habitat(self):
        """A method that prints : The bird lives in the sky"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    def fly(self):
        """A method that prints : The flying fish is soaring!"""
        print("The flying fish is soaring!")

    def swim(self):
        """A method that prints : The flying fish is swimming!"""
        print("The flying fish is swimming!")

    def habitat(self):
        """A method that prints : The flying fish lives both in
        water and the sky"""
        print("The flying fish lives both in water and the sky!")

if __name__ == "__main__":
    """Testing and Method Resolution Order Exploration"""
    flying_fish = FlyingFish()

    flying_fish.fly()
    flying_fish.swim()
    flying_fish.habitat()
    print(FlyingFish.mro())