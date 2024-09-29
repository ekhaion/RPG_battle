from hero import Hero
from monster import Monster


class Stats:
    def __init__(self):
        self.sum_damages_hero = 0
        self.max_defenses_hero = 0
        self.sum_damages_monster = 0
        self.max_defenses_monster = 0

    def display_victory_and_stats(self, monster: Monster, hero: Hero):
        # victory condition
        if hero.health > 0:
            print(f"\n👨 {hero.name} has defeated {monster.name}!")
        else:
            print(f"\n👹 {monster.name} has defeated {hero.name}!")

        print(f"{monster.name} -> ⚔ : {self.sum_damages_monster}, max 🛡 : {self.max_defenses_monster}")
        print(f"{hero.name} -> ⚔ : {self.sum_damages_hero}, max 🛡 : {self.max_defenses_hero}")

    def increment_stats(self, attacker: Monster or Hero, damage: int, defense: int):
        # increment damages and store max defense if attacker is the hero or not
        if type(attacker) is Hero:
            self.sum_damages_hero += damage
            self.max_defenses_monster = max(defense, self.max_defenses_monster)
        else:
            self.sum_damages_monster += damage
            self.max_defenses_hero = max(defense, self.max_defenses_hero)
