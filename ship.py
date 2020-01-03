from screen import Screen
import math

class Ship:

    def __init__(self, x_location, x_speed, y_location, y_speed, heading):
        self.x_location = x_location
        self.x_speed = x_speed
        self.y_location = y_location
        self.y_speed = y_speed
        self.heading = heading

    def move(self, location, x_speed, y_speed):
        """
        this function updates the location of the ship
        :param location: tuple, (x,y) representing the location of the ship on
         the axis
        :param x_speed: int, the ship's speed on the x axis
        :param y_speed: int, the ship's speed on the y axis
        """
        x, y = location
        new_x = Screen.SCREEN_MIN_X + (x + x_speed - Screen.SCREEN_MIN_X) % \
                (Screen.SCREEN_MAX_X - Screen.SCREEN_MIN_X)
        new_y = Screen.SCREEN_MIN_Y + (y + y_speed - Screen.SCREEN_MIN_Y) % \
                (Screen.SCREEN_MAX_Y - Screen.SCREEN_MIN_Y)
        self.x_location = new_x
        self.y_location = new_y

    def change_direction(self):
        """
        this function changes the heading value of the ship
        :return: nothing
        """
        if Screen.is_left_pressed():
            self.heading += 7
        elif Screen.is_right_pressed():
            self.heading -= 7

    def accelerate(self, x_speed, y_speed):
        """
        this function updates the x and y speed of the ship
        :param x_speed: current x speed
        :param y_speed: current y speed
        :return: nothing
        """
        new_x = x_speed + math.cos(self.heading)
        new_y = y_speed + math.sin(self.heading)
        self.x_speed = new_x
        self.y_speed = new_y
