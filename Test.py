'''############################LIBRARIES###############################'''

import sys
import time
import random
import pygame
sys.setrecursionlimit(1500)


pygame.init()
import random

clock=pygame.time.Clock()



'''############################COLORS###################################'''
white = [255, 255, 255]
red = [255, 0, 0]
bgold=[255,215,0]
gold=[218,165,32]
black=[0,0,0]
red = [255, 0, 0]

'''##########################IMAGES#####################################'''
background=pygame.image.load("12.jpg")
intro=pygame.image.load("123.jpg")
KS=pygame.image.load("KS.jpg")
QS=pygame.image.load("QS.jpg")
AcardS=pygame.image.load("AS.jpg")
JS=pygame.image.load("JS.jpg")
S2=pygame.image.load("2S.jpg")
S3=pygame.image.load("3S.jpg")
S4=pygame.image.load("4S.jpg")
S5=pygame.image.load("5S.jpg")
S6=pygame.image.load("6S.jpg")
S7=pygame.image.load("7S.jpg")
S8=pygame.image.load("8S.jpg")
S9=pygame.image.load("9S.jpg")
S10=pygame.image.load("10S.jpg")
KH=pygame.image.load("KH.jpg")
QH=pygame.image.load("QH.jpg")
AcardH=pygame.image.load("AH.jpg")
JH=pygame.image.load("JH.jpg")
H2=pygame.image.load("2H.jpg")
H3=pygame.image.load("3H.jpg")
H4=pygame.image.load("4H.jpg")
H5=pygame.image.load("5H.jpg")
H6=pygame.image.load("6H.jpg")
H7=pygame.image.load("7H.jpg")
H8=pygame.image.load("8H.jpg")
H9=pygame.image.load("9H.jpg")
H10=pygame.image.load("10H.jpg")
KD=pygame.image.load("KD.jpg")
QD=pygame.image.load("QD.jpg")
AcardD=pygame.image.load("AD.jpg")
JD=pygame.image.load("JD.jpg")
D2=pygame.image.load("2D.jpg")
D3=pygame.image.load("3D.jpg")
D4=pygame.image.load("4D.jpg")
D5=pygame.image.load("5D.jpg")
D6=pygame.image.load("6D.jpg")
D7=pygame.image.load("7D.jpg")
D8=pygame.image.load("8D.jpg")
D9=pygame.image.load("9D.jpg")
D10=pygame.image.load("10D.jpg")
KC=pygame.image.load("KC.jpg")
QC=pygame.image.load("QC.jpg")
AcardC=pygame.image.load("AC.jpg")
JC=pygame.image.load("JC.jpg")
C2=pygame.image.load("2C.jpg")
C3=pygame.image.load("3C.jpg")
C4=pygame.image.load("4C.jpg")
C5=pygame.image.load("5C.jpg")
C6=pygame.image.load("6C.jpg")
C7=pygame.image.load("7C.jpg")
C8=pygame.image.load("8C.jpg")
C9=pygame.image.load("9C.jpg")
C10=pygame.image.load("10C.jpg")


'''########################GRAPHICS DISPLAY PARTS#######################'''
 
H=1200
W=658
screen=pygame.display.set_mode(size=(H ,W))
mouse=pygame.mouse.get_pos()
pygame.display.set_caption("BLACK JACK")



'''##########################DRAW TEXT FUNCTIONS########################'''
def T_obj(text,font):
        t_surface= font.render(text,True,gold)
        return t_surface, t_surface.get_rect()

def T_obj_Button(text,font):
        t_surface= font.render(text,True,bgold)
        return t_surface, t_surface.get_rect()
    
def Display_message(text,x,y):
        T_text=pygame.font.SysFont('bodonicondensed', 50, True, True)
        T_Surface,T_rect=T_obj(text,T_text)
        T_rect.center=(x,y)
        screen.blit(T_Surface,T_rect)
        
        pygame.display.update()
        #time.sleep(5)
        #pygame.quit()
def imag(img,x,y):
    screen.blit(img,(x,y))
def tex(count):
    font = pygame.font.SysFont('bodonicondensed', 50)
    text = font.render("Player Score: "+str(count), True, gold)
    screen.blit(text,(30,400))
def texD(count):
    font = pygame.font.SysFont('bodonicondensed', 50)
    text = font.render("Dealer Score: "+str(count), True, gold)
    screen.blit(text,(30,500))
def texa(x,y):
    pygame.draw.rect(screen, black,(x,y,50,50))


        
