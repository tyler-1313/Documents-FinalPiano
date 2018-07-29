import pygame.midi
import pygame
from FinalDraw import *
from FinalNote import *
from Lines import *
from MMenu import *
import pygame_textinput
import random

pygame.init()
pygame.fastevent.init()
event_get = pygame.fastevent.get
event_post = pygame.fastevent.post
pygame.midi.init()

# Change this to override use of default input device
device_id = None
if device_id is None:
    input_id = pygame.midi.get_default_input_id()
else:
    input_id = device_id
i = pygame.midi.Input( input_id )

myfonts = pygame.font.SysFont('Comic Sans MS', 14)
MainMenu = myfonts.render('MainMenu', False, (0, 0, 0))
Library = myfonts.render('Library', False, (0, 0, 0))

white=(255,255,255)
black=(0,0,0)
blue=(0,255,255)
darkblue=(0,0,255)
size=(1300,900)
screen=pygame.display.set_mode(size)
FullPianoIMG=pygame.image.load('FullPiano.png')
SharpIMG=pygame.image.load('SharpD.png')
BassIMG=pygame.image.load('Bass.png')
TrebleIMG=pygame.image.load('Treble4.png')
NoteIMG=pygame.image.load('Note.png')
BlueNoteIMG=pygame.image.load('BlueNote.png')
HalfNoteIMG=pygame.image.load('HalfNote.png')
FlatIMG=pygame.image.load('Flat.png')
SharpNoteIMG=pygame.image.load('Sharp.png')
BlueHalfNoteIMG=pygame.image.load('BlueHalfNote.png')
BlueSharpNoteIMG=pygame.image.load('BlueSharp.png')
BlueFlatIMG=pygame.image.load('BlueFlat.png')


vaIMG=pygame.image.load('vaIMG.png')
vbIMG=pygame.image.load('vbIMG.png')

EthNoteTailIMG=pygame.image.load('EthTail.png')
RevEthNoteTailIMG=pygame.image.load('RevEthTail.png')

SixteenthNoteRestIMG=pygame.image.load('16thRest.png')
EthNoteRestIMG=pygame.image.load('8thNoteRest.png')
FourthNoteRestIMG=pygame.image.load('4thNoteRest.png')
HalfNoteRestIMG=pygame.image.load('HalfNoteRest.png')
WholeNoteRestIMG=pygame.image.load('WholeNoteRest.png')
StfEnder={'SixteenthNote':'16', 'SixteenthNotePlus':'24', 'EthNote':'32', 'EthNotePlus':'48', 'FourthNote':'64',
           'FourthNotePlus':'96', 'HalfNote':'128', 'HalfNotePlus':'192', 'WholeNote':'256'
          }
MeasEnderRev={'1':'SixteenthNote', '1.5':'SixteenthNotePlus', '2':'EthNote', '3':'EthNotePlus', '4':'FourthNote',
           '6':'FourthNotePlus', '8':'HalfNote', '12':'HalfNotePlus', '16':'WholeNote'}
MeasEnder={'SixteenthNote':'1', 'SixteenthNotePlus':'1.5', 'EthNote':'2', 'EthNotePlus':'3', 'FourthNote':'4',
           'FourthNotePlus':'6', 'HalfNote':'8', 'HalfNotePlus':'12', 'WholeNote':'16'}
RestImgs={'SixteenthNote':SixteenthNoteRestIMG, 'EthNote':EthNoteRestIMG, 'FourthNote':FourthNoteRestIMG,
          'HalfNote':HalfNoteRestIMG, 'WholeNote':WholeNoteRestIMG}
Convert={'WholeNote':'45'}
Trans={'1':'16', '2':'8', '4':'4', '8':'2', '16':'1'}

FlatList=[2,5,7,10,12,14,17,19,22,24,26,29,31,34,36,38]
           
SharpList=[41,43,46,48,50,53,55,58,60,
           62, 65,67,70, 72,74,77,79,82,84,86]

TS=['','1']
BPM=''
RCoordBlue=[]
RListBlue=[]
LCoordBlue=[]
LListBlue=[]
InputListR=[]
InputListL=[]
RNow=[89]
LNow=[0]
CurrentPlaying=[]
InputMarkerR=0
InputMarkerL=0
marker=1
CSVFile='FurElise.csv'
NewTimeList=[]
RList=[['EthNote', 45]]
LList=[['EthNote', 35]]
state='MMenu'

