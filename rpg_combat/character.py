DAMAGE = 10


class Character:
    def __init__(self):
        self.health = 1000
        self.level = 1
        self.alive = True

    def attack(self, enemy):
        enemy.health = enemy.health - DAMAGE