'''##########################BUTTON FUNC##############################'''
def button_func(type,x,y,w,h,action=None,action2=None):
    pygame.draw.rect(screen, black,(x,y,w,h))
    mouse=pygame.mouse.get_pos() 
    click=pygame.mouse.get_pressed()
    T_text=pygame.font.SysFont('bodonicondensed', 50, True, True)
    if(x+w > mouse[0] > x and y+h > mouse[1]>y):
        T_Surface,T_rect=T_obj_Button(type,T_text)
        if(click[0] == 1 and action != None ):
            action()
            if(action2 != None):
                action2()
    else:
        T_Surface,T_rect=T_obj(type,T_text)
    T_rect.center=(x+(w/2)),(y+(h/2))
    screen.blit(T_Surface,T_rect)
    
    
'''###############################INTRO###############################''' 
def Game_Start():
    start=True
    
    while(start==True):
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                start=False
                pygame.quit()
                quit()
        
        screen.blit(intro,(0,0))
        T_text=pygame.font.SysFont('bodonicondensed', 60, True, True)
        T_Surface,T_rect=T_obj("BLACK JACK",T_text)
        T_rect.center=(150,60)
        screen.blit(T_Surface,T_rect)
        
        pygame.draw.rect(screen, black,(30,120,100,50))
        button_func("PLAY", 30, 150, 100, 50,gameloop)
        
        pygame.draw.rect(screen,black,(30,210,100,50))
        button_func("QUIT", 30, 240, 100, 50,quit_game)
        
        pygame.display.update()
        clock.tick(60)
        
        
def quit_game():
    pygame.quit
    quit()
    
    
'''##############################CLASSES##############################'''

'''###############################CARD################################'''
class Cards:
    def __init__(self):
        self.Deck=['AS','KS','QS','JS','2S','3S','4S','5S','6S','7S','8S','9S','10S',
                   'AC','KC','QC','JC','2C','3C','4C','5C','6C','7C','8C','9C','10C',
                   'AH','KH','QH','JH','2H','3H','4H','5H','6H','7H','8H','9H','10H',
                   'AD','KD','QD','JD','2D','3D','4D','5D','6D','7D','8D','9D','10D',]
    def shuffle(self):
        random.shuffle(self.Deck)
    def Draw_Card(self):
        random.shuffle(self.Deck)
        card=self.Deck.pop(0)
        return(card)
    def print_deck(self):
        return("RED")
        
