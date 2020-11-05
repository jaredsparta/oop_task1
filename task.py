class FizzBuzz:
    # I put the play() function in the init so all one needs
    # to do is call any instance of the class
    def __init__(self, final_number):
        self.final_number = final_number
        self.play()
    
    # This prints the FIZZ, BUZZ and FIZZBUZZ as required
    # Checks using modulo for divisibility
    def play(self):
        for number in range(1, self.final_number + 1):
            if number % 3 == 0 and number % 5 == 0:
                print("FIZZBUZZ")
            elif number % 3 == 0:
                print("FIZZ")
            elif number % 5 == 0:
                print ("BUZZ")
            else:
                print(number)


FizzBuzz(100)