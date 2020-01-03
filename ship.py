from screen import Screen
class Ship:

    def __init__(self, x_location, x_speed, y_location, y_speed, heading):
        self.x_location = x_location
        self.x_speed = x_speed
        self.y_location = y_location
        self.y_speed = y_speed
        self.heading = heading

    def move(self, location, x_speed, y_speed):
        x, y = location
        new_x = Screen.SCREEN_MIN_X + (x + x_speed - Screen.SCREEN_MIN_X) % \
            (Screen.SCREEN_MAX_X - Screen.SCREEN_MIN_X)

    def change_direction(self):
        if Screen.is_left_pressed():
            self.prow_tuning += 7
        elif Screen.is_right_pressed():
            self.prow_tuning -= 7

