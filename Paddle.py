#Paddle class for creation and updating of paddle in Breakout game
#Jasmine Mai, October 10, 2017

from cs1lib import *

class Paddle:
    def __init__(self, x, y, r, g, b, length, height, speed):
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.speed = speed
        self.r = r
        self.g = g
        self.b = b

    #move paddle
    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    #checks if collision with the paddle on the left side
    def collision_left (self, x1, x2, y):
        if (y >= self.y and y <= self.y + self.height):
            if (x2 >= self.x and x2 <= self.x + (self.length // 2)):
                return True
        return False

    #checks if collision with the paddle on the right side
    def collision_right(self, x1, x2, y):
        if (y >= self.y and y <= self.y + self.height):
            if (x2 > self.x + (self.length // 2) and x1 <= self.x + self.length):
             return True
        return False

    # calculate collision distance from center
    def calculate_collision_left(self, x):
        return abs((x - (self.x + (self.length // 2))))

    #calculate collision distance from center
    def calculate_collision_right(self, x):
        return abs(((self.x + (self.length // 2)) - x))

    def draw(self):
        set_fill_color(self.r, self.g, self.b)
        draw_rectangle(self.x, self.y, self.length, self.height)

    #getters and setters
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_vx(self, vx):
        self.speed = vx

    def get_length(self):
        return self.length

