from screen import Screen
import sys
import random
from ship import Ship

DEFAULT_ASTEROIDS_NUM = 5


class GameRunner:

    def __init__(self, asteroids_amount):
        self.__screen = Screen()

        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y

    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You should not to change this method!
        self._game_loop()
        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def _game_loop(self):
        # TODO: Your code goes here
        self.add_ship()
        pass

    def generate_random_location(self):
        x_location = random.randint(self.__screen_min_x, self.__screen_max_x)
        y_location = random.randint(self.__screen_min_y, self.__screen_max_y)
        return x_location, y_location

    def add_ship(self):
        location = self.generate_random_location()
        ship = Ship(location[0], 0, location[1], 0, 0)
        self.__screen.draw_ship(ship.x_location, ship.y_location, ship.heading)
        return

def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
