from screen import Screen
import math


class Ship:
    """
                A class used to represent a ship

                ...

                Attributes
                ----------
                self.x_location : int
                    the x part of coordinates that represent the location of the ship
                self.x_speed : int
                    the x component of the speed of the ship
                self.y_location : int
                    the y part of coordinates that represent the location of the ship
                self.y_speed : int
                    the y component of the speed of the ship
                self.heading : int
                    the direction of the ship's prow in degrees
                self.life  : int
                    the number of lives the ship has in the game
                self.__radius : int
                    the radius of the ship

                Methods
                -------
                move():
                    this function updates the location of the ship according to the
                    current location and speed
                change_direction(direction):
                    changes the heading of the ship according to the direction provided
                    :param direction: str, "l" or "r"
                    :return:
                accelerate():
                    this function updates the x and y speed of the ship
                    :return: nothing
                get_radius():
                    :return: the radius of the ship (int)
                """

    def __init__(self, x_location, x_speed, y_location, y_speed, heading):
        self.x_location = x_location
        self.x_speed = x_speed
        self.y_location = y_location
        self.y_speed = y_speed
        self.heading = heading
        self.life = 3
        self.__radius = 1

    def move(self):
        """
        this function updates the location of the ship according to the current
         location and speed
        """
        new_x = Screen.SCREEN_MIN_X + \
                (self.x_location + self.x_speed - Screen.SCREEN_MIN_X) % \
                (Screen.SCREEN_MAX_X - Screen.SCREEN_MIN_X)
        new_y = Screen.SCREEN_MIN_Y + \
                (self.y_location + self.y_speed - Screen.SCREEN_MIN_Y) % \
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
        """
        :return: the radius of the ship (int)
        """
        return self.__radius
