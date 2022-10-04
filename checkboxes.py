import tkinter

import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window= tkinter.Tk()

        #geometry is how big the window will be when you run it
        self.main_window.geometry('500x200')

        #title is the title of the window that will show up at the top of the text box
        self.main_window.title('Label Demo')

        self.topframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)

        self.cb_var1=tkinter.IntVar()
        self.cb_var2=tkinter.IntVar()
        self.cb_var3=tkinter.IntVar()

        self.cb1=tkinter.Checkbutton(self.topframe, text="Option 1", variable=self.cb_var1)
        self.cb2=tkinter.Checkbutton(self.topframe, text="Option 2", variable=self.cb_var2)
        self.cb3=tkinter.Checkbutton(self.topframe, text="Option 3", variable=self.cb_var3)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()


        self.topframe.pack()
        self.bottomframe.pack()

        #button on here is you click on it and something will happen, to make something happen, use the command function
        self.mybutton=tkinter.Button(self.main_window, text='CLick Me!', command= self.do_something)

        #destroy will close the window
        self.quitbutton=tkinter.Button(self.main_window, text='Quit', command= self.main_window.destroy)

      

        self.mybutton.pack(side='left')
        self.quitbutton.pack(side='right')


        tkinter.mainloop()


    def do_something(self):
        self.message = 'You have selected: \n'
        #all of them have to be equal to 1 or 0 because that is all a checkbox can only have a status of 0 or 1
        #if it is a 1 it is checked and 0 not checked
        if self.cb_var1.get()==1:
            self.message += '1\n'
        if self.cb_var2.get()==1:
            self.message += '2\n'
        if self.cb_var3.get()==1:
            self.message += '3\n'

        #the first is the title of the box, and the second is the message)
        tkinter.messagebox.showinfo('Response', self.message)


myGUI = MyGUI()

#this will not be on the window because it is not in the loop, once you kill the window, it will show up
print('Hi there!')