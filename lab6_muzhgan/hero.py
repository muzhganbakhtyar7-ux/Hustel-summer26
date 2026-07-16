import random
from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:

    def __init__(self, name, starting_health=100):
        """
        Instance properties:
        name: String
        starting_health: Integer
        current_health: Integer
        """

        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

        # Lists for hero items
        self.abilities = []
        self.armors = []

        # Statistics
        self.kills = 0
        self.deaths = 0


    def add_ability(self, ability):
        """
        Add an ability to the hero.
        """
        self.abilities.append(ability)


    def add_weapon(self, weapon):
        """
        Add a weapon to the hero.
        Weapons are also abilities.
        """
        self.abilities.append(weapon)


    def attack(self):
        """
        Add up all attack damage from abilities.
        """

        total_damage = 0

        for ability in self.abilities:
            total_damage += ability.attack()

        return total_damage


    def add_armor(self, armor):
        """
        Add armor to the hero.
        """

        self.armors.append(armor)


    def defend(self):
        """
        Add up all armor blocks.
        """

        total_block = 0

        for armor in self.armors:
            total_block += armor.block()

        return total_block


    def take_damage(self, damage):
        """
        Reduce health after armor blocks damage.
        """

        damage = damage - self.defend()

        if damage > 0:
            self.current_health -= damage


    def is_alive(self):
        """
        Check if hero is alive.
        """

        return self.current_health > 0


    def add_kill(self, num_kills):
        """
        Add kills to the hero.
        """

        self.kills += num_kills


    def add_death(self):
        """
        Add one death to the hero.
        """

        self.deaths += 1


    def battle(self, opponent):
        """
        Hero fights opponent until one loses.
        """

        if len(self.abilities) == 0 or len(opponent.abilities) == 0:
            print("Draw")
            return


        while self.is_alive() and opponent.is_alive():

            opponent.take_damage(self.attack())

            if opponent.is_alive():

                self.take_damage(opponent.attack())


        if self.is_alive():

            self.add_kill(1)
            opponent.add_death()

            print(self.name + " won!")


        else:

            opponent.add_kill(1)
            self.add_death()

            print(opponent.name + " won!")



if __name__ == "__main__":

    # Ladybug and Cat Noir test

    ladybug = Hero("Ladybug", 150)
    cat_noir = Hero("Cat Noir", 150)


    # Abilities

    lucky_charm = Ability("Lucky Charm", 40)
    cataclysm = Ability("Cataclysm", 45)


    # Armor

    ladybug_suit = Armor("Ladybug Suit", 20)
    cat_suit = Armor("Cat Suit", 15)


    # Add abilities

    ladybug.add_ability(lucky_charm)
    cat_noir.add_ability(cataclysm)


    # Add armor

    ladybug.add_armor(ladybug_suit)
    cat_noir.add_armor(cat_suit)


    # Battle

    ladybug.battle(cat_noir)