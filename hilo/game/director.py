from game.cards import Cards


class Director:

    def __init__(self):

        self.points = 300
        self.score = 0
        self.is_playing = True
        self.cards = Cards()


    def start_game(self):

        while self.is_playing == True:
            self.do_first_card()
            self.get_high_low()
            self.do_second_card()
            self.update()
            self.get_keep_playing()
            
    
    def get_high_low(self):
        
        self.high_or_low = input('Will the next card be higher or lower? [h/l]: ')


    def get_keep_playing(self):

        self.keep_playing = input('Do you want to keep playing? [y/n]: ')
        if self.keep_playing.lower() == 'y':
            self.is_playing = True

        else:
            self.is_playing = False


    def do_first_card(self):
        
        self.first_card = self.cards.draw()
        print(f'The card is: {self.first_card}')


    def do_second_card(self):

        self.second_card = self.cards.draw()
        print(f'The next card is: {self.second_card}')


    def update(self):

        if (self.first_card > self.second_card) and self.high_or_low.lower() == 'l':
            self.points += 100
            print(f'Your score is: {self.points}')
        
        if (self.first_card < self.second_card) and self.high_or_low.lower() == 'h':
            self.points += 100
            print(f'Your score is: {self.points}')
            
        else:
            self.points -= 75
            if self.points <= 0:
                self.is_playing = False
        

