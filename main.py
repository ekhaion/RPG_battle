from monster import Monster
from hero import Hero
from fight import Fight
from weapon import Weapon
from statistic import Stats

# weapon1 = Weapon()  # Random name and damage
weapon2 = Weapon("Excalibur", 100)  # Specified name and damage
#
# print(weapon1)
# print(weapon2)
#
# monster1 = Monster()  # Random name, health, strength, and defense
monster2 = Monster("Dire Wolf", 150, 25, 10)  # Specified attributes
#
# hero1 = Hero()  # Random name, health, strength, defense, and weapon
hero2 = Hero("Valkyrie", 200, 40, 15, Weapon("Enchanted Sword", 50))

stats2 = Stats()
print(hero2)
print(monster2, "\n")

fight = Fight(hero2, monster2, weapon2, stats2)
fight.fight()
stats2.display_victory_and_stats(monster2, hero2)

hero_fight = Hero()
monster_fight = Monster()
weapon3 = Weapon()

stats = Stats()
print(hero_fight)
print(monster_fight, "\n")


fight = Fight(hero_fight, monster_fight, weapon3, stats)
fight.fight()
stats.display_victory_and_stats(monster_fight, hero_fight)
