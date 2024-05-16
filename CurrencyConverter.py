from tkinter import*
from tkinter import ttk
import tkinter.messagebox

class currencyConverter:
    
    def __init__(self, root):
        self.root = root
        self.root.title('Currency Converter')
        self.root.geometry('902x568+300+200')
        
        mainFrame = Frame(self.root, bd=10, relief=RIDGE)
        mainFrame.grid()
        
        Tops = Frame(mainFrame, bd=0, width=860, height=450, relief=RIDGE)
        Tops.pack(side=TOP)
        
        self.lblTitle =Label(Tops, font=('Calibri',61,'bold'), text='Currency Converter', justify=CENTER)
        self.lblTitle.grid()
        
        ConverterFrame = LabelFrame(mainFrame, bd=10, width=840, height=200, relief= RIDGE, font=('Calibri',22,'bold'), fg='#5f9ea0', text='Amount to Convert')
        ConverterFrame.pack(side=TOP)
        
        DisplayConverter = LabelFrame(mainFrame, bd=0, width=840, height=100, relief= RIDGE, pady=10, font=('Calibri',22,'bold'), fg='#5f9ea0', text='Display Conversion')
        DisplayConverter.pack(side=TOP)



if __name__== '__main__':
    root = Tk()
    application = currencyConverter(root)
    root.mainloop()