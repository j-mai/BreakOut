#program to re-create Atari breakout game
#Jasmine Mai, October 10, 2017

from cs1lib import *
from random import *
from Brick import Brick
from Ball import Ball
from Paddle import Paddle

PADDLE_LENGTH = 70
PADDLE_HEIGHT = 20
paddle_X = 180
paddle_Y = 380
paddle_vx = 5
paddle_move_right = False
paddle_move_left = False


blocks_list = []
BLOCK_ROWS = 5
BLOCK_COLUMNS = 5
BLOCK_LENGTH = 400/BLOCK_COLUMNS
BLOCK_WIDTH = 200/BLOCK_ROWS

BALL_RADIUS = 5
BALL_STARTING_X = ((2 * paddle_X) + PADDLE_LENGTH ) // 2
BALL_STARTING_Y = paddle_Y - BALL_RADIUS - 1
ball_starting_vx = None
ball_starting_vy = -4
ACCELERATION = 2

new_game = True
game_over = False
game_start = False
game_won = False

lives_left = 3
score = 0

WINDOW_X = 400
WINDOW_Y = 400

PADDLE_MOVE_RIGHT = "m"
PADDLE_MOVE_LEFT = "x"
RESTART = "n"
START_GAME = " "

MIN_SPEED = 3
MAX_SPEED = 15
MAX_START_SPEED = 6


#key_pressed function passed into key_press call back
#defines keys that control the game, setting global booleans
def key_pressed(key):
    global new_game, paddle_move_right, paddle_move_left, game_start, lives_left
    if (key == RESTART):
        new_game = True

    if (key == PADDLE_MOVE_RIGHT):
        paddle_move_right = True

    if(key == PADDLE_MOVE_LEFT):
        paddle_move_left = True

    if (key == START_GAME and not game_start and not game_won and not game_over):
        if (not new_game):
             ball.set_velocityY(ball_starting_vy)
             ball.set_velocityX(randomize(-1 * MAX_START_SPEED, MAX_START_SPEED, -1 * MIN_SPEED, MIN_SPEED))
        lives_left -= 1
        game_start = True

#defines what happens when control keys are released, setting global booleans
def key_release(key):
    global new_game, paddle_move_right, paddle_move_left

    if (key == PADDLE_MOVE_RIGHT):
        paddle_move_right = False

    if(key == PADDLE_MOVE_LEFT):
        paddle_move_left = False

