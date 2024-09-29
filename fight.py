import random

from hero import Hero
from monster import Monster
from statistic import Stats
from weapon import Weapon


class Fight:
    def __init__(self, hero: Hero, monster: Monster, weapon: Weapon, stats: Stats):
        self.hero = hero
        self.monster = monster
        self.stats = stats  # Store the passed Stats object
        self.weapon = weapon

    def fight(self):
        # randomize first attacker
        is_first = random.choice([True, False])
        while self.hero.health > 0 and self.monster.health > 0:
            if is_first:
                self.attack(self.hero, self.monster, self.weapon, self.stats)
            else:
                self.attack(self.monster, self.hero, self.weapon, self.stats)
            # switch between True or False for alternate attack between hero and monster
            is_first = not is_first

    @staticmethod
    def attack(attacker: Hero or Monster, target: Hero or Monster, weapon: Weapon, stats: Stats):
        # attacker and target alternate between hero and monster
        damage = attacker.strength + random.randint(-5, 5)
        defense = target.defense - random.randint(0, 5)
        # if hero add weapon damages
        if type(attacker) is Hero:
            damage += weapon.damage
        total_damage = damage - defense
        # prevent negative value
        if total_damage < 0:
            total_damage = 0

        # for statistics
        stats.increment_stats(attacker, damage, defense)

        target.health -= total_damage
        # print result of the weapon pass
        print(f"{attacker.name}: {total_damage} ⚔ -> {target.name}: {target.health} 🖤.")
