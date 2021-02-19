#!/usr/bin/python3

import time
import pygame 
from tkinter import *

# Funktionen
def calculateTiming(bpmIn):
    tempoIn = 1000/(bpmIn/60*2)
    tempoIn = int(tempoIn)
    return tempoIn

def changeTempo(event):
    global tempo
    global bpm 
    bpm = (scaleBpm.get())
    tempo = calculateTiming(bpm)

"""def changeVolume(event):
    print(scaleKick.get())"""

def lulu(track,value):
    value = value*0.1
    track.set_volume(value)

    #if track == kick:
    #    kick.set_volume(value)

    print(value)
    #print(lala.set_volume())


def noteOnOff(x):
    if x > 100 and x < 200:
        y = 0
        z = x-101
        theList = button_list_kick
    elif x > 200 and x < 300:
        y = 1
        z = x-201
        theList = button_list_snare
    elif x > 300 and x < 400:
        y = 2
        z = x-301
        theList = button_list_hihat
    elif x > 400 and x < 500:
        y = 3
        z = x-401
        theList = button_list_crash
    else:
        print("falscher Wert")
    if pattern[y][z]==0:
        pattern[y][z] = 1
        theList[z].config(bg="blue")
    else:
        pattern[y][z] = 0
        theList[z].config(bg="grey")

def letsGo():
    global isPlaying
    global zaehler
    global pattern
    global tempo
    markStep(zaehler)
    stand = startButton.cget('text')

    if isPlaying == TRUE:
        if pattern[0][zaehler] == 1:
            kick.play()
        if pattern[1][zaehler] == 1:
            snare.play()           
        if pattern[2][zaehler] == 1:
            hihat.play()
        if pattern[3][zaehler] == 1:
            crash.play()
        root.after(tempo, letsGo)
        zaehler = zaehler+1
        if zaehler >= 16:
            zaehler = 0
    else:
        isPlaying = TRUE

def stopSequencer():
    global isPlaying
    global zaehler
    if isPlaying == FALSE:
        isPlaying = TRUE
    elif isPlaying == TRUE:
        isPlaying = FALSE
        unMarkStep(zaehler)
        zaehler = 0
        
def markStep(currentStep):
    global isPlaying
    if isPlaying == TRUE:
        label_list_step[currentStep].config(bg="red")
        label_list_step[currentStep-1].config(bg="gray")

def unMarkStep(currentStep):
    label_list_step[currentStep-1].config(bg="gray")
    print(currentStep)

def hello(event):
    event.widget['bg'] = "#990000"

# Reaktion auf das Programmende
def win_close () :
    print("tschöööö")
    # Aufräumarbeiten ..
    root.quit()


# Sounds
pygame.init()
kick = pygame.mixer.Sound('kick.wav')
snare = pygame.mixer.Sound('snare.wav')
hihat = pygame.mixer.Sound('hihatlong.wav')
hihat.set_volume(0.4)
crash = pygame.mixer.Sound('crash.ogg')
crash.set_volume(0.5)

