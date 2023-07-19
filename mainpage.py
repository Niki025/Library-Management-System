from tkinter import *

roota = Tk()
roota.title("LIBRARY MANAGEMENT")  # Title of the application
roota.geometry('500x500+400+100')  # Size of the screen
Label(text='LIBRARY MANAGEMENT', fg='red', font=44).pack()  # text size and color of the topic

Chooser = Menu()  # chooser is used for menubar
itemone = Menu()  # itemone is display for the topics which comes under the my-profile
itemone.add_command(label='Student Details')  # topic one under my-profile


itemtwo= Menu()  # itemthree is display for the topics which comes under the hostels
itemtwo.add_command(label='Staff Records')
itemtwo.add_command(label='Student Records')

itemthree = Menu()  # itemfour is display for the topics which comes under the warden
itemthree.add_command(label='Book List')


itemfour = Menu()  # itemfive is display for the topics which comes under the payment list
itemfour.add_command(label='Initiate Fine')

itemfive = Menu()
itemfive.add_command(label='Visitor')

itemsix = Menu()
itemsix.add_command(label='Rules and Regulation')

# Used to view in screen all the labels in menubar
Chooser.add_cascade(label='My Profile', menu=itemone)
Chooser.add_cascade(label='Users', menu=itemtwo)
Chooser.add_cascade(label='Book List', menu=itemthree)
Chooser.add_cascade(label='Fine List', menu=itemfour)
Chooser.add_cascade(label='Visitor', menu=itemfive)
Chooser.add_cascade(label='Rules', menu=itemsix)
roota.config(menu=Chooser)
roota.mainloop()