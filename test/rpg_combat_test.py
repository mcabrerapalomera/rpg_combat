from rpg_combat.character import Character

def test_character_should_have_properties():
    barbarian = Character()
    assert barbarian.health == 1000
    assert barbarian.level == 1
    assert barbarian.isAlive == True
