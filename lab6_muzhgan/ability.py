import random

class Ability:

    def __init__(self, name, max_damage):
        """
        Instance properties:
        name: String
        max_damage: Integer
        """

        self.name = name
        self.max_damage = max_damage

    def attack(self):
        """
        Return a random attack damage.
        """

        return random.randint(0, self.max_damage)


if __name__ == "__main__":

    lucky_charm = Ability("Lucky Charm", 50)

    print(lucky_charm.name)
    print(lucky_charm.attack())