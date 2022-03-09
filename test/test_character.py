from rpg_combat.character import Character


class TestCharacter:
    def test_init(self):
        character = Character()
        assert character.health == 1000
        assert character.level == 1
        assert character.alive
