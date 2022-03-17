class Character():
    def __init__(self):
        self.health = 1000
        self.level = 1
        self.isAlive = True

    def damage(self, character):
        character.health  = character.health - 10