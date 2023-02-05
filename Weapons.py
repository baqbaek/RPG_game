class Weapon:
    def __init__(self, id, name, dmg):
        self.id = id
        self.name = name
        self.dmg = dmg

    def display_weapons(self):
        print('Name: ', self.name)
        print('Damage: ', self.dmg)


weapons = [
    Weapon(1, 'Sword', 7),
    Weapon(2, 'Bow', 8),
    Weapon(3, 'Dagger', 5),
    Weapon(4, 'Long-sword', 10),
    Weapon(5, 'Axe', 12),
    Weapon(6, 'Spear', 9),
    Weapon(7, 'Mace', 11),
    Weapon(8, 'Crossbow', 10),
    Weapon(9, 'Halberd', 13),
    Weapon(10, 'Whip', 6)
]


def show_weapons():
    print('Weapons: ')
    for i in weapons:
        i.display_weapons()
        print('---')

# show_weapons()


