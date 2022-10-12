import tkinter
import tkinter.messagebox
import tkinter.font as tfont

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

        Comic = tfont.Font(family="Comic Sans",size=14,weight="bold")
        Roman= tfont.Font(family= 'Times New Roman', size=12)
        Arial= tfont.Font(family= 'Arial', size=16)


#label and entry for name
        self.name_label=tkinter.Label(self.topframe, text='Customer Name: ', fg='red', font= Comic)

        self.name_entry = tkinter.Entry(self.topframe, width=20, font= Roman)

        self.name_label.pack(side='left')
        self.name_entry.pack(side='left')

        self.topframe.pack()

#radio buttons for type of crust
        self.crustlabel= tkinter.Label(self.crustframe, text='Choose your crust', fg='red', font= Comic)

        self.crustlabel.pack()

        self.crust_var=tkinter.IntVar()

        self.thin=tkinter.Radiobutton(self.crustframe,text='Thin Crust',variable=self.crust_var, value= 10, fg='blue', font= Roman)
        self.regular=tkinter.Radiobutton(self.crustframe,text='Regular Crust',variable=self.crust_var, value= 12, fg='blue', font= Roman)
        self.stuffed=tkinter.Radiobutton(self.crustframe,text='Stuffed Crust',variable=self.crust_var, value= 15, fg='blue', font= Roman)
        
        self.thin.pack()
        self.regular.pack()
        self.stuffed.pack()
      

        self.crustframe.pack()
#check boxes for toppings

        self.toppinglabel= tkinter.Label(self.toppingframe, text='Check which toppings you want',fg='red', font= Comic)

        self.toppinglabel.pack()

        self.cheese_var=tkinter.IntVar()
        self.pepperoni_var=tkinter.IntVar()
        self.sausage_var=tkinter.IntVar()
        self.peppers_var=tkinter.IntVar()
        self.mushrooms_var=tkinter.IntVar()

        self.cheese=tkinter.Checkbutton(self.toppingframe, text="Cheese", variable=self.cheese_var, fg='green', font= Roman)
        self.pepperoni=tkinter.Checkbutton(self.toppingframe, text="Pepperoni", variable=self.pepperoni_var, fg='green', font= Roman)
        self.sausage=tkinter.Checkbutton(self.toppingframe, text="Sausage", variable=self.sausage_var, fg='green', font= Roman)
        self.peppers=tkinter.Checkbutton(self.toppingframe, text="Peppers", variable=self.peppers_var, fg='green', font= Roman)
        self.mushrooms=tkinter.Checkbutton(self.toppingframe, text="Mushrooms", variable=self.mushrooms_var, fg='green', font= Roman)

        self.cheese.pack()
        self.pepperoni.pack()
        self.sausage.pack()
        self.peppers.pack()
        self.mushrooms.pack()

        self.toppingframe.pack()

#calculate and quit buttons
        self.calc_button=tkinter.Button(self.bottomframe, text='Find my total', command= self.convert, fg='purple', font= Arial)

        #destroy will close the window
        self.quitbutton=tkinter.Button(self.bottomframe, text='Quit', command= self.main_window.destroy, fg='purple', font= Arial)

      

        self.calc_button.pack(side='left')
        self.quitbutton.pack(side='right')
        self.bottomframe.pack()


        tkinter.mainloop()


    def convert(self):
        name= self.name_entry.get()
        self.message = 'You have selected toppings: \n'
        crusttotal= str(self.crust_var.get())
        total= float(crusttotal)
     
        cheese=0
        pepperoni=1.25
        sausage=2
        mushrooms=1
        peppers=.75
        if self.cheese_var.get()==1:
            self.message += 'Cheese\n'
            total+=cheese
        if self.pepperoni_var.get()==1:
            self.message += 'Pepperoni\n'
            total+=pepperoni
        if self.sausage_var.get()==1:
            self.message += 'Sausage\n'
            total+=sausage
        if self.peppers_var.get()==1:
            self.message += 'Peppers\n'
            total+=peppers
        if self.mushrooms_var.get()==1:
            self.message += 'Mushrooms\n'
            total+=mushrooms

        finaltotal=round(total)
        
        


        #the first is the title of the box, and the second is the message)
        tkinter.messagebox.showinfo('My Pizza Price', "Name of Customer: " + str(name) +'\n'+ '\n'+ self.message + '\nPrice of my pizza: $' + str(format(finaltotal,'.2f')))
        
myGUI = MyGUI()


