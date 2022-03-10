from rpg_combat.character import Character

class TestCharacter:
    def setup(self):
        self.knight = Character()

    def test_creation(self):
        assert self.knight.health == 1000
        assert self.knight.level == 1
        assert self.knight.alive
    
    def test_character_can_damage_character():
        knight = Character()
        prince = Character()
        old_prince_health = prince.health
        knight.attack(prince)
        assert prince.health < old_prince_health
    
