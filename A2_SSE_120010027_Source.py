from turtle import Turtle, Screen
from random import randrange
import time
Key_Up, Key_Down, Key_Left, Key_Right, Key_Stop = 'Up', 'Down', 'Left', 'Right', 'space'
g_snake = None
g_screen = None
g_monster = None
g_snake_length = 4
g_snake_stamp_id = []
g_snake_body = []
g_snake_speed = 20
g_food = []
delay = 0.15
number_food = 9

# define the screen


def set_screen(w=660, h=660):
    s = Screen()
    s.setup(w, h)
    s.title('Snake')
    s.tracer(0)
    return s

# define the function for make turtle more convenient


def set_turtle(shape='square', color='red', x=0, y=0):
    t = Turtle(shape)
    t.up()
    t.color(color)
    t.goto(x, y)
    t.direction = 'paused'
    return t

# control the snake to forward and leave stamp according to the snake_length


def create_stamp():
    global g_snake_speed
    global delay
    delay = 0.15
    if g_snake.direction != 'paused':                     # if the direction is not stop, let it move
        g_snake_speed = 20
        # record the body position in a dynamic list, for count contacts use
        g_snake_body.append(g_snake.position())
        # set the stamp color to be black with blue frame for better view
        g_snake.color('blue', 'black')
        # record the every id of stamp in the dynamic list for further deleting stamp
        id = g_snake.stamp()
        g_snake_stamp_id.append(id)
        # after making stamp, change the color to red(meaning head)
        g_snake.color('red')
        # g_snake.forward(g_snake_speed)
        if len(g_snake_stamp_id) == g_snake_length:     # if the list is full
            # clear the very first stamp
            g_snake.clearstamp(g_snake_stamp_id[0])
            # delete the first stamp id in the list for storing more stamp id
            g_snake_stamp_id.pop(0)
            g_snake_body.pop(0)                         # same as above
        # if the length changed
        elif g_snake_length > 4 and len(g_snake_stamp_id) != g_snake_length:
            delay += 0.05                          # slow down a little bit

            # g_snake.forward(g_snake_speed)              #forward (g_snake_speed) pixels

        g_snake.forward(g_snake_speed)

# change direction of the snake


def snake_up():
    if g_snake.direction != 'down':
        g_snake.setheading(90)
        g_snake.direction = 'up'


def snake_down():
    if g_snake.direction != 'up':
        g_snake.setheading(270)
        g_snake.direction = 'down'


def snake_left():
    if g_snake.direction != 'right':
        g_snake.setheading(180)
        g_snake.direction = 'left'


def snake_right():
    if g_snake.direction != 'left':
        g_snake.setheading(0)
        g_snake.direction = 'right'

# call the snake to stop


def snake_stop():
    g_snake.direction = 'paused'

# listen user's keyboard, let user depend how it turns


def user_inputKey():
    g_screen.listen()
    g_screen.onkey(snake_up, Key_Up)
    g_screen.onkey(snake_right, Key_Right)
    g_screen.onkey(snake_down, Key_Down)
    g_screen.onkey(snake_left, Key_Left)
    g_screen.onkey(snake_stop, Key_Stop)

# call the snake to move


def snake_move():
    user_inputKey()                     # take user's press as direction
    create_stamp()                      # every loop forward 20 pixels
    g_screen.update()                   # update the screen

# call the monster to move


def monster_move():
    # get the angle between the line that connect the monster and the snake and the x-axis
    ang = g_monster.towards(g_snake)
    if ang >= 315 or ang <= 45:         # if the angle is in this range, let monster moves right. The following follows the same logic
        g_monster.setheading(0)
    elif ang > 45 and ang <= 135:
        g_monster.setheading(90)
    elif ang > 135 and ang <= 225:
        g_monster.setheading(180)
    else:
        g_monster.setheading(270)
    # the monster's speed is random, but litter slower than the snake
    g_monster.forward(10)
    g_screen.update()                   # call the screen to update
    g_screen.ontimer(monster_move, randrange(50, 150))

# set a food list to randomly create (number_food) food items


def food_list(number_food):
    for i in range(number_food):
        fe = []
        # in this range and (*20) will make sure that the snake can exactly eat them
        fe.append(randrange(-12, 12)*20)
        fe.append(randrange(-12, 12)*20)
        # change fe into tuple, because the turtle coordinate is store in tuples
        fe = tuple(fe)
        g_food.append(fe)               # append them into our food list

    for i in range(number_food):        # check if there are some items overlapping each other
        for j in range(i+1, number_food):
            if abs(g_food[i][0] - g_food[j][0]) < 19 and abs(g_food[i][1] - g_food[j][1]) < 19:
                # if yes, set an anthor random food list again
                food_list(number_food)
            else:
                return g_food

# set the boarder for the snake to move


def boarder(w=500, h=500):
    w = Turtle()
    w.hideturtle()
    w.up()
    w.goto(-250, -250)
    w.down()
    for i in range(4):
        w.forward(500)
        w.left(90)
    w.up()
    w.goto(-250, 250)
    w.down()
    w.setheading(90)
    w.forward(80)
    w.right(90)
    w.forward(500)
    w.right(90)
    w.forward(80)

# display the food items in the screen


