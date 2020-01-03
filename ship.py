from screen import Screen
import math


class Ship:

    def __init__(self, x_location, x_speed, y_location, y_speed, heading):
        self.x_location = x_location
        self.x_speed = x_speed
        self.y_location = y_location
        self.y_speed = y_speed
        self.heading = heading
        self.__radius = 1

    def move(self):
        """
        this function updates the location of the ship according to the current
         location and speed
        """
        new_x = Screen.SCREEN_MIN_X +\
                (self.x_location + self.x_speed - Screen.SCREEN_MIN_X) %\
                (Screen.SCREEN_MAX_X - Screen.SCREEN_MIN_X)
        new_y = Screen.SCREEN_MIN_Y +\
                (self.y_location + self.y_speed - Screen.SCREEN_MIN_Y) %\
                (Screen.SCREEN_MAX_Y - Screen.SCREEN_MIN_Y)
        self.x_location = new_x
        self.y_location = new_y

    def change_direction(self, direction):
        """
        changes the heading of the ship according to the direction provided
        :param direction: str, "l" or "r"
        :return:
        """
        if direction == "l":
            self.heading += 7
        elif direction == "r":
            self.heading -= 7

    def accelerate(self):
        """
        this function updates the x and y speed of the ship
        :return: nothing
        """
        new_x = self.x_speed + math.cos(math.radians(self.heading))
        new_y = self.y_speed + math.sin(math.radians(self.heading))
        self.x_speed = new_x
        self.y_speed = new_y

    def get_radius(self):
        return self.__radius
