from screen import Screen
import math
from ship import Ship


class Asteroid:
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
        return self.__radius


if __name__ == '__main__':
    my_asteroid = Asteroid(439, 1, 73, 4, 3)
    my_ship = Ship(439, 1, 73, 4, 7)
    print(my_asteroid.has_intersection(my_ship))
