#Brick class for
from cs1lib import *
class Brick:
    def __init__(self, x, y, r, g, b, length, width):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.b = b
        self.length = length
        self.width = width
        self.border = 5

    #function to check if anything is colliding with the vertical wall
    #functions similarly to seeing if two lines are intersecting
    def collide_vertical(self, x1, y1, x2, y2):
        if (y1 >= self.y and y2 <= self.y + self.width):
            if (x2 >= self.x and x1 <= self.x + self.border):
                return True
            elif (x1 <= (self.x + self.length) and x2 >= (self.x + self.length - self.border)):
                return True
        return False

    #function to check if anything is colliding with the horizontal wall
    #functions similarly to seeing if two lines are intersecting
    def collide_horizontal(self, x1, y1, x2, y2):
        if (x2 >= self.x and x1 <= self.x + self.length):
            if (y2 >= self.y and y2 <= self.y + self.border):
                return True
            elif (y1 <= self.y + self.width and y1 >= self.y + self.width - self.border):
                return True
        return False

    #draw brick
    def draw(self):
        set_fill_color(self.r, self.g, self.b)
        draw_rectangle(self.x, self.y, self.length, self.width)

    #getters and setters
    def get_x (self):
        return self.x

    def get_y(self):
        return self.y

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y





