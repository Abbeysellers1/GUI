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
        self.main_window.geometry('600x400')

        #title is the title of the window that will show up at the top of the text box
        self.main_window.title("Shorty's Pizza Price Calculator")

        self.topframe = tkinter.Frame(self.main_window)
        self.crustframe= tkinter.Frame(self.main_window)
        self.toppingframe= tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)


#label and entry for name
        self.name_label=tkinter.Label(self.topframe, text='Customer Name: ', fg='red')

        self.name_entry = tkinter.Entry(self.topframe, width=20)

        self.name_label.pack(side='left')
        self.name_entry.pack(side='left')

        self.topframe.pack()

#radio buttons for type of crust
        self.crustlabel= tkinter.Label(self.crustframe, text='Choose your crust', fg='red')

        self.crustlabel.pack()

        self.crust_var=tkinter.IntVar()

        self.thin=tkinter.Radiobutton(self.crustframe,text='Thin Crust',variable=self.crust_var, value= 10, fg='blue')
        self.regular=tkinter.Radiobutton(self.crustframe,text='Regular Crust',variable=self.crust_var, value= 12, fg='blue')
        self.stuffed=tkinter.Radiobutton(self.crustframe,text='Stuffed Crust',variable=self.crust_var, value= 15, fg='blue')
        
        self.thin.pack()
        self.regular.pack()
        self.stuffed.pack()
      

        self.crustframe.pack()
#check boxes for toppings

        self.toppinglabel= tkinter.Label(self.toppingframe, text='Check which toppings you want',fg='red')

        self.toppinglabel.pack()

        self.cheese_var=tkinter.IntVar()
        self.pepperoni_var=tkinter.IntVar()
        self.sausage_var=tkinter.IntVar()
        self.peppers_var=tkinter.IntVar()
        self.mushrooms_var=tkinter.IntVar()

        self.cheese=tkinter.Checkbutton(self.toppingframe, text="Cheese", variable=self.cheese_var, fg='green')
        self.pepperoni=tkinter.Checkbutton(self.toppingframe, text="Pepperoni", variable=self.pepperoni_var, fg='green')
        self.sausage=tkinter.Checkbutton(self.toppingframe, text="Sausage", variable=self.sausage_var, fg='green')
        self.peppers=tkinter.Checkbutton(self.toppingframe, text="Peppers", variable=self.peppers_var, fg='green')
        self.mushrooms=tkinter.Checkbutton(self.toppingframe, text="Mushrooms", variable=self.mushrooms_var, fg='green')

        self.cheese.pack()
        self.pepperoni.pack()
        self.sausage.pack()
        self.peppers.pack()
        self.mushrooms.pack()

        self.toppingframe.pack()

#calculate and quit buttons
        self.calc_button=tkinter.Button(self.bottomframe, text='Find my total', command= self.convert, fg='purple')

        #destroy will close the window
        self.quitbutton=tkinter.Button(self.bottomframe, text='Quit', command= self.main_window.destroy, fg='purple')

      

        self.calc_button.pack(side='left')
        self.quitbutton.pack(side='right')
        self.bottomframe.pack()


        tkinter.mainloop()


    def convert(self):
        name= self.name_entry.get()
        crusttotal= str(self.crust_var.get())
        total= float(crusttotal)
     
        cheese=0
        pepperoni=1.5
        sausage=2
        mushrooms=1
        peppers=.75
        if self.cheese_var.get()==1:
            total+=cheese
        if self.pepperoni_var.get()==1:
            total+=pepperoni
        if self.sausage_var.get()==1:
            total+=sausage
        if self.peppers_var.get()==1:
            total+=peppers
        if self.mushrooms_var.get()==1:
            total+=mushrooms

        

        #toppingtotal= str()


        #the first is the title of the box, and the second is the message)
        tkinter.messagebox.showinfo('My Pizza Price', "Name of Customer: " + str(name) +'\n' + 'Price of my pizza: ' + str(total))


myGUI = MyGUI()


