"""Assignment 1 Unit 3 week 2"""

import sqlite3

#from notes in collab to use sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')

def q_all(query):
    curs = conn.cursor()
    curs.execute(query)
    rows = curs.fetchall()
    curs.close()
    return rows

def q_one(query):
    row = q_all(query)
    return row[0][0]

print('Character count:', q_one("SELECT COUNT(*) FROM charactercreator_character"))
# #character types?

print('Character mage:', q_one("SELECT COUNT(*) FROM charactercreator_mage"))
print('Character thief:', q_one("SELECT COUNT(*) FROM charactercreator_thief"))
print('Character cleric:', q_one("SELECT COUNT(*) FROM charactercreator_cleric"))
print('Character fighter:', q_one("SELECT COUNT(*) FROM charactercreator_fighter"))
print('Character necromancer:', q_one("SELECT COUNT(*) FROM charactercreator_necromancer"))

# # How many total Items?
print('Total Items:', q_one("SELECT COUNT(*) FROM armory_item"))

# How many of the Items are weapons? How many are not?
print('Weapons:', q_one("SELECT COUNT (*) FROM armory_weapon"))

print('Nonweapons:', q_one("SELECT COUNT(*) FROM armory_item")-q_one("SELECT COUNT(*) FROM armory_weapon"))

# How many Items does each character have? (Return first 20 rows)
print('Items per Charcter:')
query = """
SELECT name, COUNT(item_id)
FROM charactercreator_character_inventory
INNER JOIN charactercreator_character ON charactercreator_character_inventory.character_id = charactercreator_character.character_id
GROUP BY name
LIMIT 20
"""
for row in q_all(query):
    print(row[0], ':', row[1])

# How many Weapons does each character have? (Return first 20 rows)
print('Weapons per Charcter:')
query = """
SELECT name, COUNT(item_ptr_id)
FROM charactercreator_character_inventory as cci, armory_weapon as aw,
charactercreator_character as cc
WHERE cc.character_id= cci.character_id
AND cci.item_id=aw.item_ptr_id
GROUP BY name
LIMIT 20
"""
for row in q_all(query):
    print(row[0], ':', row[1])

# On average, how many Items does each Character have?
print('AVG Items per Charcter:', q_one("SELECT COUNT(item_id) FROM charactercreator_character_inventory")/q_one("SELECT COUNT(character_id) FROM charactercreator_character_inventory"))

# On average, how many Weapons does each character have?
print('AVG Weapon per Charcter:', q_one("SELECT COUNT(item_ptr_id) FROM armory_weapon")/q_one("SELECT COUNT(character_id) FROM charactercreator_character_inventory"))

# save and commit
# curs.close()
# conn.commit()

# # On average, how many Items does each Character have?
# # On average, how many Weapons does each character have?
