class FB:
    # Gives user the choice of which number is fizz and buzz
    # By default, I set it to 3 and 5
    # They also have the option to choose what integer to go up to
    def __init__(self, fizz = 3, buzz = 5, final_number = 100):
        self.fizz = fizz
        self.buzz = buzz
        self.final_number = final_number
        self.list = self.play()

    # This calls the game to play
    # I store the values in a list
    def play(self):
        list = []
        for number in range(1, self.final_number + 1):
            if number % self.fizz == 0 and number % self.buzz == 0:
                list.append("FIZZBUZZ")
            elif number % self.fizz == 0:
                list.append("FIZZ")
            elif number % self.buzz == 0:
                list.append("BUZZ")
            else:
                list.append(number)
        return list

    # This is more user-friendly as you can see all values without scrolling
    def show_as_list(self):
        return self.list

    # This shows the values line-by-line
    def show(self):
        for item in self.list:
            print(item)

    # Shows how many FIZZ's, BUZZ's and FIZZBUZZ's there are
    def count(self):
        fizz_no = self.list.count("FIZZ")
        buzz_no = self.list.count("BUZZ")
        fizzbuzz_no = self.list.count("FIZZBUZZ")
        return f"""
                There are {fizz_no} FIZZ's
                There are {buzz_no} BUZZ's
                There are {fizzbuzz_no} FIZZBUZZ's"""

# Since we can choose the numbers to check, we use input to get input
# I have a try except just to ensure they put integers as values
while True:
    try:
        fizz = int(input("Choose an integer for fizz: "))
        buzz = int(input("Choose an integer for buzz: "))
        final_number = int(input("Choose a number to go up to: "))
        break

    except:
        print("")
        continue

# This initialises the game with their inputs
fb = FB(fizz, buzz, final_number)
print("")

# This allows the user to show how they like it
while True:
    choice = input("""Choose an option (1, 2, 3):
                    1. Show as list
                    2. Show altogether
                    3. Show how many Fizzes, Buzzes and FizzBuzzes
                    4. Exit
                        ->""")
    if choice == "1":
        print(fb.show_as_list())
        print("")
        
    elif choice == "2":
        fb.show()
        print("")

    elif choice == "3":
        print(fb.count())
        print("")

    elif choice == "4":
        break

    else:
        print("")
        continue
    