from game.cards import Cards #gets us the card class from the game folder

class Director:

    def __init__(self):
        self.points = 300
        self.score = 0
        self.is_playing = True
        self.cards = Cards()

    def start_game(self):
        print(" Guess if the next random card will be higher or lower than the previous one.\n If your points reach 0, the game is over") #description
        self.current_card = self.cards.draw() #gives us a starting card
        while self.is_playing == True: #running the game cycle here
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
        print(f"\n Game over\n Final score: {self.score}\n") #last message to display
            
    def get_inputs(self):
        print(f"\n\n\n\n\n\n\n   Score: {self.score}   Points: {self.points}") 
        print("______________________________")
        print(f"          _____\n         |⯁    |\n         |  {self.current_card:02} |\n         |    ⯁|\n          ¯¯¯¯¯") #prints card
        choice = input("\nHigher or lower [h/l]: ") #variable "choice" is local to this function because it dosent have a "self." prefix
        while choice.lower() != 'l' and choice.lower() != 'h': #this while loop will keep prompting until it recieves a valid response
            choice = input("[h/l]: ")
        if choice.lower() == 'l': 
            self.is_higher = False #since theres only two options higher or lower, we can turn this into a boolean variable
        else:
            self.is_higher = True

    def do_updates(self):
        self.previous_card = self.current_card #instead of the swap function these two lines take care of it
        self.current_card = self.cards.draw()
        #this "if" block of code takes care of all correct guesses using a bit of boolean algebra 
        if self.is_higher and self.current_card > self.previous_card or not self.is_higher and self.current_card < self.previous_card:
            self.points += 100                                      
            self.score += 1
            print("\n         Correct\n          +100")
        else:
            self.points -= 75
            print("\n        Incorrect\n           -75")

    def do_outputs(self):
        print((f"          _____\n         |⯁    |\n         |  {self.current_card:02} |\n         |    ⯁|\n          ¯¯¯¯¯")) #prints card
        print(f"\n   Score: {self.score}   Points: {self.points}")
        if self.points != 0: #if we have more than 0 points
            _continue = input("\nContinue? [y/n]: ") #_contine is local. also the underscore is there because "continue" cant be a variable name
            while _continue.lower() != 'y' and _continue.lower() != 'n': #again prompting the user to give a valid response
                _continue = input("[y/n]: ")
            self.is_playing = (_continue == 'y') #returns either true or false
        else:   #if we have less than 0 points the game is just over
            self.is_playing = False