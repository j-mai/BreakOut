#Ball class for Breakout game
#Jasmine Mai

from cs1lib import *

class Ball:
    def __init__(self, x, y, radius, r, g, b, velocity_x, velocity_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.r = r
        self.g = g
        self.b = b
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    #move the ball
    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    #draw the ball
    def draw(self):
        set_fill_color(self.r, self.g, self.b)
        draw_ellipse(self.x, self.y, self.radius, self.radius)

    #getters and setters
    def get_x (self):
        return self.x

    def get_y(self):
        return self.y

    def set_x (self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_radius (self):
        return self.radius

    def get_velocityX(self):
        return self.velocity_x

    def get_velocityY(self):
        return self.velocity_y

    def set_velocityY(self, velocity):
        self.velocity_y = velocity

    def set_velocityX(self, velocity):
        self.velocity_x = velocity

