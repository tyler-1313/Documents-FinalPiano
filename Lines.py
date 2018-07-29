import pygame
MeasEnder={'SixteenthNote':'1', 'SixteenthNotePlus':'1.5', 'EthNote':'2', 'EthNotePlus':'3', 'FourthNote':'4',
           'FourthNotePlus':'6', 'HalfNote':'8', 'HalfNotePlus':'12', 'WholeNote':'16'}
EthNoteTailIMG=pygame.image.load('EthTail.png')
RevEthNoteTailIMG=pygame.image.load('RevEthTail.png')
BlueEthNoteTailIMG=pygame.image.load('BlueEthTail.png')
RevBlueEthNoteTailIMG=pygame.image.load('RevBlueEthTail.png')
white=(255,255,255)
black=(0,0,0)
blue=(0,255,255)
darkblue=(0,0,255)
size=(1300,900)
screen=pygame.display.set_mode(size)
class Lines():
    def SingleNotesR(RCoord, RList, color, TS):
        p=-1
        m=0
        time=16*(int(TS[0])/int(TS[1]))
        for a in RCoord:  # Draw Lines on Notes for 16th-half notes
            p+=1
            m+=int(MeasEnder[RList[p][0]])
            if m==time:
                m=0
            if m==0:  #last
                if RList[p][0]!=RList[p-1][0] or RList[p-1][1]==89:
                    if RList[p][0]=='SixteenthNote' or RList[p][0]=='SixteenthNotePlus':
                        if isinstance(RList[p][1], int):
                            if 89>RList[p][1]>62: #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+1, RCoord[p][1]+5), (RCoord[p][0]+1, 62)) #x+1
                                if color==black:
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+2, 50))
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+2, 46))
                                else:
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+2, 50))
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+2, 46))
                            elif 62>=RList[p][1]>50: #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+1, RCoord[p][1]+4), (RCoord[p][0]+1, RCoord[p][1]+25))#y, y+21
                                if color==black:
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+1, RCoord[p][1]+21))
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+1, RCoord[p][1]+17))
                                else:
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+1, RCoord[p][1]+21))
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+1, RCoord[p][1]+17))
                            elif 50>=RList[p][1]: #up
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, RCoord[p][1]+1), (RCoord[p][0]+9, RCoord[p][1]-20))
                                if color==black:
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+9, RCoord[p][1]-24))
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+9, RCoord[p][1]-20))
                                else:
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+9, RCoord[p][1]-24))
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+9, RCoord[p][1]-20))
                        else: #RList[p][1] = chord
                            high=RCoord[p][1][0]
                            low=RCoord[p][1][0]
                            highs=RList[p][1][0]
                            lows=RList[p][1][0]
                            for a in RCoord[p][1]:
                                if a>high:
                                    high=a
                                if a<low:
                                    low=a
                            for a in RList[p][1]:
                                if a>highs:
                                    highs=a
                                if a<lows:
                                    lows=a
                            ## high, low = y coords
                            if lows>62 or (highs>62 and lows<=62): #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+1, low+5), (RCoord[p][0]+1, high+27))
                                if color==black:
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+2, high+15))
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+2, high+11))
                                else:
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+2, high+15))
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+2, high+11))
                            elif highs<=50 or (lows<=50 and highs>50): #up
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, high), (RCoord[p][0]+9, high-20))
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, low), (RCoord[p][0]+9, high))
                                if color==black:
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+9, high-24))
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+9, high-20))
                                else:
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+9, high-24))
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+9, high-20))
                                
                            else: #down
                                
                                pygame.draw.line(screen, color, (RCoord[p][0]+10, high+3), (RCoord[p][0]+10, low-21))
                                if color==black:
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+10, low-23))
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+10, low-19))
                                else:
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+10, low-23))
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+10, low-19))                               
                            
                    elif RList[p][0]=='EthNote' or RList[p][0]=='EthNotePlus':
                        if isinstance(RList[p][1], int):
                            if 89>RList[p][1]>62: #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+1, RCoord[p][1]+5), (RCoord[p][0]+1, 62))
                                if color==black:
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+2, 50))
                                else:
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+2, 50))
                            elif 62>=RList[p][1]>50: #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+1, RCoord[p][1]+4), (RCoord[p][0]+1, RCoord[p][1]+26))
                                if color==black:
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+1, RCoord[p][1]+15))
                                else:
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+1, RCoord[p][1]+15))
                            elif 50>=RList[p][1]: #up
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, RCoord[p][1]+1), (RCoord[p][0]+9, RCoord[p][1]-20))
                                if color==black:
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+9, RCoord[p][1]-24))
                                else:
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+9, RCoord[p][1]-24))
                        else: #RList[p][1] = chord
                            high=RCoord[p][1][0]
                            low=RCoord[p][1][0]
                            highs=RList[p][1][0]
                            lows=RList[p][1][0]
                            for a in RCoord[p][1]:
                                if a>high:
                                    high=a
                                if a<low:
                                    low=a
                            for a in RList[p][1]:
                                if a>highs:
                                    highs=a
                                if a<lows:
                                    lows=a
                            ## high, low = y coords
                            
                            if lows>62 or (highs>62 and lows<=62): #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+1, low+4), (RCoord[p][0]+1, high+21)) #low + 5
                                if color==black:
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+2, high+11))
                                else:
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+2, high+11))
                            elif highs<=50 or (lows<=50 and highs>50): #up
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, high), (RCoord[p][0]+9, high-20))
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, low), (RCoord[p][0]+9, high))
                                if color==black:
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+9, high-24))
                                else:
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+9, high-24))
                                
                            else: #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+10, high+2), (RCoord[p][0]+10, low-21))
                                if color==black:
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+10, low-23))
                                else:
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+10, low-23))
                    elif RList[p][0]=='FourthNote' or RList[p][0]=='HalfNote' or RList[p][0]=='HalfNotePlus' or RList[p][0]=='FourthNotePlus':
                        if isinstance(RList[p][1], int):
                            if 89>RList[p][1]>62: #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+1, RCoord[p][1]+5), (RCoord[p][0]+1, 62))
                            elif 62>=RList[p][1]>50: #down
                                pygame.draw.line(screen, color, (RCoord[p][0], RCoord[p][1]), (RCoord[p][0], RCoord[p][1]+21))
                            elif 50>=RList[p][1]: #up
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, RCoord[p][1]+1), (RCoord[p][0]+9, RCoord[p][1]-20))
                        else: #RList[p][1] = chord
                            high=RCoord[p][1][0]
                            low=RCoord[p][1][0]
                            highs=RList[p][1][0]
                            lows=RList[p][1][0]
                            for a in RCoord[p][1]:   #high, low=RCoord   highs, lows=RList
                                if a>high:
                                    high=a
                                if a<low:
                                    low=a
                            for a in RList[p][1]:
                                if a>highs:
                                    highs=a
                                if a<lows:
                                    lows=a
                                
                            ## high, low = y coords
                            if lows>62 or (highs>62 and lows<=62): #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+1, low+4), (RCoord[p][0]+1, high+21))                               
                            elif highs<=50 or (lows<=50 and highs>50): #up
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, high), (RCoord[p][0]+9, high-20))
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, low), (RCoord[p][0]+9, high))
                            else: #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+10, low-21), (RCoord[p][0]+10, high+3))

            elif p>=len(RList)-1:
                pass
            elif p==0 or m==int(MeasEnder[RList[p][0]]):  #first
                if RList[p][0]!=RList[p+1][0] or RList[p+1][1]==89:
                    if RList[p][0]=='SixteenthNote' or RList[p][0]=='SixteenthNotePlus':
                        if isinstance(RList[p][1], int):
                            if 89>RList[p][1]>62: #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+1, RCoord[p][1]+5), (RCoord[p][0]+1, 62))
                                if color==black:
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+2, 50))
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+2, 46))
                                else:
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+2, 50))
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+2, 46))
                            elif 62>=RList[p][1]>50: #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+1, RCoord[p][1]+4), (RCoord[p][0]+1, RCoord[p][1]+25))#y, y+21
                                if color==black:
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+1, RCoord[p][1]+21))
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+1, RCoord[p][1]+17))
                                else:
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+1, RCoord[p][1]+21))
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+1, RCoord[p][1]+17))
                            elif 50>=RList[p][1]: #up
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, RCoord[p][1]+1), (RCoord[p][0]+9, RCoord[p][1]-20))
                                if color==black:
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+9, RCoord[p][1]-24))
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+9, RCoord[p][1]-20))
                                else:
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+9, RCoord[p][1]-24))
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+9, RCoord[p][1]-20))
                        else: #RList[p][1] = chord
                            high=RCoord[p][1][0]
                            low=RCoord[p][1][0]
                            highs=RList[p][1][0]
                            lows=RList[p][1][0]
                            for a in RCoord[p][1]:
                                if a>high:
                                    high=a
                                if a<low:
                                    low=a
                            for a in RList[p][1]:
                                if a>highs:
                                    highs=a
                                if a<lows:
                                    lows=a
                            ## high, low = y coords
                            if lows>62 or (highs>62 and lows<=62): #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+1, low+5), (RCoord[p][0]+1, high+27))
                                if color==black:
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+2, high+15))
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+2, high+11))
                                else:
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+2, high+15))
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+2, high+11))
                            elif highs<=50 or (lows<=50 and highs>50): #up
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, high), (RCoord[p][0]+9, high-20))
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, low), (RCoord[p][0]+9, high))
                                if color==black:
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+9, high-24))
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+9, high-20))
                                else:
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+9, high-24))
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+9, high-20))
                                
                            else: #down
                                
                                pygame.draw.line(screen, color, (RCoord[p][0]+10, high+3), (RCoord[p][0]+10, low-21))
                                if color==black:
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+10, low-23))
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+10, low-19))
                                else:
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+10, low-23))
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+10, low-19))                               
                            
                    elif RList[p][0]=='EthNote' or RList[p][0]=='EthNotePlus':
                        if isinstance(RList[p][1], int):
                            if 89>RList[p][1]>62: #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+1, RCoord[p][1]+5), (RCoord[p][0]+1, 62))
                                if color==black:
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+2, 50))
                                else:
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+2, 50))
                            elif 62>=RList[p][1]>50: #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+1, RCoord[p][1]+4), (RCoord[p][0]+1, RCoord[p][1]+26))
                                if color==black:
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+1, RCoord[p][1]+15))
                                else:
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+1, RCoord[p][1]+15))
                            elif 50>=RList[p][1]: #up
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, RCoord[p][1]+1), (RCoord[p][0]+9, RCoord[p][1]-20))
                                if color==black:
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+9, RCoord[p][1]-24))
                                else:
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+9, RCoord[p][1]-24))
                        else: #RList[p][1] = chord
                            high=RCoord[p][1][0]
                            low=RCoord[p][1][0]
                            highs=RList[p][1][0]
                            lows=RList[p][1][0]
                            for a in RCoord[p][1]:
                                if a>high:
                                    high=a
                                if a<low:
                                    low=a
                            for a in RList[p][1]:
                                if a>highs:
                                    highs=a
                                if a<lows:
                                    lows=a
                            ## high, low = y coords
                            
                            if lows>62 or (highs>62 and lows<=62): #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+1, low+4), (RCoord[p][0]+1, high+21)) #low + 5
                                if color==black:
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+2, high+11))
                                else:
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+2, high+11))
                            elif highs<=50 or (lows<=50 and highs>50): #up
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, high), (RCoord[p][0]+9, high-20))
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, low), (RCoord[p][0]+9, high))
                                if color==black:
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+9, high-24))
                                else:
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+9, high-24))
                                
                            else: #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+10, high+2), (RCoord[p][0]+10, low-21))
                                if color==black:
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+10, low-23))
                                else:
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+10, low-23))
                    elif RList[p][0]=='FourthNote' or RList[p][0]=='HalfNote' or RList[p][0]=='HalfNotePlus' or RList[p][0]=='FourthNotePlus':
                        if isinstance(RList[p][1], int):
                            if 89>RList[p][1]>62: #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+1, RCoord[p][1]+5), (RCoord[p][0]+1, 62))
                            elif 62>=RList[p][1]>50: #down
                                pygame.draw.line(screen, color, (RCoord[p][0], RCoord[p][1]), (RCoord[p][0], RCoord[p][1]+21))
                            elif 50>=RList[p][1]: #up
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, RCoord[p][1]+1), (RCoord[p][0]+9, RCoord[p][1]-20))
                        else: #RList[p][1] = chord
                            high=RCoord[p][1][0]
                            low=RCoord[p][1][0]
                            highs=RList[p][1][0]
                            lows=RList[p][1][0]
                            for a in RCoord[p][1]:   #high, low=RCoord   highs, lows=RList
                                if a>high:
                                    high=a
                                if a<low:
                                    low=a
                            for a in RList[p][1]:
                                if a>highs:
                                    highs=a
                                if a<lows:
                                    lows=a
                                
                            ## high, low = y coords
                            if lows>62 or (highs>62 and lows<=62): #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+1, low+4), (RCoord[p][0]+1, high+21))                               
                            elif highs<=50 or (lows<=50 and highs>50): #up
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, high), (RCoord[p][0]+9, high-20))
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, low), (RCoord[p][0]+9, high))
                            else: #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+10, low-21), (RCoord[p][0]+10, high+3))
            else:  #mid
                if (RList[p][0]!=RList[p-1][0] or RList[p-1][1]==89) and (RList[p][0]!=RList[p+1][0] or RList[p+1][1]==89):
                    if RList[p][0]=='SixteenthNote' or RList[p][0]=='SixteenthNotePlus':
                        if isinstance(RList[p][1], int):
                            if 89>RList[p][1]>62: #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+1, RCoord[p][1]+5), (RCoord[p][0]+1, 62))
                                if color==black:
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+2, 50))
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+2, 46))
                                else:
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+2, 50))
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+2, 46))
                            elif 62>=RList[p][1]>50: #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+1, RCoord[p][1]+4), (RCoord[p][0]+1, RCoord[p][1]+25))#y, y+21
                                if color==black:
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+1, RCoord[p][1]+21))
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+1, RCoord[p][1]+17))
                                else:
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+1, RCoord[p][1]+21))
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+1, RCoord[p][1]+17))
                            elif 50>=RList[p][1]: #up
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, RCoord[p][1]+1), (RCoord[p][0]+9, RCoord[p][1]-20))
                                if color==black:
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+9, RCoord[p][1]-24))
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+9, RCoord[p][1]-20))
                                else:
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+9, RCoord[p][1]-24))
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+9, RCoord[p][1]-20))
                        else: #RList[p][1] = chord
                            high=RCoord[p][1][0]
                            low=RCoord[p][1][0]
                            highs=RList[p][1][0]
                            lows=RList[p][1][0]
                            for a in RCoord[p][1]:
                                if a>high:
                                    high=a
                                if a<low:
                                    low=a
                            for a in RList[p][1]:
                                if a>highs:
                                    highs=a
                                if a<lows:
                                    lows=a
                            ## high, low = y coords
                            if lows>62 or (highs>62 and lows<=62): #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+1, low+5), (RCoord[p][0]+1, high+27))
                                if color==black:
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+2, high+15))
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+2, high+11))
                                else:
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+2, high+15))
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+2, high+11))
                            elif highs<=50 or (lows<=50 and highs>50): #up
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, high), (RCoord[p][0]+9, high-20))
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, low), (RCoord[p][0]+9, high))
                                if color==black:
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+9, high-24))
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+9, high-20))
                                else:
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+9, high-24))
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+9, high-20))
                                
                            else: #down
                                
                                pygame.draw.line(screen, color, (RCoord[p][0]+10, high+3), (RCoord[p][0]+10, low-21))
                                if color==black:
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+10, low-23))
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+10, low-19))
                                else:
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+10, low-23))
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+10, low-19))                               
                            
                    elif RList[p][0]=='EthNote' or RList[p][0]=='EthNotePlus':
                        if isinstance(RList[p][1], int):
                            if 89>RList[p][1]>62: #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+1, RCoord[p][1]+5), (RCoord[p][0]+1, 62))
                                if color==black:
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+2, 50))
                                else:
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+2, 50))
                            elif 62>=RList[p][1]>50: #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+1, RCoord[p][1]+4), (RCoord[p][0]+1, RCoord[p][1]+26))
                                if color==black:
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+1, RCoord[p][1]+15))
                                else:
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+1, RCoord[p][1]+15))
                            elif 50>=RList[p][1]: #up
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, RCoord[p][1]+1), (RCoord[p][0]+9, RCoord[p][1]-20))
                                if color==black:
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+9, RCoord[p][1]-24))
                                else:
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+9, RCoord[p][1]-24))
                        else: #RList[p][1] = chord
                            high=RCoord[p][1][0]
                            low=RCoord[p][1][0]
                            highs=RList[p][1][0]
                            lows=RList[p][1][0]
                            for a in RCoord[p][1]:
                                if a>high:
                                    high=a
                                if a<low:
                                    low=a
                            for a in RList[p][1]:
                                if a>highs:
                                    highs=a
                                if a<lows:
                                    lows=a
                            ## high, low = y coords
                            
                            if lows>62 or (highs>62 and lows<=62): #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+1, low+4), (RCoord[p][0]+1, high+21)) #low + 5
                                if color==black:
                                    screen.blit(RevEthNoteTailIMG, (RCoord[p][0]+2, high+11))
                                else:
                                    screen.blit(RevBlueEthNoteTailIMG, (RCoord[p][0]+2, high+11))
                            elif highs<=50 or (lows<=50 and highs>50): #up
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, high), (RCoord[p][0]+9, high-20))
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, low), (RCoord[p][0]+9, high))
                                if color==black:
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+9, high-24))
                                else:
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+9, high-24))
                                
                            else: #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+10, high+2), (RCoord[p][0]+10, low-21))
                                if color==black:
                                    screen.blit(EthNoteTailIMG, (RCoord[p][0]+10, low-23))
                                else:
                                    screen.blit(BlueEthNoteTailIMG, (RCoord[p][0]+10, low-23))
                    elif RList[p][0]=='FourthNote' or RList[p][0]=='HalfNote' or RList[p][0]=='HalfNotePlus' or RList[p][0]=='FourthNotePlus':
                        if isinstance(RList[p][1], int):
                            if 89>RList[p][1]>62: #down  
                                pygame.draw.line(screen, color, (RCoord[p][0]+1, RCoord[p][1]+5), (RCoord[p][0]+1, 62))
                            elif 62>=RList[p][1]>50: #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+1, RCoord[p][1]+3), (RCoord[p][0]+1, RCoord[p][1]+24))
                            elif 50>=RList[p][1]: #up
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, RCoord[p][1]+1), (RCoord[p][0]+9, RCoord[p][1]-20))
                        else: #RList[p][1] = chord
                            high=RCoord[p][1][0]
                            low=RCoord[p][1][0]
                            highs=RList[p][1][0]
                            lows=RList[p][1][0]
                            for a in RCoord[p][1]:   #high, low=RCoord   highs, lows=RList
                                if a>high:
                                    high=a
                                if a<low:
                                    low=a
                            for a in RList[p][1]:
                                if a>highs:
                                    highs=a
                                if a<lows:
                                    lows=a
                                
                            ## high, low = y coords
                            if lows>62 or (highs>62 and lows<=62): #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+1, low+4), (RCoord[p][0]+1, high+21))                               
                            elif highs<=50 or (lows<=50 and highs>50): #up
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, high), (RCoord[p][0]+9, high-20))
                                pygame.draw.line(screen, color, (RCoord[p][0]+9, low), (RCoord[p][0]+9, high))
                            else: #down
                                pygame.draw.line(screen, color, (RCoord[p][0]+10, low-21), (RCoord[p][0]+10, high+3))
 
 
    def SingleNotesL(LCoord, LList, color, TS):
        p=-1
        m=0
        time=16*(int(TS[0])/int(TS[1]))
        
        for a in LCoord:  # Draw Lines on Notes for 16th-half notes
            p+=1
            if LList[p][1]!=0:
                m+=int(MeasEnder[LList[p][0]])
                if m==time:
                    m=0
                if m==0:
                    if LList[p][0]!=LList[p-1][0] or LList[p-1][1]==0:   #last 16, 8, 
                        if LList[p][0]=='SixteenthNote' or LList[p][0]=='SixteenthNotePlus':
                            if isinstance(LList[p][1], int):
                                if LList[p][1]>31:
                                    pygame.draw.line(screen, color, (LCoord[p][0]+1,LCoord[p][1]+5), (LCoord[p][0]+1, LCoord[p][1]+26))
                                    if color==black:
                                        screen.blit(RevEthNoteTailIMG, (LCoord[p][0]+1, LCoord[p][1]+13))
                                        screen.blit(RevEthNoteTailIMG, (LCoord[p][0]+1, LCoord[p][1]+17))
                                    else:
                                        screen.blit(RevBlueEthNoteTailIMG, (LCoord[p][0]+1, LCoord[p][1]+13))
                                        screen.blit(RevBlueEthNoteTailIMG, (LCoord[p][0]+1, LCoord[p][1]+17))
                                elif 31>=LList[p][1]>=17:
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, LCoord[p][1]+3), (LCoord[p][0]+9, LCoord[p][1]-21))
                                    if color==black:
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+10, LCoord[p][1]-21))
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+10, LCoord[p][1]-17))
                                    else:
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+10, LCoord[p][1]-21))
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+10, LCoord[p][1]-17))                                   
                                elif 17>LList[p][1]:
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, LCoord[p][1]+1), (LCoord[p][0]+9, 122))
                                    if color==black:
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+9, 120))
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+9, 124))
                                    else:
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+9, 120))
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+9, 124))
                            else:
                                high=LCoord[p][1][0]
                                low=LCoord[p][1][0]
                                highs=LList[p][1][0]
                                lows=LList[p][1][0]
                                for a in LList[p][1]:
                                    if a>highs:
                                        highs=a
                                    if a<lows:
                                        lows=a
                                for a in LCoord[p][1]:
                                    if a>high:
                                        high=a
                                    if a<low:
                                        low=a
                                if lows<17: #up
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+1), (LCoord[p][0]+9, 122))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+1), (LCoord[p][0]+9, low))
                                    if color==black:
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+9, 120))
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+9, 124))
                                    else:
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+9, 120))
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+9, 124))
                                elif highs>31:#down
                                    pygame.draw.line(screen, color, (LCoord[p][0]+1, low+5), (LCoord[p][0]+1, low+26))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+1, low+5), (LCoord[p][0]+1, high))
                                    
                                    if color==black:
                                        screen.blit(RevEthNoteTailIMG, (LCoord[p][0]+1, low+13))
                                        screen.blit(RevEthNoteTailIMG, (LCoord[p][0]+1, low+17))
                                    else:
                                        screen.blit(RevBlueEthNoteTailIMG, (LCoord[p][0]+1, low+13))
                                        screen.blit(RevBlueEthNoteTailIMG, (LCoord[p][0]+1, low+17))
                                else: #up
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+3), (LCoord[p][0]+9, high-21))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+3), (LCoord[p][0]+9, low))
                                    if color==black:
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+10, high-21))
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+10, high-17))
                                    else:
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+10, high-21))
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+10, high-17)) 
                                
            


                                
                                    
                        elif LList[p][0]=='EthNote' or LList[p][0]=='EthNotePlus':
                            if isinstance(LList[p][1], int):
                                if LList[p][1]>31:
                                    pygame.draw.line(screen, color, (LCoord[p][0]+1,LCoord[p][1]+5), (LCoord[p][0]+1, LCoord[p][1]+26))
                                    if color==black:
                                        screen.blit(RevEthNoteTailIMG, (LCoord[p][0]+1, LCoord[p][1]+17))
                                    else:
                                        screen.blit(RevBlueEthNoteTailIMG, (LCoord[p][0]+1, LCoord[p][1]+17))
                                        
                                elif 31>=LList[p][1]>=17:
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, LCoord[p][1]+3), (LCoord[p][0]+9, LCoord[p][1]-21))
                                    if color==black:
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+10, LCoord[p][1]-21))
                                    else:
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+10, LCoord[p][1]-21))
                                elif 17>LList[p][1]:
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, LCoord[p][1]+1), (LCoord[p][0]+9, 122))
                                    if color==black:
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+9, 118))
                                    else:
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+9, 118))
                            else:
                                high=LCoord[p][1][0]
                                low=LCoord[p][1][0]
                                highs=LList[p][1][0]
                                lows=LList[p][1][0]
                                for a in LList[p][1]:
                                    if a>highs:
                                        highs=a
                                    if a<lows:
                                        lows=a
                                for a in LCoord[p][1]:
                                    if a>high:
                                        high=a
                                    if a<low:
                                        low=a
                                if lows<17: #up
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+1), (LCoord[p][0]+9, 122))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+1), (LCoord[p][0]+9, low))
                                    if color==black:
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+9, 124))
                                    else:
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+9, 124))
                                elif highs>31:#down
                                    pygame.draw.line(screen, color, (LCoord[p][0]+1, low+5), (LCoord[p][0]+1, low+26))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+1, low+5), (LCoord[p][0]+1, high))
                                    
                                    if color==black:
                                        screen.blit(RevEthNoteTailIMG, (LCoord[p][0]+1, low+17))
                                    else:
                                        screen.blit(RevBlueEthNoteTailIMG, (LCoord[p][0]+1, low+17))
                                else: #up
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+3), (LCoord[p][0]+9, high-21))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+3), (LCoord[p][0]+9, low))
                                    if color==black:
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+10, high-21))
                                    else:
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+10, high-21))
                        elif LList[p][0]=='FourthNote' or LList[p][0]=='FourthNotePlus' or LList[p][0]=='HalfNotePlus' or LList[p][0]=='HalfNote':
                            if isinstance(LList[p][1], int):
                                if LList[p][1]>62:
                                    pygame.draw.line(screen, color, (LCoord[p][0]+2, LCoord[p][1]+4), (LCoord[p][0]+2, 62))
                                elif 62>=LList[p][1]>50:
                                    pygame.draw.line(screen, color, (LCoord[p][0]+2, LCoord[p][1]+4), (LCoord[p][0]+2, LCoord[p][1]+25))
                                elif 50>=LList[p][1]:
                                   pygame.draw.line(screen, color, (LCoord[p][0]+9, LCoord[p][1]+3), (LCoord[p][0]+9, LCoord[p][1]-18))
                            else:
                                high=LCoord[p][1][0]
                                low=LCoord[p][1][0]
                                highs=LList[p][1][0]
                                lows=LList[p][1][0]
                                for a in LList[p][1]:
                                    if a>highs:
                                        highs=a
                                    if a<lows:
                                        lows=a
                                for a in LCoord[p][1]:
                                    if a>high:
                                        high=a
                                    if a<low:
                                        low=a
                                if lows<17: #up
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+1), (LCoord[p][0]+9, 122))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+1), (LCoord[p][0]+9, low))
                                elif highs>31:#down
                                    pygame.draw.line(screen, color, (LCoord[p][0]+1, low+5), (LCoord[p][0]+1, low+26))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+1, low+5), (LCoord[p][0]+1, high))
                                else: #up
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+3), (LCoord[p][0]+9, high-21))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+3), (LCoord[p][0]+9, low))

                              
                elif p>=len(LList)-1:
                    pass
                elif p==0 or m==int(MeasEnder[LList[p][0]]):  #first
                    if LList[p][0]!=LList[p+1][0] or LList[p+1][1]==0:
                        if LList[p][0]=='SixteenthNote' or LList[p][0]=='SixteenthNotePlus':
                            if isinstance(LList[p][1], int):
                                if LList[p][1]>31:
                                    pygame.draw.line(screen, color, (LCoord[p][0]+1,LCoord[p][1]+5), (LCoord[p][0]+1, LCoord[p][1]+26))
                                    if color==black:
                                        screen.blit(RevEthNoteTailIMG, (LCoord[p][0]+1, LCoord[p][1]+13))
                                        screen.blit(RevEthNoteTailIMG, (LCoord[p][0]+1, LCoord[p][1]+17))
                                    else:
                                        screen.blit(RevBlueEthNoteTailIMG, (LCoord[p][0]+1, LCoord[p][1]+13))
                                        screen.blit(RevBlueEthNoteTailIMG, (LCoord[p][0]+1, LCoord[p][1]+17))
                                elif 31>=LList[p][1]>=17:
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, LCoord[p][1]+3), (LCoord[p][0]+9, LCoord[p][1]-21))
                                    if color==black:
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+10, LCoord[p][1]-21))
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+10, LCoord[p][1]-17))
                                    else:
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+10, LCoord[p][1]-21))
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+10, LCoord[p][1]-17))                                   
                                elif 17>LList[p][1]:
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, LCoord[p][1]+1), (LCoord[p][0]+9, 122))
                                    if color==black:
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+9, 120))
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+9, 124))
                                    else:
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+9, 120))
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+9, 124))
                            else:
                                high=LCoord[p][1][0]
                                low=LCoord[p][1][0]
                                highs=LList[p][1][0]
                                lows=LList[p][1][0]
                                for a in LList[p][1]:
                                    if a>highs:
                                        highs=a
                                    if a<lows:
                                        lows=a
                                for a in LCoord[p][1]:
                                    if a>high:
                                        high=a
                                    if a<low:
                                        low=a
                                if lows<17: #up
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+1), (LCoord[p][0]+9, 122))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+1), (LCoord[p][0]+9, low))
                                    if color==black:
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+9, 120))
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+9, 124))
                                    else:
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+9, 120))
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+9, 124))
                                elif highs>31:#down
                                    pygame.draw.line(screen, color, (LCoord[p][0]+1, low+5), (LCoord[p][0]+1, low+26))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+1, low+5), (LCoord[p][0]+1, high))
                                    
                                    if color==black:
                                        screen.blit(RevEthNoteTailIMG, (LCoord[p][0]+1, low+13))
                                        screen.blit(RevEthNoteTailIMG, (LCoord[p][0]+1, low+17))
                                    else:
                                        screen.blit(RevBlueEthNoteTailIMG, (LCoord[p][0]+1, low+13))
                                        screen.blit(RevBlueEthNoteTailIMG, (LCoord[p][0]+1, low+17))
                                else: #up
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+3), (LCoord[p][0]+9, high-21))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+3), (LCoord[p][0]+9, low))
                                    if color==black:
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+10, high-21))
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+10, high-17))
                                    else:
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+10, high-21))
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+10, high-17)) 
                                
            


                                
                                    
                        elif LList[p][0]=='EthNote' or LList[p][0]=='EthNotePlus':
                            if isinstance(LList[p][1], int):
                                if LList[p][1]>31:
                                    pygame.draw.line(screen, color, (LCoord[p][0]+1,LCoord[p][1]+5), (LCoord[p][0]+1, LCoord[p][1]+26))
                                    if color==black:
                                        screen.blit(RevEthNoteTailIMG, (LCoord[p][0]+1, LCoord[p][1]+17))
                                    else:
                                        screen.blit(RevBlueEthNoteTailIMG, (LCoord[p][0]+1, LCoord[p][1]+17))
                                        
                                elif 31>=LList[p][1]>=17:
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, LCoord[p][1]+3), (LCoord[p][0]+9, LCoord[p][1]-21))
                                    if color==black:
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+10, LCoord[p][1]-21))
                                    else:
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+10, LCoord[p][1]-21))
                                elif 17>LList[p][1]:
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, LCoord[p][1]+1), (LCoord[p][0]+9, 122))
                                    if color==black:
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+9, 118))
                                    else:
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+9, 118))
                            else:
                                high=LCoord[p][1][0]
                                low=LCoord[p][1][0]
                                highs=LList[p][1][0]
                                lows=LList[p][1][0]
                                for a in LList[p][1]:
                                    if a>highs:
                                        highs=a
                                    if a<lows:
                                        lows=a
                                for a in LCoord[p][1]:
                                    if a>high:
                                        high=a
                                    if a<low:
                                        low=a
                                if lows<17: #up
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+1), (LCoord[p][0]+9, 122))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+1), (LCoord[p][0]+9, low))
                                    if color==black:
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+9, 124))
                                    else:
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+9, 124))
                                elif highs>31:#down
                                    pygame.draw.line(screen, color, (LCoord[p][0]+1, low+5), (LCoord[p][0]+1, low+26))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+1, low+5), (LCoord[p][0]+1, high))
                                    
                                    if color==black:
                                        screen.blit(RevEthNoteTailIMG, (LCoord[p][0]+1, low+17))
                                    else:
                                        screen.blit(RevBlueEthNoteTailIMG, (LCoord[p][0]+1, low+17))
                                else: #up
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+3), (LCoord[p][0]+9, high-21))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+3), (LCoord[p][0]+9, low))
                                    if color==black:
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+10, high-21))
                                    else:
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+10, high-21))
                        elif LList[p][0]=='FourthNote' or LList[p][0]=='FourthNotePlus' or LList[p][0]=='HalfNotePlus' or LList[p][0]=='HalfNote':
                            if isinstance(LList[p][1], int):
                                if LList[p][1]>62:
                                    pygame.draw.line(screen, color, (LCoord[p][0]+2, LCoord[p][1]+4), (LCoord[p][0]+2, 62))
                                elif 62>=LList[p][1]>50:
                                    pygame.draw.line(screen, color, (LCoord[p][0]+2, LCoord[p][1]+4), (LCoord[p][0]+2, LCoord[p][1]+25))
                                elif 50>=LList[p][1]:
                                   pygame.draw.line(screen, color, (LCoord[p][0]+9, LCoord[p][1]+3), (LCoord[p][0]+9, LCoord[p][1]-18))
                            else:
                                high=LCoord[p][1][0]
                                low=LCoord[p][1][0]
                                highs=LList[p][1][0]
                                lows=LList[p][1][0]
                                for a in LList[p][1]:
                                    if a>highs:
                                        highs=a
                                    if a<lows:
                                        lows=a
                                for a in LCoord[p][1]:
                                    if a>high:
                                        high=a
                                    if a<low:
                                        low=a
                                if lows<17: #up
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+1), (LCoord[p][0]+9, 122))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+1), (LCoord[p][0]+9, low))
                                elif highs>31:#down
                                    pygame.draw.line(screen, color, (LCoord[p][0]+1, low+5), (LCoord[p][0]+1, low+26))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+1, low+5), (LCoord[p][0]+1, high))
                                else: #up
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+3), (LCoord[p][0]+9, high-21))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+3), (LCoord[p][0]+9, low))
                       
                else:  #mid
                    if (LList[p][0]!=LList[p-1][0] or LList[p-1][1]==0) and (LList[p][0]!=LList[p+1][0] or LList[p+1][1]==0):
                        if LList[p][0]=='SixteenthNote' or LList[p][0]=='SixteenthNotePlus':
                            if isinstance(LList[p][1], int):
                                if LList[p][1]>31:
                                    pygame.draw.line(screen, color, (LCoord[p][0]+1,LCoord[p][1]+5), (LCoord[p][0]+1, LCoord[p][1]+26))
                                    if color==black:
                                        screen.blit(RevEthNoteTailIMG, (LCoord[p][0]+1, LCoord[p][1]+13))
                                        screen.blit(RevEthNoteTailIMG, (LCoord[p][0]+1, LCoord[p][1]+17))
                                    else:
                                        screen.blit(RevBlueEthNoteTailIMG, (LCoord[p][0]+1, LCoord[p][1]+13))
                                        screen.blit(RevBlueEthNoteTailIMG, (LCoord[p][0]+1, LCoord[p][1]+17))
                                elif 31>=LList[p][1]>=17:
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, LCoord[p][1]+3), (LCoord[p][0]+9, LCoord[p][1]-21))
                                    if color==black:
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+10, LCoord[p][1]-21))
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+10, LCoord[p][1]-17))
                                    else:
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+10, LCoord[p][1]-21))
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+10, LCoord[p][1]-17))                                   
                                elif 17>LList[p][1]:
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, LCoord[p][1]+1), (LCoord[p][0]+9, 122))
                                    if color==black:
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+9, 120))
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+9, 124))
                                    else:
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+9, 120))
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+9, 124))
                            else:
                                high=LCoord[p][1][0]
                                low=LCoord[p][1][0]
                                highs=LList[p][1][0]
                                lows=LList[p][1][0]
                                for a in LList[p][1]:
                                    if a>highs:
                                        highs=a
                                    if a<lows:
                                        lows=a
                                for a in LCoord[p][1]:
                                    if a>high:
                                        high=a
                                    if a<low:
                                        low=a
                                if lows<17: #up
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+1), (LCoord[p][0]+9, 122))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+1), (LCoord[p][0]+9, low))
                                    if color==black:
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+9, 120))
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+9, 124))
                                    else:
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+9, 120))
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+9, 124))
                                elif highs>31:#down
                                    pygame.draw.line(screen, color, (LCoord[p][0]+1, low+5), (LCoord[p][0]+1, low+26))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+1, low+5), (LCoord[p][0]+1, high))
                                    
                                    if color==black:
                                        screen.blit(RevEthNoteTailIMG, (LCoord[p][0]+1, low+13))
                                        screen.blit(RevEthNoteTailIMG, (LCoord[p][0]+1, low+17))
                                    else:
                                        screen.blit(RevBlueEthNoteTailIMG, (LCoord[p][0]+1, low+13))
                                        screen.blit(RevBlueEthNoteTailIMG, (LCoord[p][0]+1, low+17))
                                else: #up
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+3), (LCoord[p][0]+9, high-21))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+3), (LCoord[p][0]+9, low))
                                    if color==black:
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+10, high-21))
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+10, high-17))
                                    else:
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+10, high-21))
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+10, high-17)) 
                                
            


                                
                                    
                        elif LList[p][0]=='EthNote' or LList[p][0]=='EthNotePlus':
                            if isinstance(LList[p][1], int):
                                if LList[p][1]>31:
                                    pygame.draw.line(screen, color, (LCoord[p][0]+1,LCoord[p][1]+5), (LCoord[p][0]+1, LCoord[p][1]+26))
                                    if color==black:
                                        screen.blit(RevEthNoteTailIMG, (LCoord[p][0]+1, LCoord[p][1]+17))
                                    else:
                                        screen.blit(RevBlueEthNoteTailIMG, (LCoord[p][0]+1, LCoord[p][1]+17))
                                        
                                elif 31>=LList[p][1]>=17:
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, LCoord[p][1]+3), (LCoord[p][0]+9, LCoord[p][1]-21))
                                    if color==black:
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+10, LCoord[p][1]-21))
                                    else:
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+10, LCoord[p][1]-21))
                                elif 17>LList[p][1]:
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, LCoord[p][1]+1), (LCoord[p][0]+9, 122))
                                    if color==black:
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+9, 120))
                                    else:
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+9, 120))
                            else:
                                high=LCoord[p][1][0]
                                low=LCoord[p][1][0]
                                highs=LList[p][1][0]
                                lows=LList[p][1][0]
                                for a in LList[p][1]:
                                    if a>highs:
                                        highs=a
                                    if a<lows:
                                        lows=a
                                for a in LCoord[p][1]:
                                    if a>high:
                                        high=a
                                    if a<low:
                                        low=a
                                if lows<17: #up
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+1), (LCoord[p][0]+9, 122))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+1), (LCoord[p][0]+9, low))
                                    if color==black:
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+9, 118))
                                    else:
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+9, 118))
                                elif highs>31:#down
                                    pygame.draw.line(screen, color, (LCoord[p][0]+1, low+5), (LCoord[p][0]+1, low+26))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+1, low+5), (LCoord[p][0]+1, high))
                                    
                                    if color==black:
                                        screen.blit(RevEthNoteTailIMG, (LCoord[p][0]+1, low+17))
                                    else:
                                        screen.blit(RevBlueEthNoteTailIMG, (LCoord[p][0]+1, low+17))
                                else: #up
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+3), (LCoord[p][0]+9, high-21))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+3), (LCoord[p][0]+9, low))
                                    if color==black:
                                        screen.blit(EthNoteTailIMG, (LCoord[p][0]+10, high-21))
                                    else:
                                        screen.blit(BlueEthNoteTailIMG, (LCoord[p][0]+10, high-21))
                        elif LList[p][0]=='FourthNote' or LList[p][0]=='FourthNotePlus' or LList[p][0]=='HalfNotePlus' or LList[p][0]=='HalfNote':
                            if isinstance(LList[p][1], int):
                                if LList[p][1]>62:
                                    pygame.draw.line(screen, color, (LCoord[p][0]+2, LCoord[p][1]+4), (LCoord[p][0]+2, 62))
                                elif 62>=LList[p][1]>50:
                                    pygame.draw.line(screen, color, (LCoord[p][0]+2, LCoord[p][1]+4), (LCoord[p][0]+2, LCoord[p][1]+25))
                                elif 50>=LList[p][1]:
                                   pygame.draw.line(screen, color, (LCoord[p][0]+9, LCoord[p][1]+3), (LCoord[p][0]+9, LCoord[p][1]-18))
                            else:
                                high=LCoord[p][1][0]
                                low=LCoord[p][1][0]
                                highs=LList[p][1][0]
                                lows=LList[p][1][0]
                                for a in LList[p][1]:
                                    if a>highs:
                                        highs=a
                                    if a<lows:
                                        lows=a
                                for a in LCoord[p][1]:
                                    if a>high:
                                        high=a
                                    if a<low:
                                        low=a
                                if lows<17: #up
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+1), (LCoord[p][0]+9, 122))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+1), (LCoord[p][0]+9, low))
                                elif highs>31:#down
                                    pygame.draw.line(screen, color, (LCoord[p][0]+1, low+5), (LCoord[p][0]+1, low+26))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+1, low+5), (LCoord[p][0]+1, high))
                                else: #up
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+3), (LCoord[p][0]+9, high-21))
                                    pygame.draw.line(screen, color, (LCoord[p][0]+9, high+3), (LCoord[p][0]+9, low))            


    def MultiNotesR(RCoord, RList, color, TS):
        p=-1
        f=0
        m=0
        time=16*(int(TS[0])/int(TS[1]))
        while p+2<len(RCoord):
            p+=1
            f+=1
            m+=int(MeasEnder[RList[p][0]])
            if m>=time:
                m=m%time
                pass
            elif RList[p][0]==RList[f][0] and RList[p][1]!=89 and RList[f][1]!=89:
                while RList[p][0]==RList[f][0] and RList[f][1]!=89:
                    m+=int(MeasEnder[RList[f][0]])
                    f+=1
                    if len(RCoord)<=f:
                        break
                    if m>=time:
                        m=m%time
                        break
                f-=1
                if isinstance(RCoord[p][1], list) or isinstance(RCoord[p][1], tuple):
                    high=list((RCoord[p][0], RCoord[p][1][0]))
                    low=list((RCoord[p][0], RCoord[p][1][0]))
                else:
                    high=RCoord[p]
                    low=RCoord[p]
                for a in RCoord[p:f+1]:
                    if isinstance(a[1], int) or isinstance(a[1], float):
                        if a[1]<high[1]: #coord go backwards
                            high=a
                        if a[1]>low[1]:
                            low=a
                    else:
                        for w in a[1]:
                            if w<high[1]:
                                high=[a[0], w]
                            if w>low[1]:
                                low=[a[0], w]
 #                       pygame.draw.line(screen, color, (a[0], ), (a[0]))
                if high[1]>34:
                    if RList[p][0]=='EthNote' or RList[p][0]=='SixteenthNote' or RList[p][0]=='FourthNote':
                        pygame.draw.rect(screen, color, (RCoord[p][0]+10, high[1]-21, RCoord[f][0]-RCoord[p][0], 3))
                        b=p
                        while b-1<f:
       
                            if isinstance(RCoord[b][1], int) or isinstance(RCoord[b][1], float):
                                pygame.draw.line(screen, color, (RCoord[b][0]+10, RCoord[b][1]+3), (RCoord[b][0]+10, high[1]-21))
                                b+=1
                            else:
                                for k in RCoord[b][1]:
                                    pygame.draw.line(screen, color, (RCoord[b][0]+10, k+3), (RCoord[b][0]+10, high[1]-21)) #+10
                                b+=1
                        if RList[p][0]=='SixteenthNote':
                            pygame.draw.rect(screen, color, (RCoord[p][0]+10, high[1]-17, RCoord[f][0]-RCoord[p][0], 3)) 
                elif high[1]<=34:
                    if RList[p][0]=='EthNote' or RList[p][0]=='SixteenthNote' or RList[p][0]=='FourthNote':
                        pygame.draw.rect(screen, color, (RCoord[p][0]+1, low[1]+21, RCoord[f][0]-RCoord[p][0], 3))
                        b=p
                        while b-1<f:
                            if isinstance(RCoord[b][1], int) or isinstance(RCoord[b][1], float):
                                pygame.draw.line(screen, color, (RCoord[b][0]+1, RCoord[b][1]+5), (RCoord[b][0]+1, low[1]+23))
                                b+=1
                            else:
                                for k in RCoord[b][1]:
                                    #here
                                    pygame.draw.line(screen, color, (RCoord[b][0]+1, k+3), (RCoord[b][0]+1, low[1]+23))
                                b+=1
                        if RList[p][0]=='SixteenthNote':
                            pygame.draw.rect(screen, color, (RCoord[p][0]+1, low[1]+17, RCoord[f][0]-RCoord[p][0], 3))               
                f+=1
                p+=f-p-1
    def MultiNotesL(LCoord, LList, color, TS):
        p=-1
        f=0
        m=0
        time=16*(int(TS[0])/int(TS[1]))
        while p+2<len(LCoord):
            p+=1
            f+=1
            m+=int(MeasEnder[LList[p][0]])
            if m>=time:
                m=m%time
                break
            elif LList[p][0]==LList[f][0] and LList[p][1]!=0 and LList[f][1]!=0:
                while LList[p][0]==LList[f][0] and LList[f][1]!=0:
                    m+=int(MeasEnder[LList[f][0]])
                    f+=1
                    if len(LCoord)<=f:
                        break
                    if m>=time:
                        m=m%time
                        break
                f-=1
                if isinstance(LCoord[p][1], list) or isinstance(LCoord[p][1], tuple):
                    high=list((LCoord[p][0], LCoord[p][1][0]))
                    low=list((LCoord[p][0], LCoord[p][1][0]))
                else:
                    high=LCoord[p]
                    low=LCoord[p]
                
                for a in LCoord[p:f+1]:
                    if isinstance(a[1], int) or isinstance(a[1], float):
                        if a[1]<high[1]: #coord go backwards
                            high=a
                        if a[1]>low[1]:
                            low=a
                    else:
                        for w in a[1]:
                            if w<high[1]:
                                high=[a[0], w]
                            if w>low[1]:
                                low=[a[0], w]
                #print(high, low)
                if high[1]<115:
                    if LList[p][0]=='EthNote' or LList[p][0]=='SixteenthNote' or LList[p][0]=='FourthNote':
                        pygame.draw.rect(screen, color, (LCoord[p][0]+1, low[1]+21, LCoord[f][0]-LCoord[p][0], 3))
                        b=p
                        while b-1<f:
                            if isinstance(LCoord[b][1], int) or isinstance(LCoord[b][1], float):
                               pygame.draw.line(screen, color, (LCoord[b][0]+1, LCoord[b][1]+5), (LCoord[b][0]+1, low[1]+23))
                               b+=1
                            else:
                                for k in LCoord[b][1]:
                                    pygame.draw.line(screen, color, (LCoord[b][0]+1, k+4), (LCoord[b][0]+1, low[1]+23))
                                b+=1
                        if LList[p][0]=='SixteenthNote':
                            pygame.draw.rect(screen, color, (LCoord[p][0]+1, low[1]+17, LCoord[f][0]-LCoord[p][0], 3))
                            
                elif high[1]>=115:
                    pygame.draw.rect(screen, color, (LCoord[p][0]+10, high[1]-21, LCoord[f][0]-LCoord[p][0], 3))
                    b=p
                    while b-1<f:
                        if isinstance(LCoord[b][1], int) or isinstance(LCoord[b][1], float):
                            pygame.draw.line(screen, color, (LCoord[b][0]+10, LCoord[b][1]+3), (LCoord[b][0]+10, high[1]-21))
                            b+=1
                        else:
                            for k in LCoord[b][1]:
                                pygame.draw.line(screen, color, (LCoord[b][0]+10, k+3), (LCoord[b][0]+10, high[1]-21))
                            b+=1
                f+=1
                p+=f-p-1
    def MeasLines(MeasLCoord, MeasRCoord):
        for a in MeasLCoord:
            pygame.draw.line(screen, black, (a, 50), (a, 135))
            g=0
            while g<5:
                pygame.draw.line(screen, black, (a, 110+g*6), (a-150, 110+g*6))
                g+=1
        for a in MeasRCoord:
            pygame.draw.line(screen, black, (a, 50), (a, 135))
            g=0
            while g<5:
                pygame.draw.line(screen, black, (a, 50+g*6), (a-150, 50+g*6))
                g+=1
    def LedgerLines(RList, RCoord, LList, LCoord):
        h=-1
        for a in RList:
            h+=1
            if h>=(len(RCoord)):
                break
            if isinstance(a[1], list) or isinstance(a[1], tuple):
                high=a[1][0]
                for b in a[1]:
                    if b>high:
                        high=b
            elif isinstance(a[1], int) or isinstance(a[1], float):
                high=a[1]
            if 75>high>60:
                pygame.draw.line(screen, black, (RCoord[h][0]-4, 44), (RCoord[h][0]+15, 44))
                if high>63:
                    pygame.draw.line(screen, black, (RCoord[h][0]-4, 38), (RCoord[h][0]+15, 38))
                if high>67:
                    pygame.draw.line(screen, black, (RCoord[h][0]-4, 32), (RCoord[h][0]+15, 32))
                if high>70:
                    pygame.draw.line(screen, black, (RCoord[h][0]-4, 26), (RCoord[h][0]+15, 26))
            elif 89>high>=75:
                pygame.draw.line(screen, black, (RCoord[h][0]-4, 44), (RCoord[h][0]+15, 44))
                if high>75:
                    pygame.draw.line(screen, black, (RCoord[h][0]-4, 38), (RCoord[h][0]+15, 38))
                if high>79:
                    pygame.draw.line(screen, black, (RCoord[h][0]-4, 32), (RCoord[h][0]+15, 32))
                if high>82:
                    pygame.draw.line(screen, black, (RCoord[h][0]-4, 26), (RCoord[h][0]+15, 26))
                if 89>high>86:
                    pygame.draw.line(screen, black, (RCoord[h][0]-4, 20), (RCoord[h][0]+15, 20))

        h=-1
        for a in LList:
            h+=1   # high means low
            if h>=(len(LCoord)):
                break
            if isinstance(a[1], list) or isinstance(a[1], tuple):
                high=a[1][0]
                for b in a[1]:
                    if b<high:
                        high=b
            elif isinstance(a[1], int) or isinstance(a[1], float):
                high=a[1]
            if 0<high<20:
                pygame.draw.line(screen, black, (LCoord[h][0]-4, 140), (LCoord[h][0]+15, 140))
                if high<17:
                    pygame.draw.line(screen, black, (LCoord[h][0]-4, 146), (LCoord[h][0]+15, 146))
                if high<14:
                    pygame.draw.line(screen, black, (LCoord[h][0]-4, 152), (LCoord[h][0]+15, 152))
                if high<10:
                    pygame.draw.line(screen, black, (LCoord[h][0]-4, 158), (LCoord[h][0]+15, 158))
                if high<6:
                    pygame.draw.line(screen, black, (LCoord[h][0]-4, 164), (LCoord[h][0]+15, 164))
                if high<4:
                    pygame.draw.line(screen, black, (LCoord[h][0]-4, 170), (LCoord[h][0]+15, 170))
        
