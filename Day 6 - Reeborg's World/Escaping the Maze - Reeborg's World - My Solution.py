def turn_right():
    for i in range(0,3):
        turn_left()
    
while True: 
    if at_goal():
        break
    elif wall_on_right() and front_is_clear():
        move()
    elif wall_on_right() and not front_is_clear():
        turn_left()
    elif not wall_on_right():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
    
    
    
    
    