'''#############################PLAYER#################################'''
class Player:
    def __init__(self):
        self.Pscore=0
        self.PCard_obj=Cards()
    def stay(self):
        self.score_check()
        print(self.Pscore)
    def player_score(self):
        texa(215,399)
        card=self.PCard_obj.Draw_Card()
        if((card=='KS' or card=='KC' or card=='KD' or card=='KH')):
            self.Pscore=self.Pscore+10
            tex(self.Pscore)
            if(card=='KS'):
                screen.blit(KS,(400,60))
                pygame.display.update()
            elif(card=='KC'):
                screen.blit(KC,(400,60))
                pygame.display.update()
            elif(card=='KH'):
                screen.blit(KH,(400,60))
                pygame.display.update()
            elif(card=='KD'):
                screen.blit(KD,(400,60))
                pygame.display.update()
            pygame.display.update()
        elif(card=='QS' or card=='QC' or card=='QD' or card=='QH'):
            self.Pscore=self.Pscore+10
            tex(self.Pscore)
            if(card=='QS'):
                screen.blit(QS,(400,60))
                pygame.display.update()
            elif(card=='QC'):
                screen.blit(QC,(400,60))
                pygame.display.update()
            elif(card=='QH'):
                screen.blit(QH,(400,60))
                pygame.display.update()
            elif(card=='QD'):
                screen.blit(QD,(400,60))
                pygame.display.update()
            pygame.display.update()
        elif(card=='JS' or card=='JC' or card=='JD' or card=='JH'):
            self.Pscore=self.Pscore+10
            tex(self.Pscore)
            if(card=='JS'):
                screen.blit(JS,(400,60))
                pygame.display.update()
            elif(card=='JC'):
                screen.blit(JC,(400,60))
                pygame.display.update()
            elif(card=='JH'):
                screen.blit(JH,(400,60))
                pygame.display.update()
            elif(card=='JD'):
                screen.blit(JD,(400,60))
                pygame.display.update()
            pygame.display.update()
        elif(card=='AS' or card=='AC' or card=='AD' or card=='AH'):
            if(self.Pscore<=10):
                self.Pscore=self.Pscore+10
                tex(self.Pscore)
            else:
                self.Pscore=self.Pscore+1
                tex(self.Pscore)
            if(card=='AcardS'):
                screen.blit(AcardS,(400,60))
                pygame.display.update()
            elif(card=='AcardC'):
                screen.blit(AcardC,(400,60))
                pygame.display.update()
            elif(card=='AcardH'):
                screen.blit(AcardH,(400,60))
                pygame.display.update()
            elif(card=='AcardD'):
                screen.blit(AcardD,(400,60))
                pygame.display.update()
            pygame.display.update()
        elif(card=='10S' or card=='10C' or card=='10D' or card=='10H'):
            self.Pscore=self.Pscore+10
            tex(self.Pscore)
            if(card=='10S'):
                screen.blit(S10,(400,60))
                pygame.display.update()
            elif(card=='10C'):
                screen.blit(C10,(400,60))
                pygame.display.update()
            elif(card=='10H'):
                screen.blit(H10,(400,60))
                pygame.display.update()
            elif(card=='10D'):
                screen.blit(D10,(400,60))
                pygame.display.update()
            pygame.display.update()
        elif(card=='9S' or card=='9C' or card=='9D' or card=='9H'):
            self.Pscore=self.Pscore+9
            tex(self.Pscore)
            if(card=='9S'):
                screen.blit(S9,(400,60))
                pygame.display.update()
            elif(card=='9C'):
                screen.blit(C9,(400,60))
                pygame.display.update()
            elif(card=='9H'):
                screen.blit(H9,(400,60))
                pygame.display.update()
            elif(card=='9D'):
                screen.blit(D9,(400,60))
                pygame.display.update()
            pygame.display.update()
        elif(card=='8S' or card=='8C' or card=='8D' or card=='8H'):
            self.Pscore=self.Pscore+8
            tex(self.Pscore)
            if(card=='8S'):
                screen.blit(S8,(400,60))
                pygame.display.update()
            elif(card=='8C'):
                screen.blit(C8,(400,60))
                pygame.display.update()
            elif(card=='8H'):
                screen.blit(H8,(400,60))
                pygame.display.update()
            elif(card=='8D'):
                screen.blit(D8,(400,60))
                pygame.display.update()
            pygame.display.update()
        elif(card=='7S' or card=='7C' or card=='7D' or card=='7H'):
            self.Pscore=self.Pscore+7
            tex(self.Pscore)
            if(card=='7S'):
                screen.blit(S7,(400,60))
                pygame.display.update()
            elif(card=='7C'):
                screen.blit(C7,(400,60))
                pygame.display.update()
            elif(card=='7H'):
                screen.blit(H7,(400,60))
                pygame.display.update()
            elif(card=='7D'):
                screen.blit(D7,(400,60))
                pygame.display.update()
            pygame.display.update()
        elif(card=='6S' or card=='6C' or card=='6D' or card=='6H'):
            self.Pscore=self.Pscore+6
            tex(self.Pscore)
            if(card=='6S'):
                screen.blit(S6,(400,60))
                pygame.display.update()
            elif(card=='6C'):
                screen.blit(C6,(400,60))
                pygame.display.update()
            elif(card=='6H'):
                screen.blit(H6,(400,60))
                pygame.display.update()
            elif(card=='6D'):
                screen.blit(D6,(400,60))
                pygame.display.update()
            pygame.display.update()
        elif(card=='5S' or card=='5C' or card=='5D' or card=='5H'):
            self.Pscore=self.Pscore+5
            tex(self.Pscore)
            if(card=='5S'):
                screen.blit(S5,(400,60))
                pygame.display.update()
            elif(card=='5C'):
                screen.blit(C5,(400,60))
                pygame.display.update()
            elif(card=='5H'):
                screen.blit(H5,(400,60))
                pygame.display.update()
            elif(card=='5D'):
                screen.blit(D5,(400,60))
                pygame.display.update()
            pygame.display.update()
        elif(card=='4S' or card=='4C' or card=='4D' or card=='4H'):
            self.Pscore=self.Pscore+4
            tex(self.Pscore)
            if(card=='4S'):
                screen.blit(S4,(400,60))
                pygame.display.update()
            elif(card=='4C'):
                screen.blit(C4,(400,60))
                pygame.display.update()
            elif(card=='4H'):
                screen.blit(H4,(400,60))
                pygame.display.update()
            elif(card=='4D'):
                screen.blit(D4,(400,60))
                pygame.display.update()
            pygame.display.update()
        elif(card=='3S' or card=='3C' or card=='3D' or card=='3H'):
            self.Pscore=self.Pscore+3
            tex(self.Pscore)
            if(card=='3S'):
                screen.blit(S3,(400,60))
                pygame.display.update()
            elif(card=='3C'):
                screen.blit(C3,(400,60))
                pygame.display.update()
            elif(card=='3H'):
                screen.blit(H3,(400,60))
                pygame.display.update()
            elif(card=='3D'):
                screen.blit(D3,(400,60))
                pygame.display.update()
            pygame.display.update()
        elif(card=='2S' or card=='2C' or card=='2D' or card=='2H'):
            self.Pscore=self.Pscore+2
            tex(self.Pscore) 
            if(card=='2S'):
                screen.blit(S2,(400,60))
                pygame.display.update()
            elif(card=='2C'):
                screen.blit(C2,(400,60))
                pygame.display.update()
            elif(card=='2H'):
                screen.blit(H2,(400,60))
                pygame.display.update()
            elif(card=='2D'):
                screen.blit(D2,(400,60))
                pygame.display.update()
            pygame.display.update()      
            
    def score_check(self):
        playerscore=self.Pscore
        self.D_obj=Dealer()
        if(self.Pscore>21):
            Display_message("BUSTED", 365, 350)
            pygame.display.update()
        elif(self.Pscore==21):
            Display_message("YOU GOT A BLACKJACK!!", 365, 350)
            pygame.display.update()
        

