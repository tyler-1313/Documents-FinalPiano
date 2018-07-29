import pygame

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
myfonttwo = pygame.font.SysFont('Comic Sans MS', 14)
MainMenu = myfont.render('MainMenu', False, (0, 0, 0))

Learn = myfont.render('Learn', False, (0, 0, 0))

Practice= myfont.render('Practice', False, (0, 0, 0))
Notes= myfont.render('Notes', False, (0, 0, 0))
NoteTypes= myfont.render('Note Types', False, (0, 0, 0))
NumberNotes= myfont.render('Number of Notes', False, (0, 0, 0))
Chords=myfont.render('Include Chords', False, (0, 0, 0))
TimeSig=myfont.render('Time Signature', False, (0, 0, 0))
BPM=myfont.render('Beats per Minute', False, (0, 0, 0))

PracticeIMG=pygame.image.load('Practice.png')
SongList=['FurElise.CSV', 'BachFile']
SongCoordList=[]

Library = myfont.render('Library', False, (0, 0, 0))
white=(255,255,255)
black=(0,0,0)
blue=(0,255,255)
darkblue=(0,0,255)
size=(1300,900)
screen=pygame.display.set_mode(size)

HandsIMG=pygame.image.load('white.png')
SixIMG=pygame.image.load('16thIMG.png')
EthIMG=pygame.image.load('EthIMG.png')
FourthIMG=pygame.image.load('4thIMG.png')
HalfIMG=pygame.image.load('HalfIMG.png')
WholeIMG=pygame.image.load('WholeIMG.png')
CheckMarkIMG=pygame.image.load('CheckMark.png')
colonIMG=pygame.image.load('colon.png')



                    
class Menu():
    def MainMenu(state):
        if state=='MMenu':
            screen.blit(HandsIMG, (0,0))
            screen.blit(MainMenu, (500,100))
            screen.blit(Learn, (300,200))
            screen.blit(Practice, (300,300))
            screen.blit(Library, (300,400))

    def Learn(state):
        if state=='Learn':
            screen.blit(HandsIMG, (0,0))
            screen.blit(Learn, (500, 100))
            
    def Practice(state, boxone,boxtwo,boxthree,boxfour,boxfive, chordbox):
        if state=='Practice':
            screen.blit(HandsIMG, (0,0))
            screen.blit(Practice, (500, 100))
            
            screen.blit(Notes, (200, 150))
            pygame.draw.rect(screen, black, (300, 160, 30, 28), 1)
            pygame.draw.rect(screen, black, (350, 160, 30, 28), 1)
            
            screen.blit(NoteTypes, (200, 210))
            screen.blit(WholeIMG, (400, 220))
            screen.blit(HalfIMG, (440, 190))
            screen.blit(FourthIMG, (480, 190))
            screen.blit(EthIMG, (520, 190))
            screen.blit(SixIMG, (560, 190))
            g=0
            while g<5:
                pygame.draw.rect(screen, black, (410+g*38, 248, 10, 10), 1)
                g+=1
                
            screen.blit(NumberNotes, (200, 270))
            pygame.draw.rect(screen, black, (450, 277, 43, 28),1)
            pygame.draw.line(screen, black, (335, 174), (345, 174), 1)

            screen.blit(Chords, (200, 330))
            pygame.draw.rect(screen, black, (420, 348, 10, 10),1)

            pygame.draw.rect(screen, black, (600, 500, 40, 40),1)
            if chordbox==True:
                screen.blit(CheckMarkIMG, (420, 338))
            if boxone==True:
                screen.blit(CheckMarkIMG, (410, 239))
            if boxtwo==True:
                screen.blit(CheckMarkIMG, (448, 239))
            if boxthree==True:
                screen.blit(CheckMarkIMG, (486, 239))
            if boxfour==True:
                screen.blit(CheckMarkIMG, (524, 239))
            if boxfive==True:
                screen.blit(CheckMarkIMG, (562, 239))
            screen.blit(TimeSig, (200, 390))
            pygame.draw.rect(screen, black, (430, 400, 30, 30),1)
            screen.blit(colonIMG, (463, 404))
            screen.blit(BPM, (200, 445))
            pygame.draw.rect(screen, black, (450, 455, 45, 30),1)
    def SettoFalse(keep, turn, turntwo, turnthree, turnfour, turnfive):
        if keep==True:
            keep=False
        else:
            keep=True
        turn=False
        turntwo=False
        turnthree=False
        turnfour=False
        turnfive=False
        return(keep, turn, turntwo, turnthree, turnfour, turnfive)
    def Library(state):
        if state=='Library':
           screen.blit(Library, (500, 100))
           g=0
           for a in SongList:
               Song = myfonttwo.render(str(a), False, (0, 0, 0))
               x=100; y=150+15*g
               screen.blit(Song, (x,y))
               SongCoordList.append(list((x,y)))
               g+=1
