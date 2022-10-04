import tkinter

class MyGUI:
    def __init__(self):
        self.main_window= tkinter.Tk()


        #geometry is how big the window will be when you run it
        self.main_window.geometry('500x200')

        #title is the title of the window that will show up at the top of the text box
        self.main_window.title('Label Demo')


        self.Label1=tkinter.Label(self.main_window, text='Hello World')
        self.Label2=tkinter.Label(self.main_window, text='This is my GUI program')

        self.Label1.pack()
        self.Label2.pack()


        tkinter.mainloop()

myGUI = MyGUI()

#this will not be on the window because it is not in the loop, once you kill the window, it will show up
print('Hi there!')