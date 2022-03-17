from rpg_combat.character import Character


def test_character_properties_initializtion():
    knight = Character()
    assert knight.health == 1000
    assert knight.level == 1
    assert knight.isAlive == True

#  Characters can Deal Damage to Characters.
#    - Damage is subtracted from Health

def test_character_deals_damage_to_character():
    knight = Character()
    dragon = Character()
    dragon.damage(knight.health) 
    assert knight.health < 1000 