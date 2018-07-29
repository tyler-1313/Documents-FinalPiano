import csv
import pygame



Trans={'1':'16', '2':'8', '4':'4', '8':'2', '16':'1'}
MeasEnderRev={'1':'SixteenthNote', '1.5':'SixteenthNotePlus', '2':'EthNote', '3':'EthNotePlus', '4':'FourthNote',
           '6':'FourthNotePlus', '8':'HalfNote', '12':'HalfNotePlus', '16':'WholeNote'}
MeasEnder={'SixteenthNote':'1', 'SixteenthNotePlus':'1.5', 'EthNote':'2', 'EthNotePlus':'3', 'FourthNote':'4',
           'FourthNotePlus':'6', 'HalfNote':'8', 'HalfNotePlus':'12', 'WholeNote':'16'}
NoteDe={'89':'6.66','40':'0', '41':'0', '42':'1', '43':'1', '44':'2', '45':'3', '46':'3', '47':'4', '48':'4', '49':'5', '50':'5', '51':'6', '52':'7',
    '53':'7', '54':'8', '55':'8', '56':'9', '57':'10', '58':'10', '59':'11', '60':'11', '61':'12', '62':'12', '63':'13', '64':'14',
    '65':'14', '75':'13', '76':'14', '66':'15', '77':'14', '78':'15','67':'15', '68':'16', '79':'15', '69':'17', '80':'16', '81':'17',
    '70':'17', '71':'18', '82':'17', '83':'18','72':'18', '73':'19', '84':'18', '74':'19', '85':'19', '86':'19', '87':'20', '88':'21',
}
NoteDeL={'0':'-5.66','1':'-23', '2':'-22',  '3':'-22', '4':'-21', '5':'-20', '6':'-20', '7':'-19', '8':'-19', '9':'-18', '10':'-17', '11':'-17',
    '12':'-16', '13':'-16', '14':'-15', '15':'-15', '16':'-14', '17':'-13', '18':'-13', '19':'-12', '20':'-12', '21':'-11', '22':'-10',
    '23':'-10', '24':'-9', '25':'-9', '26':'-8','27':'-8', '28':'-7', '29':'-6', '30':'-6', '31':'-5', '32':'-5', '33':'-4', '34':'-3',
    '35':'-3', '36':'-2', '37':'-2', '38':'-1', '39':'-1'}
PlusRemainder={'EthNotePlus':'SixteenthNote', 'FourthNotePlus':'EthNote',
               'HalfNotePlus':'FourthNote'}
DoubleNote={'SixteenthNote':'EthNote', 'EthNote':'FourthNote', 'FourthNote':
            'HalfNote', 'HalfNote':'WholeNote'}
StfEnder={'SixteenthNote':'16', 'SixteenthNotePlus':'24', 'EthNote':'32', 'EthNotePlus':'48', 'FourthNote':'64',
           'FourthNotePlus':'96', 'HalfNote':'128', 'HalfNotePlus':'192', 'WholeNote':'256'
          }
FlatList=[2,5,7,10,12,14,17,19,22,24,26,29,31,34,36,38]
           
SharpList=[41,43,46,48,50,53,55,58,60,
           62, 65,67,70, 72,74,77,79,82,84,86]
SixteenthNoteRestIMG=pygame.image.load('16thRest.png')
EthNoteRestIMG=pygame.image.load('8thNoteRest.png')
FourthNoteRestIMG=pygame.image.load('4thNoteRest.png')
HalfNoteRestIMG=pygame.image.load('HalfNoteRest.png')
WholeNoteRestIMG=pygame.image.load('WholeNoteRest.png')
RestImgs={'SixteenthNote':SixteenthNoteRestIMG, 'EthNote':EthNoteRestIMG, 'FourthNote':FourthNoteRestIMG,
          'HalfNote':HalfNoteRestIMG, 'WholeNote':WholeNoteRestIMG}
