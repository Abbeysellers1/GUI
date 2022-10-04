from multiprocessing.sharedctypes import Value
import tkinter

from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.main_window= tkinter.Tk()

        #geometry is how big the window will be when you run it
        self.main_window.geometry('500x200')

        #title is the title of the window that will show up at the top of the text box
        self.main_window.title('Label Demo')

        self.topframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)


        self.radio_var=tkinter.IntVar()

        self.rb1=tkinter.Radiobutton(self.topframe,text='Option1',variable=self.radio_var, value=1)
        self.rb2=tkinter.Radiobutton(self.topframe,text='Option2',variable=self.radio_var, value=2)
        self.rb3=tkinter.Radiobutton(self.topframe,text='Option3',variable=self.radio_var, value=3)

        #If you want it to start by having a button selected, this is how you do it:
        #self.rb2.select()


        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()


        #button on here is you click on it and something will happen, to make something happen, use the command function
        self.OKbutton=tkinter.Button(self.bottomframe, text='OK', command= self.show_choice)

        #will reset it back to option 1
        self.RESETbutton=tkinter.Button(self.bottomframe, text='Reset', command= self.rb1.select)

        #destroy will close the window
        self.quitbutton=tkinter.Button(self.bottomframe, text='Quit', command= self.main_window.destroy)



      

        self.OKbutton.pack(side='left')
        self.RESETbutton.pack(side='left')
        self.quitbutton.pack(side='right')

        self.topframe.pack(side='top')
        self.bottomframe.pack(side='top')



        tkinter.mainloop()


    def show_choice(self):
        #the first is the title of the box, and the second is the message)
        #take out you have selected "option" if you just want it to pull the value
        # the string will display the value in the rbwhatever, not the actual option
        #try putting different values into the value = to test this
        tkinter.messagebox.showinfo('Selection', 'You have selected '+str(self.radio_var.get()))



myGUI = MyGUI()

#this will not be on the window because it is not in the loop, once you kill the window, it will show up
print('Hi there!')