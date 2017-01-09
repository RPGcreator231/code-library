# Ghost Game
from random import randint
print('Ghost Game')
feeling_brave  = True
score = 0
while feeling_brave:
    ghost_door = randint(1, 10)
    print('ten doors ahead...')
    print('two ghosts behind.')
    print('Which door do you open?')
    door = input('1 to 10')
    door_num = int(door)
    if door_num == ghost_door:
        print('GHOST!')
        feeling_brave = False
    else:
        print('no ghost!')
        print('You enter the next room')
        score = score +1
print('Run away!')
print('Game over! You scored', score)
