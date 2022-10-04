import tkinter

import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window= tkinter.Tk()

        #geometry is how big the window will be when you run it
        self.main_window.geometry('500x200')

        #title is the title of the window that will show up at the top of the text box
        self.main_window.title('InputBox Demo')

        self.topframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)

        #if you put self.mainframe, it will just show up in the box
        self.prompt_label=tkinter.Label(self.topframe, text='Please enter the distance in kilometers')

        #width in pixels, giving the useer room to input data
        self.kilo_entry = tkinter.Entry(self.topframe, width=10)

        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')


        #you have to pack the message for it to display
      

        self.topframe.pack()
        self.bottomframe.pack()

        #button on here is you click on it and something will happen, to make something happen, use the command function
        self.calc_button=tkinter.Button(self.main_window, text='Convert!', command= self.convert)

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

#this will not be on the window because it is not in the loop, once you kill the window, it will show up
print('Hi there!')