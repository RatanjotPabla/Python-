from tkinter import*

class Temperature(object):
    def __init__(self,temp):
        self.temp = temp

    def tempCon(self,w):
        if w == 1:
            temp1 = float(self.temp)*1.8+32
            return temp1
        elif w==2:
            temp1 = float((self.temp)-32)/1.8
            return temp1


def Text_File():
    textFile.delete(1.0, END)
    w = x.get()
    temp1 = y.get()
    t1 = Temperature(temp1)
    textFile.insert(INSERT,)
    if w==1 and temp1>0:
        root.config(background = 'red')
        textFile.insert(INSERT,"%y fahrenheit is equal to",t1.tempCon(w),"celsius")
    else:
        root.config(background = 'blue')
        
    
    
    

   
        
root = Tk()
root.geometry("500x200")



x = IntVar()
radio1 = Radiobutton(root, text="Celsius to Fahrenheit",variable = x, value=1).grid(row=1,column = 1)     
radio2 = Radiobutton(root, text="Fahrenheit to Celsius",variable = x, value=2).grid(row=1,column = 2)



lblTemp = Label(root, text = "Enter Temperature").grid(row = 0, column = 0)
y = IntVar()


entry_Temp = Entry(root,textvariable = y).grid(row = 0, column = 1)


#button widget for temperature convertion fahrenheit to celcius
btnConvert = Button(root, text = "Convert Now", command = lambda: Text_File()).grid (row = 1, column = 0)

label2 = Label(root, text="Converted Temperature:").grid(row = 7, column = 1)
#Creates a label for the output box.
textFile = Text(root, height = 1, width = 15 )
textFile.grid(row = 8, column = 1)
#Creates a text file for read printMethod function.

Button(root, text="Exit", command=lambda: root.destroy()).grid(row = 9, column = 1)
#Creates an exist button on window.

root.mainloop()
