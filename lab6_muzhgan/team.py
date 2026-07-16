import random


class Team:

    def __init__(self, name):
        """
        Team properties:
        name: String
        heroes: List
        """

        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        """
        Add a hero to the team.
        """
        self.heroes.append(hero)

    def remove_hero(self, name):
        """
        Remove a hero by name.
        """
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)

    def view_all_heroes(self):
        """
        Show every hero on the team.
        """
        print("Heroes on", self.name)

        for hero in self.heroes:
            print(hero.name)

    def attack(self, other_team):
        """
        Team battle.
        """

        living_heroes = []
        living_opponents = []

        for hero in self.heroes:
            if hero.is_alive():
                living_heroes.append(hero)

        for hero in other_team.heroes:
            if hero.is_alive():
                living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:

            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

            hero.battle(opponent)

            living_heroes = []
            living_opponents = []

            for hero in self.heroes:
                if hero.is_alive():
                    living_heroes.append(hero)

            for hero in other_team.heroes:
                if hero.is_alive():
                    living_opponents.append(hero)

    def revive_heroes(self):
        """
        Restore every hero's health.
        """

        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):
        """
        Show hero statistics.
        """

        for hero in self.heroes:
            print(hero.name)
            print("Kills:", hero.kills)
            print("Deaths:", hero.deaths)
            print()