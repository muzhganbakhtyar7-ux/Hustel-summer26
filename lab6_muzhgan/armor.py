import random

class Armor:

    def __init__(self, name, max_block):
        """
        Instance properties:
        name: String
        max_block: Integer
        """

        self.name = name
        self.max_block = max_block

    def block(self):
        """
        Return a random block amount.
        """

        return random.randint(0, self.max_block)


if __name__ == "__main__":

    ladybug_suit = Armor("Ladybug Suit", 30)

    print(ladybug_suit.name)
    print(ladybug_suit.block())