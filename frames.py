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

        #if you put self.mainframe, it will just show up in the box
        self.Label1=tkinter.Label(self.topframe, text='John')
        self.Label2=tkinter.Label(self.topframe, text='Jim')
        self.Label3=tkinter.Label(self.topframe, text='Jerry')

        #you have to pack the message for it to display
        self.Label1.pack(side='left')
        self.Label2.pack(side='left')
        self.Label3.pack(side='right')


        self.Label4=tkinter.Label(self.bottomframe, text='Jill')
        self.Label5=tkinter.Label(self.bottomframe, text='Janie')
        self.Label6=tkinter.Label(self.bottomframe, text='Jen')

        self.Label4.pack(side='left')
        self.Label5.pack(side='left')
        self.Label6.pack(side='right')

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
        #the first is the title of the box, and the second is the message)
        tkinter.messagebox.showinfo('Response', 'Thanks for clicking me!')


myGUI = MyGUI()

#this will not be on the window because it is not in the loop, once you kill the window, it will show up
print('Hi there!')