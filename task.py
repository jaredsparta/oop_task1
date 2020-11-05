class Fizz:
    def __init__(self):
        pass

    # Returns a FIZZ if a multiple of 3
    def fizz(self, number):
        if number % 3 == 0:
            return "FIZZ"


class Buzz:
    def __init__(self):
        pass

        # Returns BUZZ if number is multiple of 5
    def buzz(self, number):
        if number % 5 == 0:
            return "BUZZ"

class FizzBuzz:
    def __init__(self):
        pass

    # Returns FIZZBUZZ if number is multiple of both 3 and 5
    def buzz(self, number):
        if number % 5 == 0 and number % 3 == 0:
            return "FIZZBUZZ"

class Game(Fizz, Buzz, FizzBuzz):
    def __init__(self, max_number):
        pass

