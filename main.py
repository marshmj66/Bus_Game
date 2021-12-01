import pygame
from pygame.locals import QUIT
import stage
import os
import random

pygame.init()
pygame.mixer.init()

displayWH = (900,500)

displaysurface = pygame.display.set_mode(displayWH)
pygame.display.set_caption("Bus Game")

icon = pygame.image.load('Assets\\bus_boys.png')
pygame.display.set_icon(icon)

wrong_sound = pygame.mixer.Sound(os.path.join('Assets\\Wrong-answer-sound-effect.mp3'))
success_sound = pygame.mixer.Sound(os.path.join("Assets\\success-sound-effect.mp3"))

displaysurface.fill('gray')

clock = pygame.time.Clock()

start_btn = stage.Start_Button()

game_btns = stage.Game_btn(displayWH)

screen_clear = stage.Clear_Screen()

#global varibles
guess = ''
wrong = ''
table = []
ts = 0
table_phase = 0
table_set = 0
game_start = 0

class Driver:
    deck_set = 14

    def __init__(self):
        self.suits = ['Hearts',"Diamonds","Spades","Clubs"]
        self.deck = []
        self.deck_counter = 0
        #self.make_deck()

    def make_deck(self):
        for n in range(1,self.deck_set):
            for s in self.suits:
                if n == 1:
                    self.deck.append('Ace'+" "+s)
                elif n == 11:
                    self.deck.append('Jack' + " " + s)
                elif n == 12:
                    self.deck.append('Queen' + " " + s)
                elif n == 13:
                    self.deck.append('King' + " " + s)
                else:
                    self.deck.append(str(n) +" "+ s)

    def deck_shuffle(self):
        random.shuffle(self.deck)

    def pick_card(self):
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card

#start the driver object
driver = Driver()

class Rider:
    def __init__(self,name):
        self.name = name
        self.label = stage.Label()
        self.driver = driver
        global ts
        if len(self.driver.deck) == 0:
            table.clear()
            self.driver.deck_counter += 1
            self.driver.make_deck()
            self.driver.deck_shuffle()

        if table_set == 0:
            ts = 0
        elif table_set == 1 and table_phase == 1:
            ts = 1
            hold = table.pop()
            table.clear()
            table.append(hold)

        if wrong != '':
            self.label.start_label(displaysurface,[wrong],set=ts)
        else:
            self.label.start_label(displaysurface, table,ts)

    def guess_color(self,g):
            global guess
            global table_phase
            global table
            global table_set
            global wrong

            guess = ''
            fcard = self.driver.pick_card()
            card = fcard.split()
            table.append(fcard)

            if g == 'black':
                if card[1] == "Clubs" or card[1] == 'Spades':
                    if table_set == 2:
                        table_set += 1
                        success_sound.play()
                    else:
                        wrong = ''
                        table_phase += 1
                        success_sound.play()
                else:
                    wrong_sound.play()
                    table_set = 0
                    wrong = table.pop()
                    table.clear()

            elif g == 'red':
                if card[1] == "Diamonds" or card[1] == 'Hearts':
                    if table_set == 2:
                        table_set += 1
                        success_sound.play()
                    else:
                        wrong = ''
                        table_phase += 1
                        success_sound.play()
                else:
                    wrong_sound.play()
                    wrong = table.pop()
                    table_set = 0
                    table.clear()

    def guess_higher_lower(self,g):
        global guess
        global wrong
        global table
        global table_set
        global table_phase

        guess = ''
        number = 0
        answer = None
        fcard = self.driver.pick_card()
        card = fcard.split()
        table.append(fcard)

        card_compare = table[0].split()
        compare = 0

        if card_compare[0].isdigit():
            compare = int(card_compare[0])
        else:
            if card_compare[0] == 'Ace':
                compare = 1
            elif card_compare[0] == 'Jack':
                compare = 10
            elif card_compare[0] == 'Queen':
                compare = 11
            elif card_compare[0] == 'King':
                compare = 12

        if card[0].isdigit():
            number = int(card[0])
        else:
            if card[0] == 'Ace':
                number = 1
            elif card[0] == 'Jack':
                number = 10
            elif card[0] == 'Queen':
                number = 11
            elif card[0] == 'King':
                number = 12

        if number != 0:
            if number == compare:
                print('same wrong')
            if number < compare:
                answer = 'lower'
            elif number > compare:
                answer = 'higher'
        if answer == g:
            table_phase += 1
            success_sound.play()
        else:
            table_phase = 0
            table_set = 0
            table.clear()
            wrong_sound.play()

    def guess_outside_inbetween(self,g):
        global guess
        global table
        global table_set
        global table_phase
        guess = ''
        answer = None

        number = 0
        first = table[0].split()[0]
        second = table[1].split()[0]

        if first.isdigit():
            first = int(first)
        else:
            if first == 'Ace':
                first = 1
            elif first == 'Jack':
                first = 10
            elif first == 'Queen':
                first = 11
            elif first == 'King':
                first = 12

        if second.isdigit():
            second = int(second)
        else:
            if second == 'Ace':
                second = 1
            elif second == 'Jack':
                second = 10
            elif second == 'Queen':
                second = 11
            elif second == 'King':
                second = 12



        fcard = self.driver.pick_card()
        card = fcard.split()
        table.append(fcard)

        if card[0].isdigit():
            number = int(card[0])
        else:
            if card[0] == 'Ace':
                number = 1
            elif card[0] == 'Jack':
                number = 10
            elif card[0] == 'Queen':
                number = 11
            elif card[0] == 'King':
                number = 12
        if number != 0:
            if first == second:
                print('same fail')
            if first < second:
                if first < number < second:
                    answer = "inbetween"
                else:
                    answer = 'outside'
            elif second < first:
                if second < number < first:
                    answer = 'inbetween'
                else:
                    answer = 'outside'

        if answer:
            if answer == g:
                table_phase += 1
                success_sound.play()
            else:
                table.clear()
                table_set = 0
                table_phase = 0
                wrong_sound.play()

