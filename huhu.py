from tkinter import *
top = Tk()
top.geometry("500x500")

button_names = ["dev/sda", "dev/sdb"]
button_list = [] # for later needs

#my understanding of creating buttons from a list!?
for i in button_names:
    button = Button(top, text=i, command=lambda x=i:lable_name(x))
    button.pack()
    button_list.append(button) 

#Labels are packed bellow because I don't know where you want to pack it    
def lable_name(name):
    label = Label(top, text="HDD {} is added to the zpool".format(name))
    label.pack()

top.mainloop()   