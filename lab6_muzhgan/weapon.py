import random
from ability import Ability


class Weapon(Ability):

    def attack(self):
        """
        Return a random attack between half
        and the full max_damage.
        """

        half_damage = self.max_damage // 2
        return random.randint(half_damage, self.max_damage)


if __name__ == "__main__":

    lucky_charm = Weapon("Lucky Charm", 60)

    print(lucky_charm.name)
    print(lucky_charm.attack())