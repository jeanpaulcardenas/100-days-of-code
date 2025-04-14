from turtle import Turtle, Screen
import time
from random import randint

# crear snake con una longitud concreta y sus comandos de movimiento

# crear comida


# eliminar comida cuando snake se encuentre con ella y aumentar tamaño de snake

# craer limites del mapa

# condiciones de "lose" (snake con snake y snake con pared)

def snake_game():

    def create_point():
        aux = Turtle(shape='square',visible=False)
        aux.shapesize(stretch_wid=0.5, stretch_len=0.5)
        aux.up()
        aux.color("white")
        aux.speed(0)
        return aux

    def turn_right():
        if head.heading() != 180:
            head.seth(0)

    def turn_up():
        if head.heading() != 270:
            head.seth(90)

    def turn_left():
        if head.heading() != 0:
            head.seth(180)

    def turn_down():
        if head.heading() != 90:
            head.seth(270)

    def move_food(point: Turtle):
        point.goto(10 * randint(-15, 15), 10 * randint(-15, 15))

    def create_screen():
        screen = Screen()
        screen.bgcolor("black")
        screen.setup(1200, 600)
        screen.screensize(1200, 600)
        screen.listen()
        screen.onkeypress(turn_right, 'd')
        screen.onkeypress(turn_left, 'a')
        screen.onkeypress(turn_down, 's')
        screen.onkeypress(turn_up, 'w')
        return screen

    screen = create_screen()
    not_loss = True
    eaten = 0
    head = create_point()
    head.showturtle()
    head.goto(0, 0)

    food = create_point()
    food.showturtle()
    move_food(food)
    print(food.pos())
    segments = [head]
    while not_loss:

        if eaten > 0:
            for i in range(eaten, 0, -1):
                segments[i].goto(segments[i - 1].pos())
        head.forward(10)
        x_pos =head.pos()[0]
        y_pos = head.pos()[1]
        if abs(y_pos) > 150:
            head.goto(head.pos()[0], -abs(y_pos)*150/y_pos)
        if abs(x_pos) > 150:
            head.goto(-abs(x_pos)*150/x_pos, head.pos()[1])
        time.sleep(0.1)
        if head.pos() in [seg.pos() for seg in segments[1:]]:
            screen.bye()
        if round(head.pos()[0]) == round(food.pos()[0]) and round(head.pos()[1]) == round(food.pos()[1]):
            eaten += 1
            new_segment = create_point()
            new_segment.goto(head.pos())
            new_segment.showturtle()
            segments.append(new_segment)
            move_food(food)


snake_game()
