

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json


def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()     
    if wall_in_front():
        if right_is_clear():
            turn_right()
            move()        
        else:
            turn_left()
            if wall_in_front():
                turn_left()
                move()
    else:
        move()
                    