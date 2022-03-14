from rpg_combat.character import Character


def test_character_properties_initializtion():
    knight = Character()
    assert knight.health == 1000
    assert knight.level == 1
    assert knight.isAlive == True

