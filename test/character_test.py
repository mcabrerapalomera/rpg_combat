#    - Health, starting at 1000
#    - Level, starting at 1
#    - May be Alive or Dead, starting Alive (Alive may be a true/false)

def test_character_properties(self):
    knight = Character()
    assert knight.health == 1000
    assert knight.level == 1
    assert knight.isAlive == True