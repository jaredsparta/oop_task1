class FizzBuzz:
    # I put the play() function in the init so all one needs
    # to do is call any instance of the class
    def __init__(self, final_number):
        self.final_number = final_number
        self.play()
    
    # This prints the FIZZ, BUZZ and FIZZBUZZ as required
    # Checks using modulo for divisibility
    def play(self):
        for num in range(1, self.final_number + 1):
            val = ''
            if num % 3 == 0:
                val += "FIZZ"

            if num % 5 == 0:
                val += "BUZZ"

            if not val:
                print(num)
                
            else:
                print(val)


FizzBuzz(100)