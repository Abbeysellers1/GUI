
import tkinter
import tkinter.messagebox
import statistics


class MyGUI:
    def __init__(self):
        self.main_window= tkinter.Tk()

        #geometry is how big the window will be when you run it
        self.main_window.geometry('500x200')

        #title is the title of the window that will show up at the top of the text box
        self.main_window.title('Test Scores')


        #self.avg_var=tkinter.StringVar()
        


        self.test1frame = tkinter.Frame(self.main_window)
        self.test2frame = tkinter.Frame(self.main_window)
        self.test3frame = tkinter.Frame(self.main_window)
        self.averagelabel=tkinter.Frame(self.main_window)
        self.bottomframe=tkinter.Frame(self.main_window)
        
        self.prompt_test1=tkinter.Label(self.test1frame, text='Enter the score for test 1:')
        self.prompt_test2=tkinter.Label(self.test2frame, text='Enter the score for test 2:')
        self.prompt_test3=tkinter.Label(self.test3frame,text='Enter the score for test 3:')

        #width in pixels, giving the useer room to input data
        self.test1_entry = tkinter.Entry(self.test1frame, width=3)
        self.test2_entry=tkinter.Entry(self.test2frame, width=3)
        self.test3_entry=tkinter.Entry(self.test3frame, width=3)

        self.prompt_test1.pack(side='left')
        self.test1_entry.pack(side='left')

        self.prompt_test2.pack(side='left')
        self.test2_entry.pack(side='left')

        self.prompt_test3.pack(side='left')
        self.test3_entry.pack(side='left')

        self.test1frame.pack()
        self.test2frame.pack()
        self.test3frame.pack()

 

        self.avg_label= tkinter.Label(self.averagelabel, text= 'Average')

        self.avg_label.pack(side='left')

        self.calculation= tkinter.StringVar()
        self.averageanswer=tkinter.Label(self.averagelabel, textvariable=self.calculation)
        self.averageanswer.pack(side='left')


        
        self.calc_button=tkinter.Button(self.bottomframe, text='Average', command= self.calculate)

        #destroy will close the window
        self.quitbutton=tkinter.Button(self.bottomframe, text='Quit', command= self.main_window.destroy)

      
        self.calc_button.pack(side='left')
        self.quitbutton.pack(side='right')

        self.averagelabel.pack()
        self.bottomframe.pack()


        tkinter.mainloop()


    def calculate(self):
        total= float(self.test1_entry.get())+float(self.test2_entry.get())+float(self.test3_entry.get())
        average=total/3
        self.calculation.set(average)

myGUI = MyGUI()

#this will not be on the window because it is not in the loop, once you kill the window, it will show up





