from tkinter import *

# Ereignisbehandlung
def buttonCountdownClick():
    stand = int(labelZahl.cget('text'))
    print("jjj")
    if stand > 0:
        # Zähler aktualisieren
        stand = stand - 1
        labelZahl.config(text=str(stand))
        tkFenster.after(1000, buttonCountdownClick)

# Fenster
tkFenster = Tk()
tkFenster.title('Countdown')
tkFenster.geometry('170x125')
# Label
labelZahl = Label(master=tkFenster, text='10', bg='gray', font=('Arial', 36))
labelZahl.place(x=5, y=5, width=160, height=80)
# Button
buttonCountdown = Button(master=tkFenster, text='countdown', bg='#FBD975',
                         command=buttonCountdownClick)
buttonCountdown.place(x=5, y=90, width=160, height=30)
# Aktivierung des Fensters
tkFenster.mainloop()