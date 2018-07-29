import pygame
DrawInputsList={'1':'19', '2':'25', '3':'45', '4':'71', '5':'73', '6':'91',
                '7':'96', '8':'116', '9':'142', '10':'144', '11':'162', 
                '12':'168', '13':'187', '14':'192', '15':'213', '16':'238',
                '17':'240', '18':'258', '19':'263', '20':'283', '21':'309', '22':'312',
                '23':'329', '24':'335', '25':'354', '26':'360', '27':'380', '28':'406',
                '29':'408', '30':'426', '31':'431', '32':'451', '33':'477', '34':'479',
                '35':'497', '36':'503', '37':'522', '38':'527', '39':'548', '40':'573',
                '41':'575', '42':'593', '43':'598', '44':'618', '45':'644', '46':'646',
                '47':'664', '48':'670', '49':'689', '50':'694', '51':'714', '52':'740',
                '53':'742', '54':'760', '55':'765', '56':'785', '57':'811', '58':'813',
                '59':'831', '60':'837', '61':'856', '62':'861', '63':'882', '64':'908',
                '65':'909', '66':'928', '67':'933', '68':'953', '69':'979', '70':'981',
                '71':'999', '72':'10005', '73':'1024', '74':'1029', '75':'1050', '76':'1076',
                '77':'1077', '78':'1096', '79':'1100', '80':'1121', '81':'1147', '82':'1148',
                '83':'1167', '84':'1172',
                '85':'1191', '86':'1196', '87':'1217', '88':'1242'
                }
XValues={'0':'-50','1':'23', '2':'41','3':'48','4':'72','5':'89','6':'96', '7':'112','8':'120', '9':'144',
         '10':'160','11':'167','12':'184','13':'190','14':'208','15':'215','16':'239', '17':'256',
         '18':'262','19':'279', '20':'287', '21':'310','22':'327','23':'334', '24':'351','25':'358',
         '26':'375','27':'383', '28':'407','29':'423','30':'430','31':'446','32':'454', '33':'478',
         '34':'494','35':'502','36':'518','37':'526','38':'542','39':'550','40':'574','41':'590',
         '42':'598','43':'613','44':'622', '45':'646', '46':'661', '47':'670', '48':'685','49':'694',
         '50':'709','51':'718','52':'741','53':'757','54':'765','55':'780',
         '56':'789','57':'813','58':'828','59':'837','60':'852','61':'861', '62':'876','63':'885',
         '64':'909', '65':'924', '66':'933','67':'947','68':'956','69':'980','70':'996','71':'1004',
         '72':'1019','73':'1028','74':'1044', '75':'1052','76':'1077','77':'1092','78':'1100',
         '79':'1115','80':'1124',
         '81':'1148', '82':'1163','83':'1172',
         '84':'1187','85':'1196','86':'1211', '87':'1220', '88':'1244', '89':'-50'}

SharpList=[2,5,7,10,12,14,17,19,22,24,26,29,31,34,36,38,41,43,46,48,50,53,55,58,60,
           62, 65,67,70, 72,74,77,79,82,84,86]
MidList=[1,6,11,13,18,23,25,30,35,37,42,47,49,54,59,61,66,71,73,78,83,85]
RightList=[3,8,15,20,27,32,39,44,51,56,63,68,75,80,87]
SharpIMG=pygame.image.load('SharpD.png')
RightIMG=pygame.image.load('RBlue.png')
LeftIMG=pygame.image.load('LBlue.png')
MidIMG=pygame.image.load('MidBlue.png')

