#Name:          Ratanjot Pabla
#Student:       32700826
#FileName:      tempConvGUI.py
#Date:          January 11, 2019
#Teacher:       Mr.Sarros
#Purpose:       This program will take the user input of a temperature in either celsius or fahreheit and output it into the other within a graphical user interface.


from tkinter import*    #Importing tkinter module
    

class Temperature(object):  #Creates a class called temperature 
    def __init__(self,temp):
        self.temp = temp    #Initializes object with the "__init__" method to store the value for the temperature.

    def tempCon(self,w):    #It will then follow by converting the users temperature value in one unit to the other depending on what radiobutton value has been selected.
        if w == 1:           
            temp1 = float(self.temp)*1.8+32 #fahrenheit formula (from celsius to fahrenheit)  
            return temp1
        elif w==2:
            temp1 = float((self.temp)-32)/1.8 #celsius formula (from fahrenheit to celsius) 
            return temp1


def Text_File():    #This is the function that will output the user's converted temperature in the text box
    textFile.delete(1.0, END)
    w = x.get() #Determines which radiobutton has been clicked on 
    temp1 = y.get() #Determines what value is stored inside of the entry box
    t1 = Temperature(temp1) #The variable temp1 is being called into the class object.
    textFile.insert(INSERT,t1.tempCon(w))   #Inserts the converted temperature into the text box
    if w==1 and temp1>0:
        root.config(background = 'red') #if we are trying to convert from celsius to fahrenheit and the temperature inputted is  
                                        #greater than 0 degrees celsius, the background will be red.

    elif w==2 and temp1>32:             #if we are trying to convert from fahrenheit to celsius and the temperature inputted is greater than 32 (0 degrees in celsius),
        root.config(background = 'red') #the background will be red.

    else:                               #if the two if statements above are false, then the screen will be blue. 
        root.config(background = 'blue')
    
   
        
root = Tk() #Creates the main window 
root.title("Temperature Conversion")    #Sets the main window's title 



x = IntVar()    #value 1 and 2 is what differs between the two different radio buttons clicked. 
radio1 = Radiobutton(root, text="Celsius to Fahrenheit",variable = x, value=1).grid(row=1,column = 1)     
radio2 = Radiobutton(root, text="Fahrenheit to Celsius",variable = x, value=2).grid(row=1,column = 2)



Label_Entry = Label(root, text = "Enter Temperature").grid(row = 0, column = 0) #Creates a label box for the entry box 

y = IntVar()    #Variable "y" is assigned to the text that is being stored in the entry box 
entry_Temp = Entry(root,textvariable = y).grid(row = 0, column = 1) 


#button widget for temperature convertion
btnConvert = Button(root, text = "Convert Now", command = lambda: Text_File()).grid (row = 1, column = 0)

Label_conversion = Label(root, text="Converted Temperature:").grid(row = 7, column = 1)
#Creates a label for the text file box.
textFile = Text(root, height = 1, width = 15 )
textFile.grid(row = 8, column = 1)
#Creates a text file for read printMethod function and deletes the text inside of the text file box each time a new integer has been inputted into the entry box.

Button(root, text="Exit", command=lambda: root.destroy()).grid(row = 9, column = 1)
#Creates an exit button on root

root.mainloop() #To finish off the root GUI, you must use the mainloop function. 
