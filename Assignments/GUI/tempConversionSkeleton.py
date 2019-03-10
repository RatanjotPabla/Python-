#-------------------------------------------------------------------------------
# Name:         Mr. S
# Student #     NOT A STUDENT!
# Date:         30/08/2016
# Filename:     tempConversion.py
# Teacher:      Mr. S
# Purpose:      This program will create a GUI window for the temperature conversion application.
#-------------------------------------------------------------------------------

from tkinter import *

def FahToCel (fah):
    cel = ( fah - 32) / 1.8

    lblOutput = Label(root, text = cel)
    lblOutput.grid(row = 2, column = 0)


#create main or root window here
root = Tk()
root.geometry("500x500")

# Code to add widgets will go here...

#label widget for temperature label
lblTemp = Label(root, text = "Temperature")
lblTemp.grid(row = 0, column = 0)

#Entry widget for temperature (user input of temperature)
entryTemp = Entry(root)
entryTemp.grid(row = 0, column = 1)

#button widget for temperature convertion fahrenheit to celcius
btnConvert = Button(root, text = "Celcius", command = lambda: FahToCel(int(entryTemp.get())))
btnConvert.grid (row = 1, column = 0)

#start main window loop
root.mainloop()

