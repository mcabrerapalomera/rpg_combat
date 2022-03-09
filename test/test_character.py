from rpg_combat.character import Character


class TestCharacter:
    def test_init(self):
        character = Character()
        assert character.health == 1000
        assert character.level == 1
        assert character.alive

# Characters can Deal Damage to Characters.
#    - Damage is subtracted from Health

    def test_character_gets_damaged(self):
        knight = Character()        
        dragon = Character()        
        assert knight.damage(dragon, 2) == 1000 - 2