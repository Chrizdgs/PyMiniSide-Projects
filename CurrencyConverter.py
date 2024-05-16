from tkinter import*
from tkinter import ttk
import tkinter.messagebox

class currencyConverter:
    
    def __init__(self, root):
        self.root = root
        self.root.title('Currency Converter') #Title of Window
        self.root.geometry('840x600+300+200') #size of window
        #---------------------------------------------------------------------------------------------------------------
        mainFrame = Frame(self.root, bd=10, relief=RIDGE)
        mainFrame.grid()
        
        Tops = Frame(mainFrame, bd=0, width=860, height=450, relief=RIDGE)
        Tops.pack(side=TOP)
        
        self.lblTitle =Label(Tops, font=('Calibri',58,'bold'), text='Currency Converter', justify=CENTER) #Label Title
        self.lblTitle.grid()
        
        ConverterFrame = LabelFrame(mainFrame, bd=10, width=840, height=200, relief= RIDGE, font=('Calibri',22,'bold'), fg='#5f9ea0', text='Amount to Convert') #Frame of the converter Menu
        ConverterFrame.pack(side=TOP)
        
        DisplayConverter = LabelFrame(mainFrame, bd=0, width=840, height=100, relief= RIDGE, pady=10, font=('Calibri',22,'bold'), fg='#5f9ea0', text='Display Conversion') #Frame of the Display
        DisplayConverter.pack(side=TOP)
        
        ButtonFrame = LabelFrame(mainFrame, bd=10, width=840, height=150, relief= RIDGE, font=('Calibri',22,'bold'), fg='#5f9ea0', text='Confirm') # Frame of the Buttons
        ButtonFrame.pack(side=BOTTOM)
        #----------------------------------------------------Function-----------------------------------------------------------
        
        conversion_rates = {
            'Britain (GBP)': 1.00,
            'United States Dollar': 1.40,
            'Euro (EUR)': 1.17,
            'Japanese Yen (JPY)': 151.92,
            'Swiss Franc (CHF)': 1.29,
            'Canadian Dollar (CAD)': 1.72,
            'Australian Dollar (AUD)': 1.81,
            'Chinese Yuan (CNY)': 9.04,
            'Indian Rupee (INR)': 102.61,
            'Mexican Peso (MXN)': 28.09,
            'Nigerian Naira (NGN)':1647.63
        }
        
        def convert_currency(): #Function to convert currency values
            try:
                amount = float(self.amount_entry.get()) #Get the amount to convert
                from_currency = self.from_currency_cmbBox.get() #Get the currecy from
                to_currency = self.to_currency_cmbBox.get() #Get the currency to
                converted_amount = amount * conversion_rates[to_currency] / conversion_rates[from_currency] #Math Operation to convert the amount
                self.result_label.config(text=f'{amount} {from_currency} = {converted_amount:.2f} {to_currency}') #sow the result
            except ValueError:
                self.result_label.config(text='Please enter a valid number') #Show result if error
                
        def Reset(): #Funtion for resetting the screen
            self.from_currency_cmbBox.current(0) #Reset the From Currency Combobox
            self.to_currency_cmbBox.current(0) #Reset the To Currency Combobox
            self.amount_entry.delete(0, END) #Delete the values in the amount entry
            self.result_label.config(text='') #Clean the result box
            self.amount_entry.focus() #Focus on Amount text box
        
        def iExit(): #Funtion for exiting the application
            iExit = tkinter.messagebox.askyesno('Converter','Confirm if you want to exit') # Ask for confirmation
            if iExit > 0:
                root.destroy()
                return
            
        #----------------------------------------------------Widget-----------------------------------------------------------
        
        self.amount_label = Label(ConverterFrame, font=('Calibri',22,'bold'), text='Amount: ') #Amount Label
        self.amount_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.amount_entry = Entry(ConverterFrame, font=('Calibri',20,'bold'), width=41, justify=CENTER) #Amount Textbox
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        
        self.from_currency_label = Label(ConverterFrame, font=('Calibri',22,'bold'), text='From Currency ') #From Currency Type
        self.from_currency_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.from_currency_cmbBox = ttk.Combobox(ConverterFrame, font=('Calibri',20,'bold'), width=40, values=list(conversion_rates.keys())) #From Currency Type ComboBox
        self.from_currency_cmbBox.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        self.from_currency_cmbBox.current(0) #Display First Value in combobox
        
        self.to_currency_label = Label(ConverterFrame, font=('Calibri',22,'bold'), text='To Currency ') #to Currency Type
        self.to_currency_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        self.to_currency_cmbBox = ttk.Combobox(ConverterFrame, font=('Calibri',20,'bold'), width=40, values=list(conversion_rates.keys())) #to Currency Type ComboBox
        self.to_currency_cmbBox.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        self.to_currency_cmbBox.current(0) #Display First Value in combobox
        
        self.result_label = Label(DisplayConverter, font=('Calibri',20,'bold'), text='') #Amount Label
        self.result_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        
        #----------------------------------------------------Buttons Widget-----------------------------------------------------------
        
        self.amount_entry.focus() #Focus on Amount text box
        
        self.btnConverter = Button(ButtonFrame, font=('Calibri',22,'bold'), width=15, height=2, text='Convert', command=convert_currency).grid(row=0, column=0, padx=4, pady=8) #Buton for Conversion
        
        self.btnReset = Button(ButtonFrame, font=('Calibri',22,'bold'), width=15, height=2, text='Reset', command=Reset).grid(row=0, column=1, padx=4, pady=8) #Buton for Reset
        
        self.btnExit = Button(ButtonFrame, font=('Calibri',22,'bold'), width=15, height=2, text='Exit', command=iExit).grid(row=0, column=2, padx=4, pady=8) #Buton for Exit


if __name__== '__main__':
    root = Tk()
    application = currencyConverter(root)
    root.mainloop()