# Sequencer values
pattern =  [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

zaehler = 0
isPlaying = TRUE
bpm = 120
tempo = calculateTiming(bpm)


# Tkinter 
root = Tk()
root.wm_title("Drumsi")
root.config(background = "gray")

# Frames

leftFrame = Frame(root, width = 50, height = 300)
leftFrame.grid(row = 0, column = 0)

rightFrame = Frame(root, width = 350, height = 100)
rightFrame.grid(row = 0, column = 1)

topFrame = Frame(rightFrame, width=350, height=50)
topFrame.grid(row=0, column=1, padx=6, pady=6, sticky="w")

controlFrame = Frame(topFrame, width=350, height=50)
controlFrame.grid(row=0, column=0, padx=6, pady=6, sticky="w")

buttonFrame = Frame(rightFrame, width=600, height=50)
buttonFrame.grid(row=1, column=1, padx=6, pady=6)

mixerFrame = Frame(topFrame, width=350, height=50)
mixerFrame.grid(row=0, column=1)


# Mixer slider
scaleKick = Scale(mixerFrame, from_=10, to=0, command=lambda x:lulu(kick,scaleKick.get()))
scaleKick.grid(row=0, column=0, pady=6)
scaleKick.set(10)
#scaleKick.bind('<ButtonRelease-1>', changeVolume)

scaleSnare = Scale(mixerFrame, from_=10, to=0, command=lambda x:lulu(snare,scaleSnare.get()))
scaleSnare.grid(row=0, column=1, pady=6)
scaleSnare.set(10)
#scaleSnare.bind('<ButtonRelease-1>', changeVolume)

scaleHiHat = Scale(mixerFrame, from_=10, to=0, command=lambda x:lulu(hihat,scaleHiHat.get()))
scaleHiHat.grid(row=0, column=2, pady=6)
scaleHiHat.set(10)
#scaleHiHat.bind('<ButtonRelease-1>', changeVolume)

scaleCrash = Scale(mixerFrame, from_=10, to=0, command=lambda x:lulu(crash,scaleCrash.get()))
scaleCrash.grid(row=0, column=3, pady=6)
scaleCrash.set(10)
#scaleCrash.bind('<ButtonRelease-1>', changeVolume)

scaleBpm = Scale(controlFrame, from_=60, to=240, resolution=5, orient=HORIZONTAL, length=200)
scaleBpm.set(bpm)
scaleBpm.grid(row=2, column=0, padx=10, pady=3)   
scaleBpm.bind('<ButtonRelease-1>', changeTempo)

# Drum buttons
numberButtons = range(1,17)
label_list_step = []

for i in numberButtons:
    stepLabel = Label(buttonFrame, text=i, bg="gray", width=3)
    stepLabel.grid(row=0, column=i, padx=3, pady=3)
    label_list_step.append(stepLabel)

#button_names = [1,2,3,4,5,6,7,8]
button_list = [] # for later needs

button_list_kick = [] 
button_list_snare = [] 
button_list_hihat = [] 
button_list_crash = [] 

# creating buttons
for i in numberButtons:
    kickButton = Button(buttonFrame, text="", command=lambda x=i:noteOnOff(x+100))
    kickButton.grid(row=1, column=i, padx=3, pady=3)
    button_list_kick.append(kickButton) 

for i in numberButtons:
    snareButton = Button(buttonFrame, text="", command=lambda x=i:noteOnOff(x+200))
    snareButton.grid(row=2, column=i, padx=3, pady=3)
    button_list_snare.append(snareButton) 

for i in numberButtons:
    hihatButton = Button(buttonFrame, text="", command=lambda x=i:noteOnOff(x+300))
    hihatButton.grid(row=3, column=i, padx=3, pady=3)
    button_list_hihat.append(hihatButton) 

for i in numberButtons:
    crashButton = Button(buttonFrame, text="", command=lambda x=i:noteOnOff(x+400))
    crashButton.grid(row=4, column=i, padx=3, pady=3)
    button_list_crash.append(crashButton) 

# Command buttons
startButton = Button(controlFrame, text="Play", bg="#FFFFFF", width=6, command=letsGo)
startButton.grid(row=0, column=0, sticky="w", padx=3, pady=3)
#startButton.bind('<Button-1>', letsGo)

stopButton = Button(controlFrame, text="Stop", bg="#FFFFFF", width=6, command=stopSequencer)
stopButton.grid(row=0, column=0, sticky="e", padx=3, pady=3)

label_names = ["Step", "Kick", "Snare", "Hihat", "Crash"]

f = 0
for l in label_names:
    test = Label(buttonFrame, text = label_names[f], width = 5, anchor="e")
    test.grid(row=f, column = 0, sticky="w")
    f = f+1

print(label_names[0])


root.protocol("WM_DELETE_WINDOW",win_close)

# Update der GUI
root.mainloop()

