from screen import Screen
import sys
import random
from ship import Ship
from asteroid import Asteroid

DEFAULT_ASTEROIDS_NUM = 5
INIT_ASTEROID_SIZE = 3
MIN_ASTEROID_SPEED = -4
MAX_ASTEROID_SPEED = 4




class GameRunner:

    def __init__(self, asteroids_amount=DEFAULT_ASTEROIDS_NUM):
        self.__screen = Screen()

        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self.ship = self.add_ship()
        self.asteroids = []
        self.add_asteroids(DEFAULT_ASTEROIDS_NUM)



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
        pass

    def generate_random_location(self):
        """
        this function generates a random x location and y location representing coordinate
        between the screen's limits
        :return: tuple in the shape (x_location, y_location)
        """
        x_location = random.randint(self.__screen_min_x, self.__screen_max_x)
        y_location = random.randint(self.__screen_min_y, self.__screen_max_y)
        return x_location, y_location

    def add_ship(self):
        """
        this function generates a new random location for a ship,
        creates a new one and draws it on the screen
        :return: None
        """
        location = self.generate_random_location()
        ship = Ship(location[0], 0, location[1], 0, 0)
        self.__screen.draw_ship(ship.x_location, ship.y_location, ship.heading)
        return ship

    def add_asteroids(self, asteroid_num):
        for i in range(asteroid_num):
            location = self.generate_random_location()
            while location[0] == self.ship.x_location and location[1] == self.ship.y_location:
                location = self.generate_random_location()
            asteroid_speed = self.generate_asteroid_speed()
            new_asteroid = Asteroid(location[0], asteroid_speed[0], location[0], asteroid_speed[1])
            self.asteroids.append(new_asteroid)
            self.__screen.register_asteroid(new_asteroid, INIT_ASTEROID_SIZE)

    def generate_asteroid_speed(self):
        asteroid_speed_x = random.randint(MIN_ASTEROID_SPEED, MAX_ASTEROID_SPEED)
        while asteroid_speed_x == 0:
            asteroid_speed_x = random.randint(MIN_ASTEROID_SPEED, MAX_ASTEROID_SPEED)
        asteroid_speed_y = random.randint(MIN_ASTEROID_SPEED, MAX_ASTEROID_SPEED)
        while asteroid_speed_y == 0:
            asteroid_speed_y = random.randint(MIN_ASTEROID_SPEED, MAX_ASTEROID_SPEED)
        return asteroid_speed_x, asteroid_speed_y




def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
