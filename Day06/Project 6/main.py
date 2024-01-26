def turn_right():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():  # this while loop is to move the reeborg to move to the nearest wall so that he doesn't get stuck in an infinite loop where he has the right side clear in all 4 direction(This happens when he is in the middle of the maze)
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
