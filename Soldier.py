class Soldier:
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


soldiers = [
    Soldier('Bartek', 15, 80, 25),
    Soldier('Lukas', 30, 150, 10),
    Soldier('John', 20, 100, 15),
    Soldier('Mario', 20, 90, 20),


]

soldier_found = False
while not soldier_found:
    for soldier in soldiers:
        if isinstance(soldier, Soldier):
            soldier.display_attributes()
            print("---")

    soldier_name = input("Who is your soldier? ")

    for soldier in soldiers:
        if soldier_name == soldier.name:
            print("Your soldier is", soldier.name)
            soldier_found = True
            break

    if not soldier_found:
        print(soldier_name, "is not a valid soldier name")

while soldier.hp > 0:
    print("1. Healing \n2. Damage " + str(soldier.dmg))
    action = int(input("Choose an action: "))

    if action == 1:
        soldier.hp += 10
    elif action == 2:
        soldier.hp -= soldier.dmg
    else:
        print("Invalid option selected")

    if soldier.hp <= 0:
        print("You are a dead man")
    else:
        print("Current health:", soldier.hp)