boxone=True
boxtwo=False
boxthree = False
boxfour=False
boxfive=False
boxsix=False
inp=False
inb = False
inc=False
ind=False
ine=False
inf=False
chordbox=False
go=False
NoteTypeList=['WholeNote']
NoteType=16
includechords=True
rangemin =''
rangemax=''
NumNotes=''

textinput = pygame_textinput.TextInput()
textinputtwo = pygame_textinput.TextInput()
textinputthree = pygame_textinput.TextInput()
textinputfour = pygame_textinput.TextInput()
textinputfive = pygame_textinput.TextInput()
textinputsix = pygame_textinput.TextInput()

while True:
    events=pygame.event.get()
    mouse=pygame.mouse.get_pos()
    screen.fill(white)
    if state=='NewCSV':
 #       j=Note.GetNoteList(CSVFile)
     #  j=[[[0, 960], 0], ...]
        j=NewTimeList
        LList, RList= Note.GetRLLists(j)
     #  LList=[[[0, 960], 0], ((960, 2880), 0), ...]
        RList, LList = Note.FindChords(RList, LList)
        # RList= [[[0,960], [45, 51]], ...]     
        LList, RList= Note.Reduce(LList, RList)
     #  LList=[[960, 0], [1920, 0], ...]
        RList, LList=Note.BreakUpBigRests(RList, LList, TS, BPM)
     #  LList=[[[250.0, 0], [250.0, 0], ...]
        LList, RList=Note.GetMeasLists(LList, RList, TS, BPM)
     #  L/RList = [['EthNote', 39], [...], ...]]
        LList, RList=Note.CombineRests(LList, RList, TS, BPM)
     #  LList=[['HalfNote', 0], ['FourthNote', 0], ...]
        LList, RList=Note.FixMeasSpacing(LList, RList, TS)
     #  LList=[['FourthNote', 0], ['EthNote', 0], ...]
        LList, RList=Note.FixPlusRest(LList, RList)  
     #  LList=[['FourthNote', 0], ['EthNote', 0], ...]
        NewTimeList=Note.FixBug(j)
        state=''
        marker=0
    
        
 # Note, Lines, Draw

 #  NewTimeList=[[[1, 959], 0], ([961, 1199], 56), ...]
    if state=='':
        Draw.Rects(NewTimeList, marker)

        pygame.draw.rect(screen, white, (0,0,1300,250)) #block for sheet music
        pygame.draw.rect(screen, white, (0,500,1300,400))
        screen.blit(FullPianoIMG, (0,500))
        Draw.GrandStaff(TS)
        
        RCoord, LCoord, MeasRCoord, MeasLCoord=Note.GetCoord(RList, LList, TS)

        Note.va(RList, RCoord)
        Note.PlusDot(RList, LList, black, RCoord, LCoord)
        
        Note.NoteBlit(LCoord, LList, RCoord, RList)
        Lines.MeasLines(MeasLCoord, MeasRCoord)                            
                   
        Lines.LedgerLines(RList, RCoord, LList, LCoord)                       

        for e in events:
            if e.type in [pygame.midi.MIDIIN]:
                
                if e.status==144:
                    CurrentPlaying.append(e.data1-20)
                    if e.data1-20>39:
                        if RNow==[89]:
                            RNow.remove(89)
                        RNow.append(e.data1-20)
                    else:
                        if LNow==[0]:
                            LNow.remove(0)
                        LNow.append(e.data1-20)
                    for a in CurrentPlaying:
                        if a==0:
                            CurrentPlaying.remove(0)
                if e.status==128:
                    CurrentPlaying.remove(e.data1-20)
                    if CurrentPlaying==[]:
                        CurrentPlaying.append(0)
                    if e.data1-20>39:
                        RNow.remove(e.data1-20)
                        if RNow==[]:
                            RNow.append(89)
                    else:
                        LNow.remove(e.data1-20)
                        if LNow==[]:
                            LNow.append(0)
        g=-1
        Rscore=0
        Lscore=0
        if len(CurrentPlaying)>0:
            while g+1<len(CurrentPlaying):
                g+=1
                if 89>CurrentPlaying[g]>39:
                    Rscore+=1
                if 0<CurrentPlaying[g]<40:
                    Lscore+=1
        if Rscore==0:
            if 89 not in CurrentPlaying:
                CurrentPlaying.append(89)
        else:
            if 89 in CurrentPlaying:
                CurrentPlaying.remove(89)
        if Lscore==0:
            if 0 not in CurrentPlaying:
                CurrentPlaying.append(0)
        else:
            if 0 in CurrentPlaying:
                CurrentPlaying.remove(0) 
        CheckList=[]
        for a in NewTimeList:
            if a[0][0]<=marker<=a[0][1]:
                CheckList.append(a[1])
        Combined=[]
        for a in CheckList:
            for b in CurrentPlaying:
                if a==b:
                    Combined.append(a)

        if CheckList==Combined:
            marker+=110  #Arbitrary number- change to match Note Length

        Draw.CurrentNotes(CurrentPlaying)
        if len(RList)>InputMarkerR:
            if isinstance(RNow, list) and len(RNow)==1:
                if RNow[0]==RList[InputMarkerR][1]:
                    InputListR.append(list((RList[InputMarkerR][0], RNow[0])))
                    InputMarkerR+=1
            else:
                if RNow==RList[InputMarkerR][1]:
                    InputListR.append(list((RList[InputMarkerR][0], RNow)))
                    InputMarkerR+=1
        if len(LList)>InputMarkerL:
           # print(InputMarkerL)
            if isinstance(LNow, list) and len(LNow)==1:
                if LNow[0]==LList[InputMarkerL][1]:
                    InputListL.append(list((LList[InputMarkerL][0], LNow[0])))
                    InputMarkerL+=1
            else:
                if LNow==LList[InputMarkerL][1]:
                    InputListL.append(list((RList[InputMarkerL][0], LNow)))
                    InputMarkerL+=1

        InputCoordR, InputCoordL, InputMeasR, InputMeasL=Note.GetCoord(InputListR, InputListL, TS)
        Note.DrawInputs(InputCoordL, InputCoordR, LList, RList, InputListL, InputListR)

        Lines.SingleNotesR(RCoord, RList, black, TS)
        Lines.SingleNotesL(LCoord, LList, black, TS)
        
        Lines.MultiNotesR(RCoord, RList, black, TS)
        Lines.MultiNotesL(LCoord, LList, black, TS)

        Lines.SingleNotesR(InputCoordR, InputListR, blue, TS)
        Lines.SingleNotesL(InputCoordL, InputListL, blue, TS)
        Lines.MultiNotesR(InputCoordR, InputListR, blue, TS)
        Lines.MultiNotesL(InputCoordL, InputListL, blue, TS)
        
        time=16*(int(TS[0])/int(TS[1]))
        Rstf=0
        Rmark=0
        rm=0
        Rcheck=False
        for a in InputListR:
            Rstf+=int(StfEnder[a[0]])
            Rmark+=1
            rm+=int(MeasEnder[a[0]])
            if Rstf>935 and rm>=time:
                Rcheck=True
                break
            if rm>=time:
                rm=rm%time
        Lstf=0
        Lmark=0
        lm=0
        Lcheck=False
        for a in InputListL:
            Lstf+=int(StfEnder[a[0]])
            Lmark+=1
            lm+=int(MeasEnder[a[0]])
            if Lstf>935 and lm>=time:
                Lcheck=True
                break
            if lm>=time:
                lm=lm%time
                
        if Lcheck and Rcheck:
            del InputListR[0:Rmark+1]
            del InputListL[0:Lmark+1]
            del RList[0:Rmark+1]
            del LList[0:Lmark+1]
            InputMarkerR-=Rmark+1
            InputMarkerL-=Lmark+1
            if InputMarkerR<0:
                InputMarkerR=0
            if InputMarkerL<0:
                InputMarkerL=0
        Note.PlusDot(InputListR, InputListL, blue, InputCoordR, InputCoordL)
        pygame.draw.rect(screen, white, (0, 50, 10, 150))


    Menu.MainMenu(state)
    Menu.Practice(state, boxone,boxtwo,boxthree,boxfour,boxfive, chordbox)
    Menu.Learn(state)
    Menu.Library(state)
    TSOne=myfont.render(str(TS[1]), False, (0,0,0))
    if state=='':
        screen.blit(MainMenu, (1150, 180))
        
   
    for e in events:
        if state=='':
            if e.type == pygame.MOUSEBUTTONDOWN:
                if 1220>=mouse[0]>=1150 and  200>=mouse[1]>=180:
                    state='MMenu'
                
        if state=='MMenu':

            if e.type == pygame.MOUSEBUTTONDOWN:
                if 400>=mouse[0]>=300 and  300>=mouse[1]>=200:
                    state='Learn'
                elif 400>=mouse[0]>=300 and 400>=mouse[1]>=300:
                    state='Practice'
                elif 400>=mouse[0]>=300 and 500>=mouse[1]>=400:
                    state='Library'

        elif state=='Practice': #TS, Notes

            if e.type == pygame.MOUSEBUTTONDOWN:
                if 330>=mouse[0]>=300 and  190>=mouse[1]>=160:
                    inp, inb, inc, ind, ine, inf=Menu.SettoFalse(inp, inb, inc, ind, ine, inf)
                elif 380>=mouse[0]>=350 and 190>=mouse[1]>=160:
                    inb, inp, inc, ind, ine, inf=Menu.SettoFalse(inb, inp, inc, ind, ine, inf)
                elif 493>=mouse[0]>=450 and 305>=mouse[1]>=277:
                    inc, inp, inb, ind, ine, inf=Menu.SettoFalse(inc, inp, inb, ind, ine, inf)
                elif 460>=mouse[0]>=430 and 430>=mouse[1]>=400:
                    ind, inp, inb, inc, ine, inf=Menu.SettoFalse(ind, inp, inb, inc, ine, inf)
                elif 485>=mouse[0]>=455 and 480>=mouse[1]>=450:
                    inf, inp, inb, ind, ine, inc=Menu.SettoFalse(inf, inp, inb, ind, ine, inc)
                    
                elif 420>=mouse[0]>=410 and 258>=mouse[1]>=248:
                        boxone, boxtwo, boxthree, boxfour, boxfive, boxsix=Menu.SettoFalse(boxone, boxtwo, boxthree, boxfour, boxfive, boxsix)
                        NoteTypeList=['WholeNote']
                        NoteType=16
                        TS[1]='1'
                elif 458>=mouse[0]>=448 and 258>=mouse[1]>=248:
                        boxtwo, boxone, boxthree, boxfour, boxfive, boxsix=Menu.SettoFalse(boxone, boxtwo, boxthree, boxfour, boxfive, boxsix)
                        NoteTypeList=['HalfNote']
                        NoteType=8
                        TS[1]='2'
                elif 496>=mouse[0]>=486 and 258>=mouse[1]>=248:
                        boxthree, boxtwo, boxone, boxfour, boxfive, boxsix=Menu.SettoFalse(boxone, boxtwo, boxthree, boxfour, boxfive, boxsix)
                        NoteTypeList=['FourthNote']
                        NoteType=4
                        TS[1]='4'
                elif 534>=mouse[0]>=524 and 258>=mouse[1]>=248:
                        boxfour, boxtwo, boxthree, boxone, boxfive, boxsix=Menu.SettoFalse(boxone, boxtwo, boxthree, boxfour, boxfive, boxsix)
                        NoteTypeList=['EthNote']
                        NoteType=2
                        TS[1]='8'
                elif 572>=mouse[0]>=562 and 258>=mouse[1]>=248:
                        boxfive, boxtwo, boxthree, boxfour, boxone, boxsix=Menu.SettoFalse(boxone, boxtwo, boxthree, boxfour, boxfive, boxsix)
                        NoteTypeList=['SixteenthNote']
                        NoteType=1
                        TS[1]='16'
                    
                elif 430>=mouse[0]>=420 and 358>=mouse[1]>=348:
                    if chordbox==1:
                        chordbox=2
                    else:
                        chordbox=1
                    inp=False
                    inc=False
                    inb=False
                elif 640>=mouse[0]>=600 and 540>=mouse[1]>=500:
                    go=True
                    state=''
                
                else:
                    inp=False
                    inb=False
                    inc=False
            elif e.type == pygame.KEYDOWN:
                if inp:
                    if e.key == pygame.K_BACKSPACE:
                        rangemin = rangemin[:-1]
                    else:
                        rangemin += e.unicode
                if inb:
                    if e.key == pygame.K_BACKSPACE:
                        rangemax = rangemin[:-1]
                    else:
                        rangemax += e.unicode
                if inc:
                    if e.key == pygame.K_BACKSPACE:
                        NumNotes = NumNotes[:-1]
                    else:
                        NumNotes += e.unicode
                if ind:
                    if e.key == pygame.K_BACKSPACE:
                        TS[0] = TS[0][:-1]
                    else:
                        TS[0] += e.unicode
                if inf:
                    if e.key == pygame.K_BACKSPACE:
                        BPM = BPM[:-1]
                    else:
                        BPM += e.unicode

        elif state=='Library': #TS, Notes
            pass 












    
    if inp==True:
        textinput.update(events)
    if inb==True:
        textinputtwo.update(events)
    if inc==True:
        textinputthree.update(events)
    if ind==True:
        textinputfour.update(events)
    if inf==True:
        textinputsix.update(events)

    if state=='Practice':
        screen.blit(textinput.get_surface(), (302, 163))
        screen.blit(textinputtwo.get_surface(), (352, 163))
        screen.blit(textinputthree.get_surface(), (452, 280))
        screen.blit(textinputfour.get_surface(), (432, 402))  
        screen.blit(textinputsix.get_surface(), (452, 457))
        screen.blit(TSOne, (485, 394))

    if go==True:
        BPM=int(BPM)
        RList=[]
        LList=[]
        NewTimeList=[]
        InputMarkerR=0
        InputMarkerL=0
        InputListR=[]
        InputListL=[]
        h=((60/BPM)*1000)/int(Trans[str(TS[1])]) # 16th note length
        h=int(h)
        g=0
        d=0
        while g<int(NumNotes):
            g+=1
            s=h*NoteType
            j=2
            k=random.randint(int(rangemin), int(rangemax))
            f=random.randint(0,3)
            if chordbox:
                j=random.randint(1,2)
            if j==1 and 40>k>32:
                k=32
            if j==1 and k>81:
                k=81
            if j==2:
                NewTimeList.append(list(([d, s+d], k)))
                if k>39:
                    NewTimeList.append(list(([d, s+d], 0)))
                else:
                    NewTimeList.append(list(([d, s+d], 89)))
            else:
                if f==3:
                    NewTimeList.append(list(([d, s+d], k)))
                    NewTimeList.append(list(([d, s+d], k+4)))
                    if k>39:
                        NewTimeList.append(list(([d, s+d], 0)))
                    else:
                        NewTimeList.append(list(([d, s+d], 89)))
                    
                elif f==2:
                    NewTimeList.append(list(([d, s+d], k)))
                    NewTimeList.append(list(([d, s+d], k+7)))
                    if k>39:
                        NewTimeList.append(list(([d, s+d], 0)))
                    else:
                        NewTimeList.append(list(([d, s+d], 89)))
                        
                elif f==1:
                    NewTimeList.append(list(([d, s+d], k)))
                    NewTimeList.append(list(([d, s+d], k+3)))
                    NewTimeList.append(list(([d, s+d], k+7)))
                    if k>39:
                        NewTimeList.append(list(([d, s+d], 0)))
                    else:
                        NewTimeList.append(list(([d, s+d], 89)))
                else:
                    NewTimeList.append(list(([d, s+d], k)))
                    NewTimeList.append(list(([d, s+d], k+4)))
                    NewTimeList.append(list(([d, s+d], k+7)))
                    if k>39:
                        NewTimeList.append(list(([d, s+d], 0)))
                    else:
                        NewTimeList.append(list(([d, s+d], 89)))
            d+=s
        go=''
        state='NewCSV'

     
        

           
            
       # elif state=='Library':
#            pass

    
    pygame.display.update()
    if i.poll():
        midi_events = i.read(10)
        midi_evs = pygame.midi.midis2events(midi_events, i.device_id)
        for m_e in midi_evs:
            event_post( m_e )
pygame.quit()
    