def create_food(xcor, ycor, num):
    food = Turtle()
    food.up()
    food.hideturtle()
    # go to certain coordinate which is just in the square
    food.goto(xcor-4, ycor-10)
    food.write('%d' % (num), font=('Arial', 14, 'normal'))
    return food

# the main function


def main(x, y):
    wo.undo()                             # clear the sentence in the mid of the screen
    contact = 0
    t = 0
    global g_snake_length
    global g_snake_stamp_id
    global g_snake_body
    global g_snake_speed
    global g_food
    global delay
    global number_food
    # set food items and display it on the screen, set the first item in food list to have the value of 1
    food_1 = create_food(g_food[0][0], g_food[0][1], 1)
    food_2 = create_food(g_food[1][0], g_food[1][1], 2)
    food_3 = create_food(g_food[2][0], g_food[2][1], 3)
    food_4 = create_food(g_food[3][0], g_food[3][1], 4)
    food_5 = create_food(g_food[4][0], g_food[4][1], 5)
    food_6 = create_food(g_food[5][0], g_food[5][1], 6)
    food_7 = create_food(g_food[6][0], g_food[6][1], 7)
    food_8 = create_food(g_food[7][0], g_food[7][1], 8)
    food_9 = create_food(g_food[8][0], g_food[8][1], 9)
    monster_move()                                          # call the monster to move
    while True:                                                 # the main loop which controls the program
        # if the monster touches the snake, end the program and print lose prompt
        if g_monster.distance(g_snake) < 19:
            pen.goto(0, 0)
            pen.color('purple')
            pen.write('YOU LOSE!!!', align='center',
                      font=('Arial', 20, 'normal'))
            return

        # if the snake touches the boarder set the direction to stop in order to stop the snake
        if g_snake.xcor() > 230 and g_snake.direction == 'right':
            g_snake.direction = 'paused'
        elif g_snake.xcor() < -230 and g_snake.direction == 'left':  # same as above
            g_snake.direction = 'paused'
        elif g_snake.ycor() < -230 and g_snake.direction == 'down':
            g_snake.direction = 'paused'
        elif g_snake.ycor() > 230 and g_snake.direction == 'up':
            g_snake.direction = 'paused'

        # check if any food has been eat
        for i in range(len(g_food)):
            # if there is nothing in that position in food list, go to next position
            if g_food[i] == None:
                continue
            # if the snake reaches the food
            if g_snake.distance(g_food[i]) < 19:
                # change this position to None, meaning it has been eaten
                g_food[i] = None
                g_screen.update()
                # the length will increase respectively
                g_snake_length += i+1

        for i in g_snake_body:                                  # count contact betwwen monster and the snake boby
            if g_monster.distance(i) < 19:
                contact += 1
                break

        # if the ith position is None, move the corresponding turtle out of screen and clear the number
        for i in range(len(g_food)):
            if g_food[i] == None:
                if i == 0:
                    food_1.goto(300, 300)
                    food_1.clear()
                if i == 1:
                    food_2.goto(300, 300)
                    food_2.clear()
                if i == 2:
                    food_3.goto(300, 300)
                    food_3.clear()
                if i == 3:
                    food_4.goto(300, 300)
                    food_4.clear()
                if i == 4:
                    food_5.goto(300, 300)
                    food_5.clear()
                if i == 5:
                    food_6.goto(300, 300)
                    food_6.clear()
                if i == 6:
                    food_7.goto(300, 300)
                    food_7.clear()
                if i == 7:
                    food_8.goto(300, 300)
                    food_8.clear()
                if i == 8:
                    food_9.goto(300, 300)
                    food_9.clear()

        # call the snake to move every loop
        snake_move()
        # refresh the timer shown on the top
        word.clear()

        # %d makes sure that all the numbers are digit, it displays the time the monster touches the snake and the total time consumes during the game and the current direction
        word.write('Contact:%d    Time:%d    Direction:  %s     ' % (
            contact, t, g_snake.direction), align='center', font=('Arial', 14, 'normal'))

        # every loop plus delay, because the loop run every (delay) seconds
        t += delay
        # every (delay) seconds compete the loop
        time.sleep(delay)
        # if all items in the food list become None, meaning no food left, end the game and print you win
        if g_food.count(None) == number_food:
            pen.color('orange')
            pen.write('CONGRATS! YOU WIN!!!', align='center',
                      font=('Arial', 20, 'normal'))
            return

    g_screen.mainloop()


# set a screen for play
g_screen = set_screen()
# define the snake head
g_snake = set_turtle()
g_monster = set_turtle(color='purple', x=-200, y=-
                       200)            # define a monster
# set a turtle for display introduction
word = Turtle()
word.hideturtle()
word.up()
word.goto(0, 270)
word.write('Contact:0    Time:0    Direction:paused',
           align='center', font=('Arial', 14, 'normal'))
wo = Turtle()
wo.hideturtle()
wo.up()
wo.goto(0, 100)
wo.write('''
Welcome to the snake game, use arrow keys to decide the direction of the snake
There will be a monster chasing you, try to avoid it!!!
You will win after consuming all the food which are indicated as numbers
You may click anywhere to start
Good luck!!!!
''', align='center', font=('Arial', 10, 'normal'))
boarder()
pen = Turtle()
pen.up()
pen.hideturtle()
food_list(number_food)
g_screen.update()
# click to run main function
g_screen.onscreenclick(main)
g_screen.mainloop()
