from screen import Screen
import math


class Asteroid:
    """
            A class used to represent an Asteroid

            ...

            Attributes
            ----------
            self.x_location : int
                the x part of coordinates that represent the location of the asteroid
            self.x_speed : int
                the x component of the speed of the Asteroid
            self.y_location : int
                the y part of coordinates that represent the location of the asteroid
            self.y_speed : int
                the y component of the speed of the Asteroid
            self.size : int
                the size of the asteroid
            self.__radius = self.size * 10 - 5
                the radius of the asteroid calculated according to the size of the asteroid

            Methods
            -------
            move():
                this function updates the location of the asteroid according to the
                current location and speed
            has_intersection(obj):
                this function checks if an object has the same location as an asteroid
                :param obj: ship or torpedo type object
                :return: True if there's an intersection, False otherwise
            get_radius():
                :return: an int value for the object's radius
            """

    def __init__(self, x_location, x_speed, y_location, y_speed, size):
        self.x_location = x_location
        self.x_speed = x_speed
        self.y_location = y_location
        self.y_speed = y_speed
        self.size = size
        self.__radius = self.size * 10 - 5

    def move(self):
        """
        this function updates the location of the asteroid according to the
         current location and speed
        """
        new_x = Screen.SCREEN_MIN_X + \
                (self.x_location + self.x_speed - Screen.SCREEN_MIN_X) % \
                (Screen.SCREEN_MAX_X - Screen.SCREEN_MIN_X)
        new_y = Screen.SCREEN_MIN_Y + \
                (self.y_location + self.y_speed - Screen.SCREEN_MIN_Y) % \
                (Screen.SCREEN_MAX_Y - Screen.SCREEN_MIN_Y)
        self.x_location = new_x
        self.y_location = new_y

    def has_intersection(self, obj):
        """
        this function checks if an object has the same location as an asteroid
        :param obj: ship or torpedo type object
        :return: True if there's an intersection, False otherwise
        """
        distance = math.sqrt((obj.x_location - self.x_location) ** 2 + (
                    obj.y_location - self.y_location) ** 2)
        if distance <= self.get_radius() + obj.get_radius():
            return True
        else:
            return False

    def get_radius(self):
        """
        :return: an int value for the object's radius
        """
        return self.__radius



