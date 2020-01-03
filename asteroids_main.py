from screen import Screen
import sys
import random
from ship import Ship
from asteroid import Asteroid
from torpedo import Torpedo
import math

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
        self.torpedoes = []


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
        self.__screen.draw_ship(self.ship.x_location, self.ship.y_location, self.ship.heading)
        self.move_all()
        #for asteroid in self.asteroids:






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
            new_asteroid = Asteroid(location[0], asteroid_speed[0], location[1], asteroid_speed[1], INIT_ASTEROID_SIZE)
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

    def move_all(self):
        for asteroid in self.asteroids:
            asteroid.move()
            self.__screen.draw_asteroid(asteroid, asteroid.x_location, asteroid.y_location)
            if asteroid.has_intersection(self.ship):
                self.__screen.show_message("Message", "You lost a life!")
                self.__screen.remove_life()
                self.ship.life -= 1
                self.__screen.unregister_asteroid(asteroid)
                self.asteroids.remove(asteroid)
                break
        if self.__screen.is_left_pressed():
            self.ship.change_direction("l")
        elif self.__screen.is_right_pressed():
            self.ship.change_direction("r")
        elif self.__screen.is_up_pressed():
            self.ship.accelerate()
        self.ship.move()

    def add_torpedo(self):
        x_speed = self.ship.x_speed + 2*math.cos(math.radians(self.ship.heading))
        y_speed = self.ship.y_speed + 2*math.sin(math.radians(self.ship.heading))
        x_location = self.ship.x_location
        y_location = self.ship.y_location
        heading = self.ship.heading
        new_torpedo = Torpedo(x_location, x_speed, y_location, y_speed, heading)
        return new_torpedo

    def shoot_torpedo(self):
        if Screen.is_space_pressed():
            new_torpedo = self.add_torpedo()
            self.torpedoes.append(new_torpedo)
            self.__screen.register_torpedo(new_torpedo)







def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
