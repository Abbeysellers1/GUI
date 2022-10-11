import tkinter
import tkinter.messagebox

'''Design a creative UI using Python's tkinter module to calculate the total cost of a pizza. 
The UI should have (at least) each widget that was covered in class:

Frames
Labels (crust type, toppings)

input box (name) ------------------------------------------topframe

buttons (calculate, quick)---------------------------------bottomframe

radio buttons(thin, regular, stuffed crust, deep dish)-----crustframe

check boxes (cheese, pepperoni, sausage, peppers, mushrooms, )---topping frame
message box (total cost, name )--------------------------------- message box

You can use check boxes for for selecting toppings (each with a different cost), 
radio buttons for the type of crust selected (each with a different cost), buttons for calculation and quit. 
The input box can be used to record the name of the person placing the order. 
Use a message box to display the total cost of the pizza along with the name of the person placing the order.

Make sure your design is well laid out and intuitive to the user. 
Take account of spacing and packing so that everything is properly aligned and professional looking. 
Be creative with font, color, size, etc.'''

class MyGUI:
    def __init__(self):
        self.main_window= tkinter.Tk()

        #geometry is how big the window will be when you run it
        self.main_window.geometry('750x200')

        #title is the title of the window that will show up at the top of the text box
        self.main_window.title("Shorty's Pizza Price Calculator")

        self.topframe = tkinter.Frame(self.main_window)
        self.crustframe= tkinter.Frame(self.main_window)
        self.toppingframe= tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)


#label and entry for name
        self.name_label=tkinter.Label(self.topframe, text='Customer Name: ')

        self.name_entry = tkinter.Entry(self.topframe, width=20)

        self.name_label.pack(side='left')
        self.name_entry.pack(side='left')

        self.topframe.pack()

#radio buttons for type of crust
        self.crustlabel= tkinter.Label(self.crustframe, text='Choose your crust')

        self.crustlabel.pack()

        self.crust_var=tkinter.IntVar()

        self.thin=tkinter.Radiobutton(self.crustframe,text='Thin Crust',variable=self.crust_var, value= 10)
        self.regular=tkinter.Radiobutton(self.crustframe,text='Regular Crust',variable=self.crust_var, value= 12)
        self.stuffed=tkinter.Radiobutton(self.crustframe,text='Stuffed Crust',variable=self.crust_var, value= 15)
        
        self.thin.pack()
        self.regular.pack()
        self.stuffed.pack()
      

        self.crustframe.pack()
#check boxes for toppings

        self.toppinglabel= tkinter.Label(self.toppingframe, text='Check which toppings you want')

        self.toppinglabel.pack()

        self.cheese_var=tkinter.IntVar()
        self.pepperoni_var=tkinter.IntVar()
        self.sausage_var=tkinter.IntVar()
        self.peppers_var=tkinter.IntVar()
        self.mushrooms_var=tkinter.IntVar()

        self.cheese=tkinter.Checkbutton(self.toppingframe, text="Cheese", variable=self.cheese_var)
        self.pepperoni=tkinter.Checkbutton(self.toppingframe, text="Pepperoni", variable=self.pepperoni_var)
        self.sausage=tkinter.Checkbutton(self.toppingframe, text="Sausage", variable=self.sausage_var)
        self.peppers=tkinter.Checkbutton(self.toppingframe, text="Peppers", variable=self.peppers_var)
        self.mushrooms=tkinter.Checkbutton(self.toppingframe, text="Mushrooms", variable=self.mushrooms_var)

        self.cheese.pack()
        self.pepperoni.pack()
        self.sausage.pack()
        self.peppers.pack()
        self.mushrooms.pack()

        self.toppingframe.pack()

#calculate and quit buttons
        self.calc_button=tkinter.Button(self.main_window, text='Find my total', command= self.convert)

        #destroy will close the window
        self.quitbutton=tkinter.Button(self.main_window, text='Quit', command= self.main_window.destroy)

      

        self.calc_button.pack(side='left')
        self.quitbutton.pack(side='right')


        tkinter.mainloop()


    def convert(self):
        kilo=float(self.kilo_entry.get())

        miles=round(kilo * 0.6214, 2)

        #the first is the title of the box, and the second is the message)
        tkinter.messagebox.showinfo('Results', str(kilo)+' kilometers is equal to '+ str(miles)+ ' miles')


myGUI = MyGUI()