while True:  # main game loop
    if game_start == 1:
        screen_clear.clear(displaysurface)

        if table_set == 3:
            screen_clear.clear(displaysurface)
            stage.Victory_Page().show_page(displaysurface,driver.deck_counter)
        else:
            rider = Rider('Rider')

        if table_phase == 0 and table_set != 3:
            game_btns.red_btn(displaysurface)
            game_btns.black_btn(displaysurface)
            if guess != '':
                rider.guess_color(guess)

        elif table_phase == 1:
            game_btns.higher_btn(displaysurface)
            game_btns.lower_btn(displaysurface)
            if guess != '':
                rider.guess_higher_lower(guess)
        elif table_phase == 2:
            game_btns.outside_btn(displaysurface)
            game_btns.inbetween_btn(displaysurface)
            if guess != '':
                rider.guess_outside_inbetween(guess)
        elif table_phase == 3:
            table_set += 1
            table_phase = 0

    else:
        start_btn.bliting(game_start, displaysurface, displayWH)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mospos = pygame.mouse.get_pos()
            if mospos[0] >= 326 and mospos[1] >= 145 and mospos[0] <= 523 and mospos[1] <= 344 and game_start == 0:
                game_start = 1
            elif mospos[0] >= 151 and mospos[1] >= 301 and mospos[0] <= 398 and mospos[1] <= 448 and table_set == 3:
                table_set = 0
                table_phase = 0
            elif mospos[0] >= 600 and mospos[1] >= 302 and mospos[0] <= 798 and mospos[1] <= 447 and table_set == 3:
                exit()
            elif mospos[0] >= 151 and mospos[1] >= 302 and mospos[0] <= 347 and mospos[1] <= 447 and game_start == 1:
                if table_phase == 0:
                    guess = 'red'
                elif table_phase == 1:
                    guess = 'lower'
                elif table_phase == 2:
                    guess = 'outside'
            elif mospos[0] >= 601 and mospos[1] >= 300 and mospos[0] <= 797 and mospos[1] <= 445 and game_start == 1:
                if table_phase == 0:
                    guess = 'black'
                elif table_phase == 1:
                    guess = "higher"
                elif table_phase == 2:
                    guess = 'inbetween'

    pygame.display.update()

    clock.tick(15)
