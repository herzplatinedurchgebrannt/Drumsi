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

pattern =  [[0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]]

zaehler = 0

bpm = 120

#sequencerVariables
isPlaying = True

jo = True

def calculateTiming(bpmIn):
    tempoIn = 1000/(bpmIn/60*1)
    tempoIn = int(tempoIn)
    return tempoIn

tempo = calculateTiming(bpm)
print(tempo)


root = Tk()
root.wm_title("Drumsi")
root.config(background = "#000000")

topFrame = Frame(root, width=350, height=50)
topFrame.grid(row=0, column=0, padx=3, pady=3)

buttonFrame = Frame(root, width=600, height=50)
buttonFrame.grid(row=1, column=0, padx=3, pady=3)

def callback1():
    print(B1.get())

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

def say_hello(event):
    step = int(event.widget['text'])-1
    print(event.widget['text'])

    if pattern[0][step]==0:
        pattern[0][step] = 1
        event.widget['bg'] = "#990000"
    else:
        pattern[0][step] = 0
        event.widget['bg'] = "#660033"
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
        root.after(tempo, letsGo)
        zaehler = zaehler+1
        if zaehler >= 8:
            zaehler = 0
        print(zaehler)
    else:
        print(jo)



B1 = Button(buttonFrame, text="1", bg=styleButtonColor, width=styleButtonWidth)
B1.grid(row=0, column=0, padx=styleButtonPadX, pady=styleButtonPadY)
B1.bind('<Button-1>', say_hello)

B2 = Button(buttonFrame, text="2", bg=styleButtonColor, width=styleButtonWidth)
B2.grid(row=0, column=1, padx=styleButtonPadX, pady=styleButtonPadY)
B2.bind('<Button-1>', say_hello)

B3 = Button(buttonFrame, text="3", bg=styleButtonColor, width=styleButtonWidth)
B3.grid(row=0, column=2, padx=styleButtonPadX, pady=styleButtonPadY)
B3.bind('<Button-1>', say_hello)

B4 = Button(buttonFrame, text="4", bg=styleButtonColor, width=styleButtonWidth)
B4.grid(row=0, column=3, padx=styleButtonPadX, pady=styleButtonPadY)
B4.bind('<Button-1>', say_hello)

B5 = Button(buttonFrame, text="5", bg=styleButtonColor, width=styleButtonWidth)
B5.grid(row=0, column=4, padx=styleButtonPadX, pady=styleButtonPadY)
B5.bind('<Button-1>', say_hello)

B6 = Button(buttonFrame, text="6", bg=styleButtonColor, width=styleButtonWidth)
B6.grid(row=0, column=5, padx=styleButtonPadX, pady=styleButtonPadY)
B6.bind('<Button-1>', say_hello)

B7 = Button(buttonFrame, text="7", bg=styleButtonColor, width=styleButtonWidth)
B7.grid(row=0, column=6, padx=styleButtonPadX, pady=styleButtonPadY)
B7.bind('<Button-1>', say_hello)

B8 = Button(buttonFrame, text="8", bg=styleButtonColor, width=styleButtonWidth)
B8.grid(row=0, column=7, padx=styleButtonPadX, pady=styleButtonPadY)
B8.bind('<Button-1>', say_hello)



startButton = Button(topFrame, text="lets go", bg="#FFFFFF", width=15, command=letsGo)
startButton.grid(row=0, column=0)
#startButton.bind('<Button-1>', letsGo)

print(B1.cget('text'))



# Reaktion auf das Programmende
def win_close () :
    print("tschöööö")
    # Aufräumarbeiten ..
    root.quit()

root.protocol("WM_DELETE_WINDOW",win_close)


# Update der GUI
root.mainloop()

