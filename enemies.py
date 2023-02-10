class Enemy:
    def __init__(self, name, armor, hp, dmg):
        self.name = name
        self.armor = armor
        self.hp = hp
        self.dmg = dmg

    def display_attributes(self):
        print("Name:", self.name)
        print("Armor:", self.armor)
        print("HP:", self.hp)
        print("Damage:", self.dmg)


enemies = [
    # name, armor, hp, dmg
    Enemy('Dragon', 10, 100, 10),
    Enemy('Goblin', 10, 10, 10),
    Enemy('Orc', 10, 10, 10),
    Enemy('Snake', 10, 10, 10),
    Enemy("Troll", 8, 12, 8),
    Enemy("Demon", 12, 8, 12),
    Enemy("Succubus", 6, 14, 10),
    Enemy("Zombie", 4, 16, 6),
    Enemy("Vampire", 10, 10, 12)
]
def show_enemies():
    print('Enemies: ')
    for i in enemies:
        i.display_attributes()
        print('---')