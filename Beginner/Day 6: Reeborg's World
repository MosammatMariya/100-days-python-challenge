#Reeborg's World
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
# Hurdle 1
def action():
    turn_left()
    turn_left()
    turn_left()
    
def run():
    move()
    turn_left()
    move()
    action()
    move()
    action()
    move()
    turn_left()
for step in range(6):
    run()

# Hurdle 2
def action():
    turn_left()
    turn_left()
    turn_left()
    
def run():
    move()
    turn_left()
    move()
    action()
    move()
    action()
    move()
    turn_left()

while not at_goal():
    run()
#Hurdle 3
def action():
    turn_left()
    turn_left()
    turn_left()
    
def run():
    turn_left()
    move()
    action()
    move()
    action()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        run()
    else:
        move()
# Hurdle 4
def action():
    turn_left()
    turn_left()
    turn_left()
    
def run():
    turn_left()
    while wall_on_right():
        move()
    action()
    move()
    action()
    while front_is_clear():
        move() 
    turn_left()

while not at_goal():
    if wall_in_front():
        run()
    else:
        move()
#maze
def action():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        action()
        move()
    elif front_is_clear():
        move() 
    else:
        turn_left()
