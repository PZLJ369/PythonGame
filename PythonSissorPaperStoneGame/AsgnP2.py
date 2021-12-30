# Monster Game
import random

start_point = 10

win_game = 0

num = 0

while start_point > 0:

    computer_move = str(random.randint(0, 2))

    loss: int = 0
    win: int = 0
    draw: int = 0

    print("You have", start_point, "points.")

    play_point = int(input("Enter the number of points to be used for next game(-1 to end the game): "))

    if 0 < play_point <= start_point:

        for x in range(3):
            if start_point > 0:
                # game
                player_move1 = input("Enter 0(fire), 1(grass) or 2(water) or V(Void):")

                computer_move = str(random.randint(0, 2))

                if player_move1 == 'v' or player_move1 == 'V' or player_move1 == 'void':
                    print("Your game is void.")
                    print("")
                    # Monster Game
                    import random

                    start_point = start_point

                    while start_point > 0:

                        computer_move = random.randint(0, 2)

                        loss: int = 0
                        win: int = 0
                        draw: int = 0

                        print("You have", start_point, "points.")

                        play_point = int(input("Enter the number of points to be used for next game(-1 to end the game): "))

                        if 0 < play_point <= start_point:

                            for y in range(3):

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
                                start_point = start_point + play_point
                                print("You won the game with", play_point, "points added.")
                                win_game = win_game + 1
                                print("")
                            elif loss >= 2:
                                start_point = start_point - play_point
                                print("You lost the game with", play_point, "points deducted.")
                                print("")
                                if start_point == 0:
                                    print("You have no more points, End of Game!")
                                    print("")

                                    print("you have", win_game, "wins.")

                                    text_file = open("write.txt", "a")

                                    # puts in the values in the file
                                    import datetime
                                    d = datetime.datetime.now()

                                    def write_in_file():
                                        global text_file
                                        text_file.write("Name:" + str(Name))
                                        text_file.write("\n")
                                        text_file.write("Wins:" + str(Wins))
                                        text_file.write("\n")
                                        text_file.write("Dates:" + str(d.strftime("%x")))
                                        text_file.write("\n")
                                        text_file.write("\n")
                                        text_file.close()
                                        text_file = open("write.txt", "a")

                                    # highest value in a file

                                    Name = input("Name:")
                                    Wins = win_game
                                    write_in_file()
                                    print("Thanks", Name, ", your scores have saved!")
                                    print("For more details please visit write.txt!")
                                    print(d.strftime("%x"))
                                    print(d.strftime("%X"))

                                    print("")
                                    print("")
                                    print("All players and scores: ")
                                    f = open("write.txt", "r")
                                    print(f.read())

                                    break
                            else:
                                print("Tie! Your points remain unchanged.")
                                print("")

                        elif play_point == -1:
                            print("")
                            print("End of Game!")
                            break

                        else:
                            print("You do not have enough points.")
                            print("")

                # Draw
                elif player_move1 == computer_move:
                    print("draw!")
                    if player_move1 == computer_move:
                        draw += 1
                    else:
                        draw = 0
                    computer_move = str(random.randint(0, 2))

                # Win
                elif player_move1 == '0' and computer_move == '1':
                    print("You are fire and computer is grass, you won!")
                    if player_move1 == '0' and computer_move == '1':
                        win += 1
                    else:
                        win = 0
                    computer_move = str(random.randint(0, 2))
                elif player_move1 == '1' and computer_move == '2':
                    print("You are grass and computer is water, you won!")
                    if player_move1 == '1' and computer_move == '2':
                        win += 1
                    else:
                        win = 0
                    computer_move = str(random.randint(0, 2))
                elif player_move1 == '2' and computer_move == '0':
                    print("You are water and computer is fire, you won!")
                    if player_move1 == '2' and computer_move == '0':
                        win += 1
                    else:
                        win = 0
                    computer_move = str(random.randint(0, 2))

                # loss
                elif player_move1 == '1' and computer_move == '0':
                    print("You are grass and computer is fire, you lost!")
                    if player_move1 == '1' and computer_move == '0':
                        loss += 1
                    else:
                        loss = 0
                    computer_move = str(random.randint(0, 2))
                elif player_move1 == '2' and computer_move == '1':
                    print("You are water and computer is grass, you lost!")
                    if player_move1 == '2' and computer_move == '1':
                        loss += 1
                    else:
                        loss = 0
                    computer_move = str(random.randint(0, 2))
                elif player_move1 == '0' and computer_move == '2':
                    print("You are fire and computer is water, you lost!")
                    if player_move1 == '0' and computer_move == '2':
                        loss += 1
                    else:
                        loss = 0
                    computer_move = str(random.randint(0, 2))
                else:
                    print("You entered an invalid option, you lost!")
                    loss += 1

        if start_point == 0:
            break
        else:
            print("You have", win, "win,", loss, "loss and", draw, "draw")

            if win >= 2:
                start_point = start_point + play_point
                print("You won the game with", play_point, "points added.")
                win_game += 1
                print("")
            elif loss >= 2:
                start_point = start_point - play_point
                print("You lost the game with", play_point, "points deducted.")
                print("")
                if start_point == 0:
                    print("You have no more points, End of Game!")
                    print("")

                    print("you have", win_game, "wins.")

                    text_file = open("write.txt", "a")

                    # puts in the values in the file
                    import datetime
                    d = datetime.datetime.now()

                    def write_in_file():
                        global text_file
                        text_file.write("Name:" + str(Name))
                        text_file.write("\n")
                        text_file.write("Wins:" + str(Wins))
                        text_file.write("\n")
                        text_file.write("Dates:" + str(d.strftime("%x")))
                        text_file.write("\n")
                        text_file.write("\n")
                        text_file.close()
                        text_file = open("write.txt", "a")

                    # highest value in a file

                    Name = input("Name:")
                    Wins = win_game
                    write_in_file()
                    print("Thanks", Name, ", your scores have saved!")
                    print("For more details please visit write.txt!")
                    print(d.strftime("%x"))
                    print(d.strftime("%X"))

                    print("")
                    print("")
                    print("All players and scores: ")
                    f = open("write.txt", "r")
                    print(f.read())

                    break
            else:
                print("Tie! Your points remain unchanged.")
                print("")

    elif play_point == -1:
        print("")
        print("End of Game!")
        break

    else:
        print("You do not have enough points.")
        print("")
