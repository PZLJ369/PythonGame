# Monster Game
import random

computer_move = random.randint(0, 2)

# game
player_move = int(input("Enter 0(fire), 1(grass) or 2(water):"))

# Draw
if player_move == computer_move:
    print("draw!")
    print("")

# Win
elif player_move == 0 and computer_move == 1:
    print("You are fire and computer is grass, you won!")
    print("")

elif player_move == 1 and computer_move == 2:
    print("You are grass and computer is water, you won!")
    print("")

elif player_move == 2 and computer_move == 0:
    print("You are water and computer is fire, you won!")
    print("")

# loss
elif player_move == 1 and computer_move == 0:
    print("You are grass and computer is fire, you lost!")
    print("")

elif player_move == 2 and computer_move == 1:
    print("You are water and computer is grass, you lost!")
    print("")

elif player_move == 0 and computer_move == 2:
    print("You are fire and computer is water, you lost!")
    print("")

else:
    print("You entered an invalid option, you lost!")
    print("")
