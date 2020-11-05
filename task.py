class FizzBuzz:
    def __init__(self, final_number):
        pass
    
    def play(self, final_number):
        for number in range(1, final_number + 1):
            if number % 3 == 0 and number % 5 == 0:
                print("FIZZBUZZ")
            elif number % 3 == 0:
                print("FIZZ")
            elif number % 5 == 0:
                print ("BUZZ")
            else:
                print(number)


FizzBuzz(100)