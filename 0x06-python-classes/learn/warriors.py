#!/usr/bin/python3
import random


class Warrior:

    def __init__(self, name="", health=0):
        self.name = name
        self.health = health

    def attack(self, other):
        amt = random.randint(0, other.health)
        other.health -= amt
        print("{} attacks {} and deals {} damage".format(self.name, other.name, amt))
        print("{} is down to {} health".format(other.name, other.health))


def main():
    sam = Warrior("Sam", 100)
    paul = Warrior("Paul", 100)
    fighters = [sam, paul]
    i = 0
    j = 1
    checker = 0

    while (sam.health is not 0 and paul.health is not 0):
        fighters[i].attack(fighters[abs(i - j)])
        if (i > 0):
            i = 0
        else:
            i += 1

    while (checker < len(fighters)):
        if fighters[checker].health <= 0:
            print("{} has Died and {} is victorous".format(fighters[checker].name, fighters[abs(i - j)].name))

        checker += 1


if __name__ == "__main__":
    main()