'''############################DEALER##################################'''

class Dealer:
    global dealerscore
    def __init__(self):
        self.Card_obj=Cards()
        self.player_obj=Player()
        self.Dscore=0
    def shuffle_cards(self):
        self.Card_obj.shuffle()
        self.Card_obj.print_deck()
    '''####################DEALER HIT#####################################'''
    def dealer_score(self):
        texa(215,517)
        card=self.Card_obj.Draw_Card()
        print(card)
        if(card=='KS' or card=='KC' or card=='KD' or card=='KH'):
            self.Dscore= self.Dscore+10
        elif(card=='QS' or card=='QC' or card=='QD' or card=='QH'):
            self.Dscore= self.Dscore+10
        elif(card=='JS' or card=='JC' or card=='JD' or card=='JH'):
            self.Dscore= self.Dscore+10
        elif(card=='AS' or card=='AC' or card=='AD' or card=='AH'):
            if(self.Dscore<=10):
                self.Dscore= self.Dscore+11
            else:
                self.Dscore+1
        elif(card=='2S' or card=='2C' or card=='2D' or card=='2H'):
            self.Dscore= self.Dscore+2
        elif(card=='3S' or card=='3C' or card=='3D' or card=='3H'):
            self.Dscore= self.Dscore+3
        elif(card=='4S' or card=='4C' or card=='4D' or card=='4H'):
            self.Dscore= self.Dscore+4
        elif(card=='5S' or card=='5C' or card=='5D' or card=='5H'):
            self.Dscore= self.Dscore+4
        elif(card=='6S' or card=='6C' or card=='6D' or card=='6H'):
            self.Dscore= self.Dscore+6
        elif(card=='7S' or card=='7C' or card=='7D' or card=='7H'):
            self.Dscore= self.Dscore+7
        elif(card=='8S' or card=='8C' or card=='8D' or card=='8H'):
            self.Dscore= self.Dscore+8
        elif(card=='9S' or card=='9C' or card=='9D' or card=='9H'):
            self.Dscore= self.Dscore+9
        elif(card=='10S' or card=='10C' or card=='10D' or card=='10H'):
            self.Dscore= self.Dscore+10

    def score_D_check(self):
        dealerscore=self.Dscore
        if(self.Dscore<17):
            self.dealer_score()
        elif(self.Dscore>=17):
            print("")
    def print_D_score(self):
        texD(self.Dscore)
        
        
'''###############################MAIN#################################'''

def gameloop():
    def main():
        
        count=0
        
        '''OBJECTS'''
        P=Player()
        C1=Cards()
        D=Dealer()  
        
        
        runing=True
        
        while (runing):
            for event in pygame.event.get():
                if(event.type==pygame.QUIT):
                    pygame.quit
                    quit
                    runing=False
            print(mouse)
            
            if(count==0):
                screen.blit(background,(0,0))
                P.player_score()
                D.dealer_score()
                count=count+1
            def equ():
                if(P.Pscore>21):
                    Display_message("BUSTED", 365, 350)
                    pygame.display.update()
                elif(P.Pscore==21):
                    Display_message("YOU GOT A BLACKJACK!!", 365, 350)
                    pygame.display.update()
                elif(D.Dscore>P.Pscore and D.Dscore <22):
                    Display_message("Dealer Won", 365, 350) 
                elif(D.Dscore==P.Pscore):
                    Display_message("Tied", 365, 350)
                else:
                    Display_message("Player Won", 365, 350)
                
                    
            Display_message("Your Card", 470, 30)
            button_func("HIT", 150, 60, 100, 50,P.player_score,D.score_D_check )
            button_func("SHUFFLE", 150, 180, 100, 50,C1.shuffle,None)
            button_func("STAY", 150, 120, 100, 50,equ,D.print_D_score)
            button_func("QUIT", 30, 600, 100, 50,quit_game)
            button_func("PLAY AGAIN", 200, 600, 100, 50, gameloop, None)
           
            
                
            pygame.display.update()
            clock.tick(7)
    if __name__=='__main__':
        main()
        
Game_Start()
pygame.quit()
quit()
    
   
        


    
    