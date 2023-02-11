class Enemy:
    def __init__(self, short, name, armor, hp, dmg):
        self.short = short
        self.name = name
        self.armor = armor
        self.hp = hp
        self.dmg = dmg

    def display_attributes(self):
        print("Short Name:", self.short)
        print("Name:", self.name)
        print("Armor:", self.armor)
        print("HP:", self.hp)
        print("Damage:", self.dmg)


enemies = [
    # short_name, name, armor, hp, dmg
    Enemy('D', 'Dragon', 10, 100, 10),
    Enemy('G', 'Goblin', 10, 10, 10),
    Enemy('O', 'Orc', 10, 10, 10),
    Enemy('S', 'Snake', 10, 10, 10),
    Enemy('T', "Troll", 8, 12, 8),
    Enemy('D', "Demon", 12, 8, 12),
    Enemy('S', "Succubus", 6, 14, 10),
    Enemy('Z', "Zombie", 4, 16, 6),
    Enemy('V', "Vampire", 10, 10, 12)
]
def show_enemies():
    print('Enemies: ')
    for i in enemies:
        i.display_attributes()
        print('---')