from rpg_combat.character import Character


class TestCharacter:
    def setup(self):
        self.knight = Character()

    def test_creation(self):
        assert self.knight.health == 1000
        assert self.knight.level == 1
        assert self.knight.alive

    # This test is failing, but not for the RIGHT reason. It should be failing on line 18 on the assertion,
    # but it's failing on line 14. Shauna, we threw you something different here than you may be did with Chris
    # since our tests aren't just functions, but methods within a test Class. Which means every method
    # needs to accept a self parameter.
    def test_character_can_damage_character(self):
        knight = Character()
        prince = Character()
        old_prince_health = prince.health
        # OK, so I was wrong about it failing on the assertion. It fails here first because we don't have an attack method
        knight.attack(prince)
        assert prince.health < old_prince_health
