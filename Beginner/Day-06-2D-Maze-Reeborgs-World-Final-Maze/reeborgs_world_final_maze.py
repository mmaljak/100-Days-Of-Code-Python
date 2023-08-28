def turn_right():
    for turn in range(3):
        turn_left()

def face_north():
    while not is_facing_north():
        turn_left()

face_north()
while not at_goal():
    if front_is_clear():
        move()
        if right_is_clear():
            turn_right()
    elif right_is_clear():
        turn_right()
    else:
        turn_left()