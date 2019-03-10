#Name:        Neal Bhullar
#Student:     33601190
#FileName:    tempConversions.py
#Date:        January 8,2019
#Teacher:     Mr.Sarros
#Purpose:     Creates a window to convert tempertures between celsius and fahrenheit.
#==================================================================================================================================================================
from tkinter import *
#Importing tkinter

window = Tk()
#Creates a main window window.
window.title("Temperature Conversion")
#Names the window, Temperature Conversion

class Tempertaure(object):
    #Creates class called temperature.
    def __init__(self, temp):
        self._temp = temp
        #Initializes object to have a value for its temperature.

    def tempCon(self,w):
        #Converts the temperature to celcius/fahrenheit depending on the button value.
        #Then, returns the new temperature.
        if w == 1:
            temp1 = float(self._temp)*1.8 + 32
            return temp1
        elif w==2:
            temp1 = (float(self._temp) - 32)*5/9
            return temp1


def printMethod():
    #Creates a function that converts the temperature to celcius/fahrenheit, then outputs it to the text box.
    textFile.delete(1.0, END)
    #Deletes whatever is in the textbox (allows you to do more than one conversion and takes away the previous conversion result.
    w = v.get()
    #Determine which radio button is clicked.
    temp1 = variable.get()
    t1 = Tempertaure(temp1)
    #Creates object
    textFile.insert(INSERT, t1.tempCon(w))
    if temp1>0:
        window.config(background = 'red')
    else:
        window.config(background = 'blue')
        
    #Prints and converts tmepertaure


v = IntVar()
#variable is 1 or 2 depending on which radio button is clicked.
Radiobutton(window, text="Celsius to Fahrenheit", variable = v, value = 1).grid(row = 1, column = 1 )
Radiobutton(window, text="Fahrenheit to Celsius", variable = v, value = 2).grid(row = 2, column = 1)
#Creates the radio buttons

label = Label(window, text="Enter temperature:").grid(row = 3, column = 1)
#Creates a label for the input box.
variable = IntVar()
#variable is the integer put into the textbox.
entry = Entry(window, textvariable = variable)
entry.grid(row = 4, column = 1)
#Entry textbox.


buttonEnter = Button(window, text = "Convert", command = lambda: printMethod()).grid(row=5, column=1)
#Creates a button called, Convert, that when clicked executes the tempCon method.

label2 = Label(window, text="Converted Temperature:").grid(row = 7, column = 1)
#Creates a label for the output box.
textFile = Text(window, height = 1, width = 15 )
textFile.grid(row = 8, column = 1)
#Creates a text file for read printMethod function.

Button(window, text="Exit", command=lambda: window.destroy()).grid(row = 9, column = 1)
#Creates an exist button on window.

window.mainloop()

