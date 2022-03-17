from pyparsing import Char
from rpg_combat.character import Character


def test_character_properties_initializtion():
    knight = Character()
    assert knight.health == 1000
    assert knight.level == 1
    assert knight.isAlive == True

def test_character_deals_damage_to_character():
    knight = Character()
    dragon = Character()
    dragon.damage(knight) 
    assert knight.health < 1000

def test_character_can_die():
    knight = Character()
    dragon = Character()
    dragon.health == 1
    knight.damage(dragon)
    assert dragon.health == 0
    assert dragon.isAlive == False