from rpg_combat.character import Character


class TestCharacter:
    def setup(self):
        self.knight = Character()
        self.dragon = Character()

    def test_init(self):
        assert self.knight.health == 1000
        assert self.knight.level == 1
        assert self.knight.alive

    # Characters can Deal Damage to Characters.
    #    - Damage is subtracted from Health
    def test_character_gets_damaged(self):
        self.knight.damage(self.dragon, 2)
        assert self.dragon.health == 1000 - 2

    #    - When damage received exceeds current Health, Health becomes 0 and the character dies
    def test_character_dies(self):
        self.knight.damage(self.dragon, 1000)
        assert self.dragon.health == 0
        assert not self.dragon.alive
