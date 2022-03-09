class Character:
    def __init__(self):
        self.health = 1000
        self.level = 1
        self.alive = True

    def damage(self, character, amount):
        character.health = character.health - amount
