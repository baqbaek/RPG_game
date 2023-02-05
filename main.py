from soldier import *
from map import *
from enemies import *

print('hi (About game)')
# selected_soldier = Soldier.choose_soldier(soldiers)
enemy_spawn(int(input('Number of enemies: ')))
player_spawn()
display_map()
move_player(input('Direction: '))

# selected_soldier.actions()
