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
POINTS_BY_ASTEROIDS_SIZE = {1: 100, 2: 50, 3: 20}
WINNING_MSG = "All asteroids have been eliminated! Good job, Hero."
LOSING_MSG = "You have been terminated, Bad luck :("
QUITTING_MSG = "That's it? Well ok... Bye!"


class GameRunner:

    def __init__(self, asteroids_amount=DEFAULT_ASTEROIDS_NUM):
        self.__screen = Screen()
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self.ship = self.add_ship()
        self.asteroids = []
        self.add_initial_asteroids(DEFAULT_ASTEROIDS_NUM)
        self.torpedoes = []
        self.score = 0

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
        self.__screen.draw_ship(self.ship.x_location, self.ship.y_location,
                                self.ship.heading)
        self.shoot_torpedo()
        self.torpedo_time()
        self.move_all()
        self.if_game_over()

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

    def add_initial_asteroids(self, asteroid_num):
        """
        this function adds asteroids to the game asteroid list, and registers
        them on screen
        :param asteroid_num: int, number of asteroids wanted added to the game
        :return:None
        """
        for i in range(asteroid_num):
            location = self.generate_random_location()
            while location[0] == self.ship.x_location and location[
                1] == self.ship.y_location:
                location = self.generate_random_location()
            asteroid_speed = self.generate_asteroid_speed()
            new_asteroid = Asteroid(location[0], asteroid_speed[0],
                                    location[1], asteroid_speed[1],
                                    INIT_ASTEROID_SIZE)
            self.add_asteroid(new_asteroid)

    def add_asteroid(self, asteroid):
        """
        this function adds an individual asteroid object to the game
        :param asteroid: an Asteroid type object
        :return: None
        """
        self.asteroids.append(asteroid)
        self.__screen.register_asteroid(asteroid, asteroid.size)

    def generate_asteroid_speed(self):
        """
        this function generates random x and y speed for asteroid speed use
        :return:int, x speed and y speed
        """
        asteroid_speed_x = random.randint(MIN_ASTEROID_SPEED,
                                          MAX_ASTEROID_SPEED)
        while asteroid_speed_x == 0:
            asteroid_speed_x = random.randint(MIN_ASTEROID_SPEED,
                                              MAX_ASTEROID_SPEED)
        asteroid_speed_y = random.randint(MIN_ASTEROID_SPEED,
                                          MAX_ASTEROID_SPEED)
        while asteroid_speed_y == 0:
            asteroid_speed_y = random.randint(MIN_ASTEROID_SPEED,
                                              MAX_ASTEROID_SPEED)
        return asteroid_speed_x, asteroid_speed_y

    def move_all(self):
        """
        this function moves all the objects in the game and updates their
        status on screen
        :return: None
        """
        for asteroid in self.asteroids:
            asteroid.move()
            self.__screen.draw_asteroid(asteroid, asteroid.x_location,
                                        asteroid.y_location)
            if asteroid.has_intersection(self.ship):
                self.intersection_with_ship(asteroid)
            for torpedo in self.torpedoes:
                if asteroid.has_intersection(torpedo):
                    self.intersection_with_torpedo(asteroid, torpedo)
        if self.__screen.is_left_pressed():
            self.ship.change_direction("l")
        elif self.__screen.is_right_pressed():
            self.ship.change_direction("r")
        elif self.__screen.is_up_pressed():
            self.ship.accelerate()
        self.ship.move()
        for torpedo in self.torpedoes:
            torpedo.move()
            self.__screen.draw_torpedo(torpedo, torpedo.x_location,
                                       torpedo.y_location, torpedo.heading)

    def intersection_with_ship(self, asteroid):
        """
        this function checks if the ship is intersecting with an asteroid, and
        if so, the ship loses one life point, and a message pops up.
        :param asteroid:
        :return:None
        """
        self.__screen.show_message("Message", "You lost a life!")
        self.__screen.remove_life()
        self.ship.life -= 1
        self.__screen.unregister_asteroid(asteroid)
        self.asteroids.remove(asteroid)

    def intersection_with_torpedo(self, asteroid, torpedo):
        """
        this function checks if there are torpedoes intersecting with asteroids
        and if so, adds score points.
        :param torpedo:
        :param asteroid:
        :return:
        """
        self.score += POINTS_BY_ASTEROIDS_SIZE[asteroid.size]
        self.__screen.set_score(self.score)
        self.asteroid_split(asteroid, torpedo)

    def asteroid_split(self, asteroid, torpedo):
        """
        this method checks whether the size of the asteroid is more than 1,
         and if it is it will split it into 2 smaller asteroids
        :param asteroid: an Asteroid object
        :param torpedo: a torpedo object
        :return: None
        """
        if asteroid.size == 1:
            self.asteroids.remove(asteroid)
            self.__screen.unregister_asteroid(asteroid)
        else:
            new_speed = self.calculate_new_speed(asteroid, torpedo)
            x_speed = new_speed[0]
            y_speed = new_speed[1]
            if asteroid.size == 2 or asteroid.size == 3:
                asteroid_1 = Asteroid(asteroid.x_location, x_speed,
                                      asteroid.y_location, -y_speed,
                                      asteroid.size - 1)
                asteroid_2 = Asteroid(asteroid.x_location, -x_speed,
                                      asteroid.y_location, y_speed,
                                      asteroid.size - 1)
                self.add_asteroid(asteroid_1)
                self.add_asteroid(asteroid_2)
                self.__screen.unregister_asteroid(asteroid)
                self.asteroids.remove(asteroid)
        self.__screen.unregister_torpedo(torpedo)
        self.torpedoes.remove(torpedo)

    def calculate_new_speed(self, asteroid, torpedo):
        """
        this function calculates the new speed of the split asteroid according to the speed of
        it's mother asteroid and the speed of the torpedo that hit it
        :param asteroid: an Asteroid object
        :param torpedo: a Torpedo object
        :return: tuple (new_speed_x, new_speed_y)
        """
        new_speed_x = (torpedo.x_speed + asteroid.x_speed) / math.sqrt(
            asteroid.x_speed ** 2 + asteroid.y_speed ** 2)
        new_speed_y = (torpedo.y_speed + asteroid.y_speed) / math.sqrt(
            asteroid.x_speed ** 2 + asteroid.y_speed ** 2)
        return new_speed_x, new_speed_y

    def add_torpedo(self):
        """
        this function returns a new torpedo object, with attributes depending
        on the ship current location, speed and heading.
        :return: torpedo type object
        """
        x_speed = self.ship.x_speed + 2 * math.cos(
            math.radians(self.ship.heading))
        y_speed = self.ship.y_speed + 2 * math.sin(
            math.radians(self.ship.heading))
        x_location = self.ship.x_location
        y_location = self.ship.y_location
        heading = self.ship.heading
        new_torpedo = Torpedo(x_location, x_speed, y_location, y_speed,
                              heading)
        return new_torpedo

    def shoot_torpedo(self):
        """
        this function adds the new torpedo to the game, adding it to a torpedo
        list, and registering it on screen.
        :return:
        """
        if self.__screen.is_space_pressed() and len(self.torpedoes) <= 10:
            new_torpedo = self.add_torpedo()
            self.torpedoes.append(new_torpedo)
            self.__screen.register_torpedo(new_torpedo)

    def torpedo_time(self):
        """
        this function removes a torpedo object from the game and screen if
        it has been around for 200 rounds (200 calls for the game_loop func)
        :return: None
        """
        for torpedo in self.torpedoes:
            torpedo.life_time += 1
            if torpedo.life_time >= 200:
                self.__screen.unregister_torpedo(torpedo)
                self.torpedoes.remove(torpedo)

    def if_game_over(self):
        """
        this function checks if one of the conditions for ending the game is
        met, and if so, ends the game
        :return:
        """
        if not self.asteroids and self.ship.life > 0:  # if there's no asteroids left
            self.__screen.show_message("You Won!", WINNING_MSG)
            self.__screen.end_game()
            sys.exit()
        elif self.ship.life == 0:  # the ships has no more lives
            self.__screen.show_message("You Died!", LOSING_MSG)
            self.__screen.end_game()
            sys.exit()
        elif self.__screen.should_end():  # the player pressed "q"
            self.__screen.show_message("Quit", QUITTING_MSG)
            self.__screen.end_game()
            sys.exit()


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