ZeroIMG=pygame.image.load('0.png')
OneIMG=pygame.image.load('1.png')
TwoIMG=pygame.image.load('2.png')
ThreeIMG=pygame.image.load('3.png')
FourIMG=pygame.image.load('4.png')
FiveIMG=pygame.image.load('5.png')
SixIMG=pygame.image.load('6.png')
SevenIMG=pygame.image.load('7.png')
EightIMG=pygame.image.load('8.png')
NineIMG=pygame.image.load('9.png')
BassIMG=pygame.image.load('Bass.png')
TrebleIMG=pygame.image.load('Treble4.png')
TimeSig={'0':ZeroIMG, '1':OneIMG, '2':TwoIMG, '3':ThreeIMG, '4':FourIMG, '5':FiveIMG,
         '6':SixIMG,'7':SevenIMG,'8':EightIMG, '9':NineIMG}

white=(255,255,255)
black=(0,0,0)
blue=(0,255,255)
darkblue=(0,0,255)
size=(1300,900)
screen=pygame.display.set_mode(size)

class Draw():
    def GrandStaff(TS):
        g=0
        while g<5:
            pygame.draw.line(screen, black, (10, 50+g*6), (1350,50+g*6))
            g+=1
        g=0
        while g<5:
            pygame.draw.line(screen, black, (10, 110+g*6), (1350, 110+g*6))
            g+=1
        pygame.draw.line(screen, black, (10,50), (10, 134))
        g=0
        while g<3:
            pygame.draw.line(screen, black, (143+g*168,500), (143+g*168,250))
            g+=1
        g=0
        while g<4:
            pygame.draw.line(screen, black, (645+g*168,500), (645+g*168,250))
            g+=1
        screen.blit(TrebleIMG, (12,45))
        screen.blit(BassIMG, (6,104))
        if len(str(TS[0]))==1:
            screen.blit(TimeSig[str(TS[0])], (40,50))
            screen.blit(TimeSig[str(TS[0])], (40,110))
        elif len(str(TS[0]))==2:
            screen.blit(TimeSig[str(TS[0][0])], (40,50))
            screen.blit(TimeSig[str(TS[0][1])], (46,50))
            screen.blit(TimeSig[str(TS[0][0])], (40,110))
            screen.blit(TimeSig[str(TS[0][1])], (46,110))
            
        if len(str(TS[1]))==1:
            screen.blit(TimeSig[str(TS[1])], (38,61))
            screen.blit(TimeSig[str(TS[1])], (38,121))
        elif len(str(TS[1]))==2:
            screen.blit(TimeSig[str(TS[1][0])], (38,61))
            screen.blit(TimeSig[str(TS[1][1])], (44,61))
            screen.blit(TimeSig[str(TS[1][0])], (38,121))
            screen.blit(TimeSig[str(TS[1][1])], (44,121))
        
    def WhichKey(Note):
        if Note in SharpList:
            return (SharpIMG)
        elif Note in RightList:
            return (RightIMG)
        elif Note in MidList:
            return (MidIMG)
        else:
            return (LeftIMG)
        screen.blit(IMG, (Draw.FindX(Note), Draw.FindY(Note)))
    def FindX(Note):
        return(int(DrawInputsList[str(Note)]))
    def FindY(Note):
        if Note in MidList:
            return(490)
        elif Note in RightList:
            return (491)
        elif Note in SharpList:
            return(488)
        else:
            return(492)
    def NoteLength(Note):
        return((Note[0][1]-Note[0][0])/8)
    
    def FindXRect(Note):
        return (int(XValues[str(Note)]))

    def NoteWidth(Note):
        
        if Note in SharpList:
            return(15)
        else:
            return(23)

    def Rects(NewTimeList, marker):
        g=-1
        for a in NewTimeList:
            g+=1
            if a[1] in SharpList:
                color=darkblue
            else:
                color=blue
            pygame.draw.rect(screen, color, (Draw.FindXRect(a[1]), (marker/8)+500-Draw.NoteLength(a)-(a[0][0]/8),Draw.NoteWidth(a[1]), ((a[0][1]-a[0][0])/8)))
    def CurrentNotes(CurrentPlaying):
        for a in CurrentPlaying:
            if a==0 or a==89:
                pass
            else:
                screen.blit(Draw.WhichKey(a), (Draw.FindX(a), Draw.FindY(a)))
        