NoteIMG=pygame.image.load('Note.png')
BlueNoteIMG=pygame.image.load('BlueNote.png')
HalfNoteIMG=pygame.image.load('HalfNote.png')
BlueHalfNoteIMG=pygame.image.load('BlueHalfNote.png')
FlatIMG=pygame.image.load('Flat.png')
SharpNoteIMG=pygame.image.load('Sharp.png')
BlueSharpNoteIMG=pygame.image.load('BlueSharp.png')
BlueFlatIMG=pygame.image.load('BlueFlat.png')

white=(255,255,255)
black=(0,0,0)
blue=(0,255,255)
darkblue=(0,0,255)
size=(1300,900)
screen=pygame.display.set_mode(size)
vaIMG=pygame.image.load('vaIMG.png')
class Note():
        
    def GetNoteList(CSVFile):
        f = open(CSVFile, 'rt', encoding='latin1')
        csv_f = csv.reader(f)
        g=0
        TimeList=[]
        for row in csv_f:
            g+=1
            if len(row[2])>=17:
                pass
            else:
                TimeList.append(tuple(((row[1]), int(row[4])-20)))
 #       print(TimeList[0:20], 'here')
        g=0
        NoteList=[]
        NoteTypeList=[]
        NewTimeList=[]
        while len(TimeList)>0:
            g=1
            if TimeList[0][1]==TimeList[1][1]:
                NewTimeList.append(tuple((list((int(TimeList[0][0]), int(TimeList[g][0]))), int(TimeList[0][1]))))
                del TimeList[0]
                del TimeList[0]
            else:
                while TimeList[0][1]!=TimeList[g][1]:
                    g+=1
                NewTimeList.append(tuple((list((int(TimeList[0][0]), int(TimeList[g][0]))), int(TimeList[0][1]))))
                del TimeList[g]
                del TimeList[0]
        if NewTimeList[0][0][0]>0:
            NewTimeList.insert(0, list((list(((0, NewTimeList[0][0][0]))), 0)))
       # print(NewTimeList[0:20])
        return(NewTimeList)
    def GetRLLists(NewTimeList):
        RList=[]
        LList=[]
        for a in NewTimeList:
            if a[1]>39:
                RList.append(a)
            else:
                LList.append(a)
       
        if len(LList)==0:
            for a in RList:
                LList.append((a[0], 0))
        if len(RList)==0:
            for a in LList:
                RList.append((a[0], 89))
                
        if LList[0][0][0]>0:
            LList.insert(0, tuple(((0, LList[0][0][0]), 0)))
        if RList[0][0][0]>0:
            RList.insert(0, tuple(((0, RList[0][0][0]), 89)))
        g=0
        for a in LList:
            g+=1
            if g+1>=len(LList):
                break
            if a[0][1]<LList[g][0][0]:
                LList.insert(g, tuple(((a[0][1],LList[g][0][0]) ,0)))
        g=0
        for a in RList:
            g+=1
            if g+1>=len(RList):
                break
            if a[0][1]<RList[g][0][0]:
                RList.insert(g, tuple(((a[0][1],RList[g][0][0]) ,89)))
        return(LList, RList)
    def FindChords(RList, LList):
        g=0
        while g<5:
            g+=1
            p=0
            f=-1
            for a in RList:
                p+=1
                f+=1
                if p<len(RList):
                    if a[0][0]==RList[p][0][0]:
                        if isinstance(RList[f][1], int) and isinstance(RList[p][1], int):
                            RList[f]=list((RList[f]))
                            RList[p]=list((RList[p]))
                            RList[f][1]=list((RList[f][1], 0))
                            RList[f][1].insert(2, RList[p][1])
                            del RList[f][1][1]
                            del RList[p]
                        elif isinstance(RList[f][1], int)==False and isinstance(RList[p][1], int):
                            RList[f]=list((RList[f]))
                            RList[p]=list((RList[p]))
                            RList[f][1]=list((RList[f][1]))
                            RList[f][1].insert(2, RList[p][1])
                            del RList[p]
                        elif isinstance(RList[f][1], int)==False and isinstance(RList[p][1], int)==False:
                            RList[f]=list((RList[f]))
                            RList[p]=list((RList[p]))
                            RList[f][1]=list((RList[f][1]))
                            for b in RList[p][1]:
                                RList[f][1].insert(2, b)
                            del RList[p]
            p=0
            f=-1
            for a in LList:
                p+=1
                f+=1
                if p<len(LList):
                    if a[0][0]==LList[p][0][0]:
                        if isinstance(LList[f][1], int) and isinstance(LList[p][1], int):
                            LList[f]=list((LList[f]))
                            LList[p]=list((LList[p]))
                            LList[f][1]=list((LList[f][1], 0))
                            LList[f][1].insert(2, LList[p][1])
                            del LList[f][1][1]
                            del LList[p]
                        elif isinstance(LList[f][1], int)==False and isinstance(LList[p][1], int):
                            LList[f]=list((LList[f]))
                            LList[p]=list((LList[p]))
                            LList[f][1]=list((LList[f][1]))
                            LList[f][1].insert(2, LList[p][1])
                            del LList[p]
                        elif isinstance(LList[f][1], int)==False and isinstance(LList[p][1], int)==False:
                            LList[f]=list((LList[f]))
                            LList[p]=list((LList[p]))
                            LList[f][1]=list((LList[f][1]))
                            for b in LList[p][1]:
                                LList[f][1].insert(2, b)
                            del LList[p]
        return (RList, LList)
    # TS=[3,8] BPM=120
    def Reduce(LList, RList):
        k=-1
        for a in RList:
            k+=1
            RList[k]=list(RList[k])
            RList[k][0]=list(RList[k][0])
            b=a[0][1]-a[0][0]
            RList[k].insert(1, b)
            del RList[k][0]
        k=-1
        for a in LList:
            k+=1
            LList[k]=list(LList[k])
            LList[k][0]=list(LList[k][0])
            b=a[0][1]-a[0][0]
            LList[k].insert(1, b)
            del LList[k][0]
        return (LList, RList)
        
    def BreakUpBigRests(RList, LList, TS, BPM):
        h=((60/BPM)*1000)/int(Trans[str(TS[1])])
        p=-1
        for a in RList:
            p+=1
            if a[1]==89:
                d=a[0]
                while d>0:
                    d-=h
                    if d>(-1*(h/2)):
                        RList.insert(p+1, list(((h, 89))))
                del RList[p]
        p=-1
        for a in LList:
            p+=1
            if a[1]==0:
                d=a[0]
                while d>0:
                    d-=h
                    if d>(-1*(h/2)):
                        LList.insert(p+1, list(((h, 0))))
                del LList[p]
        return(RList, LList)


                
    def GetMeasLists(RList, LList, TS, BPM):
        k=-1
        for a in RList:
            k+=1
            h=((60/BPM)*1000)/int(Trans[str(TS[1])])   #h=16th note duration
            d=a[0]   
            if d<1.25*h:
                RList[k][0]='SixteenthNote'
            elif 1.25<=d<1.75:
                RList[k][0]='SixteenthNotePlus'
            elif 1.75*h<=d<2.5*h:
                RList[k][0]='EthNote'
            elif 2.5*h<=d<3.5*h:
                RList[k][0]='EthNotePlus'
            elif 3.5*h<=d<h*5:
                RList[k][0]='FourthNote'
            elif 5*h<=d<h*7:
                RList[k][0]='FourthNotePlus'
            elif 7*h<=d<10*h:
                RList[k][0]='HalfNote'
            elif 10*h<=d<14*h:
                RList[k][0]='HalfNotePlus'
            else:
                RList[k][0]='WholeNote'
        k=-1
        for a in LList:
            k+=1
            h=((60/BPM)*1000)/int(Trans[str(TS[1])])   #h=16th note duration
            d=a[0]
            if d<1.25*h:
                LList[k][0]='SixteenthNote'
            elif 1.25<=d<1.75:
                LList[k][0]='SixteenthNotePlus'
            elif 1.75*h<=d<2.5*h:
                LList[k][0]='EthNote'
            elif 2.5*h<=d<3.5*h:
                LList[k][0]='EthNotePlus'
            elif 3.5*h<=d<h*5:
                LList[k][0]='FourthNote'
            elif 5*h<=d<h*7:
                LList[k][0]='FourthNotePlus'
            elif 7*h<=d<10*h:
                LList[k][0]='HalfNote'
            elif 10*h<=d<14*h:
                LList[k][0]='HalfNotePlus'
            else:
                LList[k][0]='WholeNote'
        return (RList, LList)
    def FixMeasSpacing(LList, RList, TS):
        h=-1
        time=16*(int(TS[0])/int(TS[1])) #=6
        while h<len(RList):
            h+=1
            p=-1
            m=0
            for a in RList:
                p+=1
                m+=int(MeasEnder[a[0]])
                if m==time:
                    m=m%time
                elif m>time:
                    m=m%time
                    RList.insert(p+1, list((((MeasEnderRev[str(int(int(MeasEnder[a[0]])/2))])), RList[p][1])))
                    RList.insert(p+1, list((((MeasEnderRev[str(int(int(MeasEnder[a[0]])/2))]),  RList[p][1]))))
                    del RList[p]
                    h=-1
                    break
        h=-1
        while h<len(LList):
            h+=1
            p=-1
            m=0
            for a in LList:
                p+=1
                m+=int(MeasEnder[a[0]])
                if m==time:
                    m=0
                elif m>time:
                    m=m%time
                    LList.insert(p+1, list((((MeasEnderRev[str(int(int(MeasEnder[a[0]])/2))])), LList[p][1])))
                    LList.insert(p+1, list((((MeasEnderRev[str(int(int(MeasEnder[a[0]])/2))]),  LList[p][1]))))
                    del LList[p]
                    h=-1
                    break
        return (LList, RList)
    def CombineRests(LList, RList, TS, BPM):
        g=0
        while g<4:
            g+=1
            p=0
            m=0
 #           print(LList)
            for a in LList:
                p+=1
                k=True
                m+=int(MeasEnder[a[0]])
                time=16*(int(TS[0])/int(TS[1]))
 #               print(a, p)
                if p>=len(LList):
                    break
                if m>=time:
                    m=m%time
                    k=False
    
                if k==True and a[0]==LList[p][0] and a[1]==0 and LList[p][1]==0 and a[0][len(a[0])-4:len(a[0])]!='Plus' and LList[p][0][len(LList[p][0])-4:len(LList[p][0])]!='Plus':
                   # print(a, p)
                    LList.insert(p+1, list((DoubleNote[a[0]], a[1])))
 #                   print(LList[0:p])
                    m+=int(MeasEnder[a[0]])
                    if m>=time:
                        m=m%time
                    del LList[p]
                    del LList[p-1]
                    
            
         
                    
            
            p=0
            m=0
            for a in RList:
                p+=1
                k=True
                m+=int(MeasEnder[a[0]])
                if p>=len(RList):
                    break
                if m>=time:
                    m=m%time
                    k=False
                if k==True and a[0]==RList[p][0] and a[1]==89 and RList[p][1]==89 and a[0][len(a[0])-4:len(a[0])]!='Plus' and RList[p][0][len(RList[p][0])-4:len(RList[p][0])]!='Plus':
                    RList.insert(p+1, list((DoubleNote[a[0]], a[1])))
                    m+=int(MeasEnder[a[0]])
                    if m>=time:
                        m=m%time
                    del RList[p]
                    del RList[p-1]

        return(LList, RList)


        
    def FixBug(NewTimeLis):
        for a in NewTimeLis:
            a[0][0]+=1
            a[0][1]-=1
        return(NewTimeLis)
    def GetYCoord(Note):
        if isinstance(Note, int):
            if Note>39:
                ycoord=76
                ycoord-=3*float(NoteDe[str(Note)])
            elif Note<40:
                ycoord=100 #  97
                ycoord-=3*float(NoteDeL[str(Note)])
            return (ycoord)
        else:
            ycoord=[]
            for a in Note:
                if a>39:
                    b=76
                    b-=3*float(NoteDe[str(a)])
                    ycoord.append(b)
                elif a<40:
                    b=100 #  97
                    b-=3*float(NoteDeL[str(a)])
                    ycoord.append(b)
            return(ycoord)

    def FixPlusRest(LList, RList):
        r=-1
        for a in LList:
            r+=1
            if a[0][len(a[0])-4:len(a[0])]=='Plus' and a[1]==0:
                LList.insert(r+1, list(((a[0][0:len(a[0])-4]), 0)))
                LList.insert(r+1, list(((PlusRemainder[a[0]]), 0)))
                del LList[r]
        r=-1
        for a in RList:
            r+=1
            if a[0][len(a[0])-4:len(a[0])]=='Plus' and a[1]==89:
                RList.insert(r+1, list(((a[0][0:len(a[0])-4]), 89)))
                RList.insert(r+1, list(((PlusRemainder[a[0]]), 89)))
                del RList[r]
        return(LList, RList)
    def GetCoord(RList, LList, TS):
        x=75
        addx=0
        RCoord=[]
        MeasRCoord=[]
        m=0
        time=16*(int(TS[0])/int(TS[1]))
        for a in RList:
            m+=int(MeasEnder[str(a[0])])
     
            RCoord.append(list((x+addx, Note.GetYCoord(a[1]))))
            addx+=int(StfEnder[a[0]])
            if m>=time:
                MeasRCoord.append(x+addx)
    
                addx+=17
                m=m%time
            if addx>1300:
                break

        x=75
        addx=0
        LCoord=[]
        MeasLCoord=[]
        m=0
        
        for a in LList:
            m+=int(MeasEnder[str(a[0])])
            LCoord.append(list((x+addx, Note.GetYCoord(a[1]))))
            addx+=int(StfEnder[a[0]])
            if m>=time:
                MeasLCoord.append(x+addx)
                addx+=17
                m=m%time
            if addx>1300:
                break
        return (RCoord, LCoord, MeasRCoord, MeasLCoord)

    def PlusDot(RList, LList, color, RCoord, LCoord):
        g=-1
        for a in RList:
            g+=1
            if g>=(len(RCoord)):
                break
            if a[0][len(a[0])-4:len(a[0])]=='Plus':
                if isinstance(a[1], int) or isinstance(a[1], float):
                    pygame.draw.circle(screen, color, (int(RCoord[g][0]+14), int(RCoord[g][1]+4)), 2)
                elif isinstance(a[1], list) or isinstance(a[1], tuple):
                    for b in RCoord[g][1]:
                        pygame.draw.circle(screen, color, (int(RCoord[g][0])+14, int(b)+4), 2)

        g=-1
 
        for a in LList:
            g+=1
            if g>=(len(LCoord)):
                break
            #print(a[0][len(a[0])-5:len(a[0])-1])
            if a[0][len(a[0])-4:len(a[0])]=='Plus':
                if isinstance(a[1], int) or isinstance(a[1], float):
                    pygame.draw.circle(screen, color, (int(LCoord[g][0]+14), int(LCoord[g][1]+4)), 2)
                elif isinstance(a[1], list) or isinstance(a[1], tuple):
                    for b in LCoord[g][1]:
                        pygame.draw.circle(screen, color, (int(LCoord[g][0])+14, int(b)+4), 2)
        
        
    def va(RList, RCoord):
        g=-1
        f=0
        for a in RList:
            g+=1
            f+=1
            if g>=(len(RCoord)):
                break
            if isinstance(a[1], int) or isinstance(a[1], float):
                if 89>a[1]>74:
                    screen.blit(vaIMG, (RCoord[g][0], RCoord[g][1]-11))
            elif isinstance(a[1], list) or isinstance(a[1], tuple):
                high=RCoord[g][1][0]
                for b in RCoord[g][1]:
                    if b<high:
                        high=b
                highs=RList[g][1][0]
                for b in RList[g][1]:
                    if b>highs:
                        highs=b
                if 89>highs>74:
                    screen.blit(vaIMG, (RCoord[g][0], high-11))
    def NoteBlit(LCoord, LList, RCoord, RList):
        g=-1
        for a in LCoord:
            g+=1
            if isinstance(a[1], int) or isinstance(a[1], float):
                if LList[g][1] in FlatList:
                    screen.blit(FlatIMG, (a[0]-10, a[1]-5))
                if LList[g][1]>0:
                    if LList[g][0]!='HalfNote' and LList[g][0]!='WholeNote':
                        screen.blit(NoteIMG, a)
                    else:
                        screen.blit(HalfNoteIMG, a)
                else:
                    screen.blit(RestImgs[LList[g][0]], a)
            else:
                d=-1
     #           print(a)
                for b in LList[g][1]:
                    d+=1
                    if b in FlatList:
                        screen.blit(FlatIMG, (a[0]-10, a[1][d]))
                    if b>0:
                        if LList[g][0]!='HalfNote' and LList[g][0]!='WholeNote':
                            screen.blit(NoteIMG, (a[0], a[1][d]))
                        else:
                            screen.blit(HalfNoteIMG, (a[0], a[1][d]))
                    else:
                        screen.blit(RestImgs[LList[g][0]], (a[0], a[1][d]))
        g=-1
        for a in RCoord:
            g+=1
            if isinstance(a[1], int) or isinstance(a[1], float):
                
                if RList[g][1] in SharpList:
                    screen.blit(SharpNoteIMG, (a[0]-6, a[1]-4))
                if RList[g][1]<89:
                    if RList[g][0]!='HalfNote' and RList[g][0]!='WholeNote':
                        screen.blit(NoteIMG, a)
                    else:
                        screen.blit(HalfNoteIMG, a)
                else:
                    screen.blit(RestImgs[RList[g][0]], a)
            else:
                h=0
                for b in a[1]:
                    if RList[g][1][h] in SharpList:
                        screen.blit(SharpNoteIMG, (a[0]-6, a[1][h]-4))
                    if RList[g][1][h]<89:
                        if RList[g][0]!='HalfNote' and RList[g][0]!='WholeNote':
                            #print(a[0], a[1][h])
                            screen.blit(NoteIMG, list((a[0], a[1][h])))
                        else:
                            screen.blit(HalfNoteIMG, list((a[0], a[1][h])))
                    h+=1
    def DrawInputs(InputCoordL, InputCoordR, LList, RList, InputListL, InputListR):
        g=-1
        for a in InputCoordL:
            g+=1
            if InputListL[g][1] in FlatList:
                screen.blit(BlueFlatIMG, (a[0]-10, a[1]-5))
            if InputListL[g][1]>0:
                if LList[g][0]!='HalfNote' and InputListL[g][0]!='WholeNote':
                    screen.blit(BlueNoteIMG, a)
                else:
                    screen.blit(BlueHalfNoteIMG, a)
            else:
                screen.blit(RestImgs[InputListL[g][0]], a)
        g=-1
        for a in InputCoordR:
            g+=1
            if InputListR[g][1] in SharpList:
                screen.blit(BlueSharpNoteIMG, (a[0]-6, a[1]-4))
            if InputListR[g][1]<89:
                if InputListR[g][0]!='HalfNote' and RList[g][0]!='WholeNote':
                    screen.blit(BlueNoteIMG, a)
                else:
                    screen.blit(BlueHalfNoteIMG, a)
            else:
                screen.blit(RestImgs[RList[g][0]], a)

                        
