from turtle import Turtle ,Screen
import random

screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the game? Enter a color: ")
colors = ["red","blue","green","yellow","purple","pink"]
y_position = [-70,-40,-10,20,50,80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            win = turtle.pencolor()
            if win == user_bet:
                print(f"You won! {win} color won the game!")
            else:
                print(f"You lost! {win} color won the game!")

        distance = random.randint(0,10)
        turtle.speed("fastest")
        turtle.forward(distance)

screen.exitonclick()
