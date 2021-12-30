# Monster Game
import random

computer_move = random.randint(0, 2)

loss: int = 0
win: int = 0
draw: int = 0

for x in range(3):

    # game
    player_move = int(input("Enter 0(fire), 1(grass) or 2(water):"))

    computer_move = random.randint(0, 2)

    # Draw
    if player_move == computer_move:
        print("draw!")
        if player_move == computer_move:
            draw += 1
        else:
            draw = 0
        computer_move = random.randint(0, 2)

    # Win
    elif player_move == 0 and computer_move == 1:
        print("You are fire and computer is grass, you won!")
        if player_move == 0 and computer_move == 1:
            win += 1
        else:
            win = 0
        computer_move = random.randint(0, 2)
    elif player_move == 1 and computer_move == 2:
        print("You are grass and computer is water, you won!")
        if player_move == 1 and computer_move == 2:
            win += 1
        else:
            win = 0
        computer_move = random.randint(0, 2)
    elif player_move == 2 and computer_move == 0:
        print("You are water and computer is fire, you won!")
        if player_move == 2 and computer_move == 0:
            win += 1
        else:
            win = 0
        computer_move = random.randint(0, 2)

    # loss
    elif player_move == 1 and computer_move == 0:
        print("You are grass and computer is fire, you lost!")
        if player_move == 1 and computer_move == 0:
            loss += 1
        else:
            loss = 0
        computer_move = random.randint(0, 2)
    elif player_move == 2 and computer_move == 1:
        print("You are water and computer is grass, you lost!")
        if player_move == 2 and computer_move == 1:
            loss += 1
        else:
            loss = 0
        computer_move = random.randint(0, 2)
    elif player_move == 0 and computer_move == 2:
        print("You are fire and computer is water, you lost!")
        if player_move == 0 and computer_move == 2:
            loss += 1
        else:
            loss = 0
        computer_move = random.randint(0, 2)
    else:
        print("You entered an invalid option, you lost!")
        loss += 1

print("You have", win, "win,", loss, "loss and", draw, "draw")

if win >= 2:
    print("You won the game.")
elif loss >= 2:
    print("You lost the game.")
else:
    print("Tie!")
