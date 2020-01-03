from screen import Screen


def move(location, x_speed, y_speed):
    """

    :param location:
    :param x_speed:
    :param y_speed:
    :return:
    """
    x, y = location
    new_x = Screen.SCREEN_MIN_X + (x + x_speed - Screen.SCREEN_MIN_X) % \
        (Screen.SCREEN_MAX_X - Screen.SCREEN_MIN_X)
    new_y = Screen.SCREEN_MIN_Y + (y + y_speed - Screen.SCREEN_MIN_Y) % \
        (Screen.SCREEN_MAX_Y - Screen.SCREEN_MIN_Y)
    new_location = (new_x, new_y)
    return new_location


class Ship:

    def __init__(self, x_location, x_speed, y_location, y_speed, heading):
        self.x_location = x_location
        self.x_speed = x_speed
        self.y_location = y_location
        self.y_speed = y_speed
        self.heading = heading

    def change_direction(self):
        if Screen.is_left_pressed():
            self.heading += 7
        elif Screen.is_right_pressed():
            self.heading -= 7

