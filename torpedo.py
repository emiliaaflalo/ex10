from screen import Screen


class Torpedo:
    """
                 A class used to represent a torpedo

                 ...

                 Attributes
                 ----------
                 self.x_location : int
                     the x part of coordinates that represent the location of the torpedo
                 self.x_speed : int
                     the x component of the speed of the torpedo
                 self.y_location : int
                     the y part of coordinates that represent the location of the torpedo
                 self.y_speed : int
                     the y component of the speed of the torpedo
                 self.heading : int
                     the direction of the torpedo's heading in degrees which is equal to the ship's heading
                 self.life_time  : int
                     keeps the amount of turns for which the torpedo is still on screen
                 self.__radius : int
                     the radius of the torpedo

                 Methods
                 -------
                 move():
                     this function updates the location of the torpedo according to the current location and speed
                     :return: None
                     :return: the radius of the torpedo (int)
                 """

    def __init__(self, x_location, x_speed, y_location, y_speed, heading,
                 life_time=0):
        self.x_location = x_location
        self.x_speed = x_speed
        self.y_location = y_location
        self.y_speed = y_speed
        self.heading = heading
        self.__radius = 4
        self.life_time = life_time

    def move(self):
        """
        this function updates the location of the torpedo according to the
         current location and speed
        :return: None
        """
        new_x = Screen.SCREEN_MIN_X + \
                (self.x_location + self.x_speed - Screen.SCREEN_MIN_X) % \
                (Screen.SCREEN_MAX_X - Screen.SCREEN_MIN_X)
        new_y = Screen.SCREEN_MIN_Y + \
                (self.y_location + self.y_speed - Screen.SCREEN_MIN_Y) % \
                (Screen.SCREEN_MAX_Y - Screen.SCREEN_MIN_Y)
        self.x_location = new_x
        self.y_location = new_y

    def get_radius(self):
        """
        :return: torpedo's radius
        """
        return self.__radius
