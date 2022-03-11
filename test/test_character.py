from rpg_combat.character import Character


class TestCharacter:
    def setup(self):
        self.knight = Character()
        self.prince = Character()

    def test_creation(self):
        assert self.knight.health == 1000
        assert self.knight.level == 1
        assert self.knight.alive

    def test_character_can_damage_character(self):
        old_prince_health = self.prince.health
        self.knight.attack(self.prince)
        assert self.prince.health < old_prince_health
