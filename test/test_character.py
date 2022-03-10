from rpg_combat.character import Character

class TestCharacter:
    def setup(self):
        self.knight = Character()

    def test_creation(self):
        assert self.knight.health == 1000
        assert self.knight.level == 1
        assert self.knight.alive
