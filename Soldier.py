class Soldier():
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


soldiers = [Soldier('Lukas', 20, 100, 10),
            Soldier('Bartek', 20, 100, 10)
            ]
soldier_found = False
while soldier_found == False:
    for soldier in soldiers:
        if isinstance(soldier, Soldier):
            soldier.display_attributes()
            print('---')
    soldier_name = input('Who is your Soldier?')
    for soldier in soldiers:
        if soldier_name == soldier.name:
            print('Your soldier is', soldier.name)
            soldier_found = True
            break

    if not soldier_found:
        print(soldier_name, 'is not a valid soldier name')

while soldier.hp > 0:
    print('1. Leczenie 10\n2. Obrażenia 10')  # 1
    action = int(input("wybierz akcje: "))  # 2

    if action == 1:
        soldier.hp += 10
    elif action == 2:
        soldier.hp -= 10
    else:
        print('Wybrano złą opcje')

    if soldier.hp == 0:
        print('You are dead man')
    else:
        print('Aktualne zdrowie: ' + str(soldier.hp))
