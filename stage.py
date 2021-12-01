import pygame

class Clear_Screen:
    def clear(self,display):
        display.fill('gray')


class Start_Button:
    def __init__(self):
        pass

    def bliting(self,on,DISPLAYSURF,WH):
        if on == 0:
            self.start_btn = pygame.draw.rect(DISPLAYSURF, 'lightyellow', (325, 145, 200, 200), 0)
            self.smallfont = pygame.font.SysFont('Corbel', 65)
            self.text = self.smallfont.render('Start', True, 'black')
            DISPLAYSURF.blit(self.text, (WH[0] // 2.5, WH[1] // 2.5))

class Game_btn:
    def __init__(self,WH):
        self.WH = WH
    def red_btn(self,DISPLAYSURF):
        self.red_btnt = pygame.draw.rect(DISPLAYSURF, 'red', (150, 300, 200, 150), 0)
        self.smallfont = pygame.font.SysFont('Corbel', 65)
        self.text = self.smallfont.render('Red', True, 'black')
        DISPLAYSURF.blit(self.text, (200,345))

    def black_btn(self,DISPLAYSURF):
        self.black_btnt = pygame.draw.rect(DISPLAYSURF, 'black', (600, 300, 200, 150), 0)
        self.smallfont = pygame.font.SysFont('Corbel', 65)
        self.text = self.smallfont.render('Black', True, 'white')
        DISPLAYSURF.blit(self.text, (630,335))
    def lower_btn(self,DISPLAYSURF):
        self.red_btnt = pygame.draw.rect(DISPLAYSURF, 'red', (100, 300, 300, 150), 0)
        self.smallfont = pygame.font.SysFont('Corbel', 65)
        self.text = self.smallfont.render('Lower', True, 'black')
        DISPLAYSURF.blit(self.text, (150, 345))
    def higher_btn(self,DISPLAYSURF):
        self.black_btnt = pygame.draw.rect(DISPLAYSURF, 'black', (550, 300, 300, 150), 0)
        self.smallfont = pygame.font.SysFont('Corbel', 65)
        self.text = self.smallfont.render('Higher', True, 'white')
        DISPLAYSURF.blit(self.text, (600, 335))
    def outside_btn(self,DISPLAYSURF):
        self.red_btnt = pygame.draw.rect(DISPLAYSURF, 'red', (100, 300, 300, 150), 0)
        self.smallfont = pygame.font.SysFont('Corbel', 65)
        self.text = self.smallfont.render('Outside', True, 'black')
        DISPLAYSURF.blit(self.text, (150, 345))
    def inbetween_btn(self,DISPLAYSURF):
        self.black_btnt = pygame.draw.rect(DISPLAYSURF, 'black', (550, 300, 300, 150), 0)
        self.smallfont = pygame.font.SysFont('Corbel', 65)
        self.text = self.smallfont.render('Inbetween', True, 'white')
        DISPLAYSURF.blit(self.text, (560, 335))

class Label:

    def start_label(self,DISPLAYSURF,table,set):
        placement = [0,50]
        placement2 = [700,50]
        counter = 1

        for card in table:
            identifer = card.split()
            self.smallfont = pygame.font.SysFont('Corbel', 35)
            if set == 0:
                if identifer[1] == 'Hearts' or identifer[1] == 'Diamonds':
                    self.text = self.smallfont.render(card, True, 'red')
                    DISPLAYSURF.blit(self.text, (placement[0], placement[1]))
                else:
                    self.text = self.smallfont.render(card, True, 'black')
                    DISPLAYSURF.blit(self.text, (placement[0],placement[1]))

                placement[0] += 200

            else:
                if identifer[1] == 'Hearts' or identifer[1] == 'Diamonds':
                    self.text = self.smallfont.render(card, True, 'red')
                    DISPLAYSURF.blit(self.text, (placement2[0], placement2[1]))
                else:
                    self.text = self.smallfont.render(card, True, 'black')
                    DISPLAYSURF.blit(self.text, (placement2[0],placement2[1]))

                placement2[0] -= 200

            if 'Diamonds' in card:
                if set == 0:
                    placement[0] += 50
                else:
                    placement2[0] -= 50

class Victory_Page:

    def show_page(self,DISPLAYSURF,decks):
        self.start_btn = pygame.draw.rect(DISPLAYSURF, 'lightgreen', (50, 25, 800, 200), 0)
        self.smallfont = pygame.font.SysFont('Corbel', 45)
        self.text = self.smallfont.render(f'You won Finally it took {decks} number of decks', True, 'black')
        DISPLAYSURF.blit(self.text, (80,100))

        self.red_btnt = pygame.draw.rect(DISPLAYSURF, 'red', (150, 300, 250, 150), 0)
        self.smallfont = pygame.font.SysFont('Corbel', 65)
        self.text = self.smallfont.render('Restart', True, 'black')
        DISPLAYSURF.blit(self.text, (180, 345))

        self.black_btnt = pygame.draw.rect(DISPLAYSURF, 'black', (600, 300, 200, 150), 0)
        self.smallfont = pygame.font.SysFont('Corbel', 65)
        self.text = self.smallfont.render('Quit', True, 'white')
        DISPLAYSURF.blit(self.text, (630, 335))
