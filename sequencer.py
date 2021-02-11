#!/usr/bin/python3

import time
import pygame 
from tkinter import *
#pushtest

pygame.init()

kick = pygame.mixer.Sound('kick.wav')
snare = pygame.mixer.Sound('snare.wav')
hihat = pygame.mixer.Sound('hihatlong.wav')
hihat.set_volume(0.4)

pattern =  [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

zaehler = 0

bpm = 120

#sequencerVariables
isPlaying = True



def calculateTiming(bpmIn):
    tempoIn = 1000/(bpmIn/60*2)
    tempoIn = int(tempoIn)
    return tempoIn

tempo = calculateTiming(bpm)

root = Tk()
root.wm_title("Drumsi")
root.config(background = "#000000")

topFrame = Frame(root, width=350, height=50)
topFrame.grid(row=0, column=0, padx=3, pady=3)

buttonFrame = Frame(root, width=600, height=50)
buttonFrame.grid(row=1, column=0, padx=3, pady=3)

def changeTempo(event):
    global tempo
    global bpm 

    bpm = (Slider.get())
    tempo = calculateTiming(bpm)
    print(tempo)
	
Slider = Scale(topFrame, from_=60, to=200, resolution=5, orient=HORIZONTAL, length=400)
Slider.set(bpm)
Slider.grid(row=1, column=0, padx=10, pady=3)   
Slider.bind('<ButtonRelease-1>', changeTempo)

styleButtonWidth = 1
styleButtonColor = "#FFFFFF"
styleButtonPadX = 3
styleButtonPadY = 3

def noteOnOff(x):
    if x > 100 and x < 200:
        if pattern[0][x-101]==0:
            pattern[0][x-101] = 1
            #event.widget['bg'] = "#990000"
        else:
            pattern[0][x-101] = 0
            #event.widget['bg'] = "#660033"  
    elif x > 200 and x < 300:
        if pattern[1][x-201]==0:
            pattern[1][x-201] = 1
            #event.widget['bg'] = "#990000"
        else:
            pattern[1][x-201] = 0
            #event.widget['bg'] = "#660033"
    elif x > 300 and x < 400:
        if pattern[2][x-301]==0:
            pattern[2][x-301] = 1
            #event.widget['bg'] = "#990000"
        else:
            pattern[2][x-301] = 0
            #event.widget['bg'] = "#660033"
    elif x > 400 and x < 500:
        if pattern[3][x-401]==0:
            pattern[3][x-401] = 1
            #event.widget['bg'] = "#990000"
        else:
            pattern[3][x-401] = 0
            #event.widget['bg'] = "#660033"
    else:
        print("falscher Wert")
    print(pattern)


def letsGo():
    global isPlaying
    global zaehler
    global pattern
    global tempo

    stand = startButton.cget('text')
    print(stand)
    if stand == "lets go":
        if pattern[0][zaehler] == 1:
            kick.play()
        if pattern[1][zaehler] == 1:
            snare.play()           
        if pattern[2][zaehler] == 1:
            hihat.play()

        root.after(tempo, letsGo)
        zaehler = zaehler+1
        if zaehler >= 8:
            zaehler = 0
        print(zaehler)
    else:
        print(jo)




button_names = [1,2,3,4,5,6,7,8]
button_list = [] # for later needs

# 16 buttons for 16 steps
numberButtons = range(1,17)

for i in numberButtons:
    kickButton = Button(buttonFrame, text=i, command=lambda x=i:noteOnOff(x+100))
    kickButton.grid(row=1, column=i-1, padx=styleButtonPadX, pady=styleButtonPadY)
    button_list.append(kickButton) 

for i in numberButtons:
    snareButton = Button(buttonFrame, text=i, command=lambda x=i:noteOnOff(x+200))
    snareButton.grid(row=2, column=i-1, padx=styleButtonPadX, pady=styleButtonPadY)
    button_list.append(snareButton) 

for i in numberButtons:
    hihatButton = Button(buttonFrame, text=i, command=lambda x=i:noteOnOff(x+300))
    hihatButton.grid(row=3, column=i-1, padx=styleButtonPadX, pady=styleButtonPadY)
    button_list.append(hihatButton) 

for i in numberButtons:
    crashButton = Button(buttonFrame, text=i, command=lambda x=i:noteOnOff(x+400))
    crashButton.grid(row=4, column=i-1, padx=styleButtonPadX, pady=styleButtonPadY)
    button_list.append(crashButton) 

print(button_list)

def lable_name(name):
    label = Label(buttonFrame, text="HDD {} is added to the zpool".format(name))
    label.pack()

def sendNote(receivedNote):
    print("hi",receivedNote)








"""
Kick_B1 = Button(buttonFrame, text="1", bg=styleButtonColor, width=styleButtonWidth, command= lambda: say_hi("fuck"))
Kick_B1.grid(row=0, column=0, padx=styleButtonPadX, pady=styleButtonPadY)
#Kick_B1.bind('<Button-1>', noteOnOff)

Kick_B2 = Button(buttonFrame, text="2", bg=styleButtonColor, width=styleButtonWidth)
Kick_B2.grid(row=0, column=1, padx=styleButtonPadX, pady=styleButtonPadY)
Kick_B2.bind('<Button-1>', noteOnOff)

Kick_B3 = Button(buttonFrame, text="3", bg=styleButtonColor, width=styleButtonWidth)
Kick_B3.grid(row=0, column=2, padx=styleButtonPadX, pady=styleButtonPadY)
Kick_B3.bind('<Button-1>', noteOnOff)

Kick_B4 = Button(buttonFrame, text="4", bg=styleButtonColor, width=styleButtonWidth)
Kick_B4.grid(row=0, column=3, padx=styleButtonPadX, pady=styleButtonPadY)
Kick_B4.bind('<Button-1>', noteOnOff)

Kick_B5 = Button(buttonFrame, text="5", bg=styleButtonColor, width=styleButtonWidth)
Kick_B5.grid(row=0, column=4, padx=styleButtonPadX, pady=styleButtonPadY)
Kick_B5.bind('<Button-1>', noteOnOff)

Kick_B6 = Button(buttonFrame, text="6", bg=styleButtonColor, width=styleButtonWidth)
Kick_B6.grid(row=0, column=5, padx=styleButtonPadX, pady=styleButtonPadY)
Kick_B6.bind('<Button-1>', noteOnOff)

Kick_B7 = Button(buttonFrame, text="7", bg=styleButtonColor, width=styleButtonWidth)
Kick_B7.grid(row=0, column=6, padx=styleButtonPadX, pady=styleButtonPadY)
Kick_B7.bind('<Button-1>', noteOnOff)

Kick_B8 = Button(buttonFrame, text="8", bg=styleButtonColor, width=styleButtonWidth)
Kick_B8.grid(row=0, column=7, padx=styleButtonPadX, pady=styleButtonPadY)
Kick_B8.bind('<Button-1>', noteOnOff)


Snare_B1 = Button(buttonFrame, text="1", bg=styleButtonColor, width=styleButtonWidth)
Snare_B1.grid(row=1, column=0, padx=styleButtonPadX, pady=styleButtonPadY)
Snare_B1.bind('<Button-1>', noteOnOff)

Snare_B2 = Button(buttonFrame, text="2", bg=styleButtonColor, width=styleButtonWidth)
Snare_B2.grid(row=1, column=1, padx=styleButtonPadX, pady=styleButtonPadY)
Snare_B2.bind('<Button-1>', noteOnOff)

Snare_B3 = Button(buttonFrame, text="3", bg=styleButtonColor, width=styleButtonWidth)
Snare_B3.grid(row=1, column=2, padx=styleButtonPadX, pady=styleButtonPadY)
Snare_B3.bind('<Button-1>', noteOnOff)

Snare_B4 = Button(buttonFrame, text="4", bg=styleButtonColor, width=styleButtonWidth)
Snare_B4.grid(row=1, column=3, padx=styleButtonPadX, pady=styleButtonPadY)
Snare_B4.bind('<Button-1>', noteOnOff)

Snare_B5 = Button(buttonFrame, text="5", bg=styleButtonColor, width=styleButtonWidth)
Snare_B5.grid(row=1, column=4, padx=styleButtonPadX, pady=styleButtonPadY)
Snare_B5.bind('<Button-1>', noteOnOff)

Snare_B6 = Button(buttonFrame, text="6", bg=styleButtonColor, width=styleButtonWidth)
Snare_B6.grid(row=1, column=5, padx=styleButtonPadX, pady=styleButtonPadY)
Snare_B6.bind('<Button-1>', noteOnOff)

Snare_B7 = Button(buttonFrame, text="7", bg=styleButtonColor, width=styleButtonWidth)
Snare_B7.grid(row=1, column=6, padx=styleButtonPadX, pady=styleButtonPadY)
Snare_B7.bind('<Button-1>', noteOnOff)

Snare_B8 = Button(buttonFrame, text="8", bg=styleButtonColor, width=styleButtonWidth)
Snare_B8.grid(row=1, column=7, padx=styleButtonPadX, pady=styleButtonPadY)
Snare_B8.bind('<Button-1>', noteOnOff)


HiHat_B1 = Button(buttonFrame, text="1", bg=styleButtonColor, width=styleButtonWidth)
HiHat_B1.grid(row=2, column=0, padx=styleButtonPadX, pady=styleButtonPadY)
HiHat_B1.bind('<Button-1>', noteOnOff)

HiHat_B2 = Button(buttonFrame, text="2", bg=styleButtonColor, width=styleButtonWidth)
HiHat_B2.grid(row=2, column=1, padx=styleButtonPadX, pady=styleButtonPadY)
HiHat_B2.bind('<Button-1>', noteOnOff)

HiHat_B3 = Button(buttonFrame, text="3", bg=styleButtonColor, width=styleButtonWidth)
HiHat_B3.grid(row=2, column=2, padx=styleButtonPadX, pady=styleButtonPadY)
HiHat_B3.bind('<Button-1>', noteOnOff)

HiHat_B4 = Button(buttonFrame, text="4", bg=styleButtonColor, width=styleButtonWidth)
HiHat_B4.grid(row=2, column=3, padx=styleButtonPadX, pady=styleButtonPadY)
HiHat_B4.bind('<Button-1>', noteOnOff)

HiHat_B5 = Button(buttonFrame, text="5", bg=styleButtonColor, width=styleButtonWidth)
HiHat_B5.grid(row=2, column=4, padx=styleButtonPadX, pady=styleButtonPadY)
HiHat_B5.bind('<Button-1>', noteOnOff)

HiHat_B6 = Button(buttonFrame, text="6", bg=styleButtonColor, width=styleButtonWidth)
HiHat_B6.grid(row=2, column=5, padx=styleButtonPadX, pady=styleButtonPadY)
HiHat_B6.bind('<Button-1>', noteOnOff)

HiHat_B7 = Button(buttonFrame, text="7", bg=styleButtonColor, width=styleButtonWidth)
HiHat_B7.grid(row=2, column=6, padx=styleButtonPadX, pady=styleButtonPadY)
HiHat_B7.bind('<Button-1>', noteOnOff)

HiHat_B8 = Button(buttonFrame, text="8", bg=styleButtonColor, width=styleButtonWidth)
HiHat_B8.grid(row=2, column=7, padx=styleButtonPadX, pady=styleButtonPadY)
HiHat_B8.bind('<Button-1>', noteOnOff)
"""



startButton = Button(topFrame, text="lets go", bg="#FFFFFF", width=15, command=letsGo)
startButton.grid(row=0, column=0)
#startButton.bind('<Button-1>', letsGo)





# Reaktion auf das Programmende
def win_close () :
    print("tschöööö")
    # Aufräumarbeiten ..
    root.quit()

root.protocol("WM_DELETE_WINDOW",win_close)


# Update der GUI
root.mainloop()

