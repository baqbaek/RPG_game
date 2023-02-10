from enemies import *


class Soldier:
    def __init__(self, type, name, armor, hp, dmg):
        self.type = type
        self.name = name
        self.armor = armor
        self.hp = hp
        self.dmg = dmg

    def display_attributes(self):
        print("Class:", self.type)
        print("Name:", self.name)
        print("Armor:", self.armor)
        print("HP:", self.hp)
        print("Damage:", self.dmg)

    @staticmethod
    def choose_soldier():
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
                    return soldier

            if not soldier_found:
                print(soldier_name, "is not a valid soldier name")

    def actions(self):
        while self.hp > 0:
            print("1. Healing \n2. Attack")
            action = int(input("Choose an action: "))

            if action == 1:
                self.hp += 10
            elif action == 2:
                print("Enemies: ")
                for i in range(len(enemies)):
                    print(i + 1, ". ", enemies[i].name)

                enemy_choice = int(input("Enter the number of the enemy: ")) - 1
                selected_enemy = enemies[enemy_choice]
                selected_enemy.hp -= self.dmg
                print(selected_enemy.name, "has been hit and lost", self.dmg, "HP.")
                if selected_enemy.hp > 0:
                    self.hp -= selected_enemy.dmg
                    print("Enemy has attacked back, you lost", selected_enemy.dmg, "HP.")
                else:
                    enemies.remove(selected_enemy)
                    print(selected_enemy.name, "has been defeated.")
            else:
                print("Invalid option selected")

            if self.hp <= 0:
                print("You are a dead man")
                break
            else:
                print("Current health:", self.hp)
                print("Enemies left: ", len(enemies))
                if not enemies:
                    print("You have defeated all enemies!")
                    break


soldiers = [
    Soldier('Archer', 'Bartek', 15, 80, 25),
    Soldier('Tank', 'Lukas', 30, 150, 10),
    Soldier('Healer', 'John', 20, 100, 15),
    Soldier('Barbarian', 'Mario', 20, 90, 20),
]
selected_soldier = Soldier.choose_soldier()
Soldier.actions(selected_soldier)