#keep track if number of lives left is decreased, when ball hits the lower edge of the window
def lives_lost():
    global game_over, lives_left, game_start, game_won

    #decrease number of lives if ball passes lower edge of the screen
    if (ball.get_y() - ball.get_radius() > WINDOW_Y):
        if lives_left > 0:
            ball.set_x(((paddle.get_x() + paddle.get_length()) + paddle.get_x()) // 2)
            ball.set_y(BALL_STARTING_Y)
            game_start = False
            print (lives_left)
        elif (lives_left == 0):
            game_over = True
            game_won = False
            game_start = False

#for creating random x velocity
def randomize (a, b, lower_bound, upper_bound):
    r = randint(a, b)
    if (r > lower_bound and r < upper_bound):
        randomize(a, b, lower_bound, upper_bound)

    return r

#reset game function
def start_game(rows, columns) :
    global ball, blocks_list, starting_vy, ball_starting_vx, paddle, game_start, lives_left, game_over, score, game_won

    blocks_list = [] #clear list of blocks


    ball_starting_vx = randomize(-1 * MAX_START_SPEED, MAX_START_SPEED, -1 * MIN_SPEED, MIN_SPEED) #create random initial x-direction for ball

    #draw number of blocks specified
    for i in range(columns):
        for j in range(rows):
            #randomize colors
            r = uniform(0, 1)
            g = uniform (0, 1)
            b = uniform (0, 1)

            brick = Brick(i * BLOCK_LENGTH, j * BLOCK_WIDTH, r, g, b, BLOCK_LENGTH, BLOCK_WIDTH)
            blocks_list.append(brick) #add the block to the list

    #create ball and paddle
    ball = Ball(BALL_STARTING_X, BALL_STARTING_Y, BALL_RADIUS, uniform(0, 1), uniform(0, 1), uniform(0, 1),
                ball_starting_vx, ball_starting_vy)

    paddle = Paddle(paddle_X, paddle_Y, uniform(0, 1), uniform(0, 1), uniform(0, 1), PADDLE_LENGTH,
                    PADDLE_HEIGHT, paddle_vx)

    game_start = False
    game_over = False
    game_won = False
    score = 0
    lives_left = 3

#change ball's velocity depending on collision with anything
def collision(list):
    global score

    #if collide with paddle, make ball x-velocity dependent on distance of collision from the center of paddle

    #if collide with left side of paddle, ball velocity is negative
    if (paddle.collision_left(ball.get_x() - ball.get_radius(), ball.get_x() + ball.get_radius(),
                         ball.get_y() + ball.get_radius())):

        ball.set_velocityY((-1) * ball.get_velocityY())
        ball.set_y(ball.get_y() - ball.get_radius())

        from_center = (paddle.calculate_collision_left(ball.get_x() + ball.get_radius())) / (paddle.get_length() // 8)

        ball.set_x(ball.get_x() - ball.radius)

        #prevent ball from getting too fast or too slow
        if (ball.get_velocityX() < 0):
            if (ball.get_velocityX() * from_center > -1 * MIN_SPEED):
                # ball.set_velocityX(ball.get_velocityX() * from_center - 1)
                ball.set_velocityX(-1 * MIN_SPEED)
            elif (ball.get_velocityX() * from_center < -1 * MAX_SPEED):
                ball.set_velocityX(-1 * MAX_START_SPEED)
            else:
                ball.set_velocityX(ball.get_velocityX() * from_center)

        else:
            if (ball.get_velocityX() * from_center < MIN_SPEED):
                # ball.set_velocityX((-1) * ball.get_velocityX() * from_center - 1)
                ball.set_velocityX(-1 * MIN_SPEED)
            elif (ball.get_velocityX() * from_center > MAX_SPEED):
                ball.set_velocityX(-1 * MAX_START_SPEED)
            else:
                ball.set_velocityX((-1) * ball.get_velocityX() * from_center)

        #accelerate in direction of paddle if moving left and ball is moving left
        if (paddle_move_left):
            ball.set_velocityX(ball.get_velocityX() - ACCELERATION)

    #if ball collides with paddle on the right side, ball velocity is postive
    elif (paddle.collision_right(ball.get_x() - ball.get_radius(), ball.get_x() + ball.get_radius(),
                         ball.get_y() + ball.get_radius())):

        ball.set_velocityY((-1) * ball.get_velocityY())
        ball.set_y(ball.get_y() - ball.get_radius())

        from_center = paddle.calculate_collision_right(ball.get_x() - ball.get_radius()) / (paddle.get_length() // 8)

        ball.set_x(ball.get_x() + ball.radius)

        #prevent ball from getting too fast or too slow
        if (ball.get_velocityX() < 0):
            if (ball.get_velocityX() * from_center > -1 * MIN_SPEED):
                ball.set_velocityX(MIN_SPEED)
            elif (ball.get_velocityX() * from_center < -1 * MAX_SPEED):
                ball.set_velocityX(MAX_START_SPEED)
            else:
                ball.set_velocityX((-1) * ball.get_velocityX() * from_center)

        else:
            if (ball.get_velocityX() * from_center < MIN_SPEED):
                ball.set_velocityX(MIN_SPEED)
            elif (ball.get_velocityX() * from_center > MAX_SPEED):
                ball.set_velocityX(MAX_START_SPEED)
            else:
                ball.set_velocityX(ball.get_velocityX() * from_center)

        if (paddle_move_right):
            ball.set_velocityX(ball.get_velocityX() + ACCELERATION)

    #if ball hits sides of window, reverse x-velocity
    if (ball.get_x() + ball.get_radius() > WINDOW_X or ball.get_x() - ball.get_radius() <= 0):
        ball.set_velocityX((-1) * ball.get_velocityX())
        if (ball.get_velocityX() < 0):
            ball.set_x(ball.get_x() - ball.get_radius())
        else:
            ball.set_x(ball.get_x() + ball.get_radius())

    #if ball hits top of window
    if (ball.get_y() - ball.get_radius() <= 0):
        ball.set_velocityY((-1) * ball.get_velocityY())

    #check if ball has collided with any blocks
    for i in range(len(list)):
        collided = None

        if (list[i].collide_vertical(ball.get_x()-ball.get_radius(), ball.get_y() - ball.get_radius(),
                                   ball.get_x() + ball.get_radius(), ball.get_y() + ball.get_radius())):
            ball.set_velocityX((-1) * ball.get_velocityX())
            collided = i

        elif (list[i].collide_horizontal(ball.get_x()-ball.get_radius(), ball.get_y() - ball.get_radius(),
                                   ball.get_x() + ball.get_radius(), ball.get_y() + ball.get_radius())):
            ball.set_velocityY((-1) * ball.get_velocityY())
            collided = i

        if (collided is not None):
            del(list[collided])
            score += 1
            break


#move paddle
def move_paddle():
    global paddle_X
    #if the key to move paddle right is pressed
    if paddle_move_right:
        if (paddle.get_x() + PADDLE_LENGTH < WINDOW_X):
            paddle.move_right()
    # if the key to move paddle left is pressed
    elif paddle_move_left:
        if (paddle.get_x() > 0):
            paddle.move_left()

#checks if game is won (won meaning no more blocks on the screen)
def game_win_check():
    global game_won, game_start, game_over
    if (len(blocks_list) == 0):
        game_won = True

#main draw function
def draw():
    global new_game, blocks_list

    if (new_game):
        start_game(BLOCK_ROWS, BLOCK_COLUMNS)
        set_clear_color(1, 1, 1)
        new_game = False

    clear()

    for brick in blocks_list:
        enable_stroke()
        brick.draw()

    ball.draw()
    paddle.draw()
    game_win_check()

    if (not game_start):
        draw_text("Lives Left: " + str(lives_left), 300, 390)

    #game has started
    if (game_start):
        ball.move()
        move_paddle()
        collision(blocks_list)
        lives_lost()

    #player won the game
    elif (game_won):
        set_clear_color(.5, .5, .5)
        clear()
        draw_text("You won!", 160, 200)
        draw_text("Score: " + str(score), 180, 220)

    #game lost
    elif (game_over):
        set_clear_color(1, 0, 0)
        clear()
        draw_text("Better Luck Next Time :(", 130, 200)
        draw_text("Score: " + str(score), 180, 220)


start_graphics(draw, key_press=key_pressed, key_release=key_release)