from math import sqrt
from huhu import Hello
import time
import pygame 

pygame.init()
hiClick = pygame.mixer.Sound('hiclick.wav')
loClick = pygame.mixer.Sound('loclick.wav')

kick = pygame.mixer.Sound('kick.wav')
snare = pygame.mixer.Sound('snare.wav')
hihat = pygame.mixer.Sound('hihatlong.wav')
hihat.set_volume(0.4)


counter = 1

bpm = 120
tempo = 1/(bpm/60*1)
print(tempo)

timeNow = 0
timeOld = 0



while True:

    timeNow = time.perf_counter()
    if timeNow-timeOld > tempo:
        print(timeNow-timeOld)
        if counter == 1:
            #hiClick.play()
            kick.play()
            hihat.play()

        elif counter == 3:
            snare.play()
            hihat.play()
        else:
            hihat.play()
        counter = counter+1
        if counter > 4:
            counter = 1
        timeOld = timeNow


