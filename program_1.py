#Title: program_1.py
#By: Sabria Fafach
#Date: April 4, 2025



import tkinter

class CalculatorGUI:
    def __init__(self):
        #Create main window:
        self.main_window=tkinter.Tk()

        #Create three frames:
        self.top_frame=tkinter.Frame(self.main_window)
        self.middle_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)

        #Create widgets for top frame:
        self.prompt_label_1=tkinter.Label(self.top_frame
                                          ,text="How many gallons of gas "
                                                "does your car hold?")
        self.gal_entry=tkinter.Entry(self.top_frame,width=10)

        self.prompt_label_2=tkinter.Label(self.top_frame, text="How many miles "
                                                               "does your car get from"
                                                               " a full gas tank?")
        self.mil_entry=tkinter.Entry(self.top_frame,width=10)

        #Pack the widgets in the top frame:
        self.prompt_label_1.pack(side="left")
        self.gal_entry.pack(side="left")
        self.prompt_label_2.pack(side="left")
        self.mil_entry.pack(side="left")


        #Create widgets for the middle frame:
        self.descr_label=tkinter.Label(self.middle_frame,text="Miles per Gallon (MPG):")
        self.value=tkinter.StringVar()
        self.MPG_label=tkinter.Label(self.middle_frame,textvariable=self.value)

        #Pack middle frame's widgets:
        self.descr_label.pack(side="left")
        self.MPG_label.pack(side="left")


        #Create the button widgets for the bottom frame:
        self.calc_button=tkinter.Button(self.bottom_frame,text="Calculate MPG",
                                        command=self.Calculate)
        self.quit_button=tkinter.Button(self.bottom_frame,text="Quit",
                                        command=self.main_window.destroy)
        #Pack the buttons:
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")


        #Pack the frames:
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        #Enter the tkinter main loop:
        tkinter.mainloop()



    def Calculate(self):
    #Get the values entered by the user:
        gal=float(self.gal_entry.get())
        mil=float(self.mil_entry.get())

    #Calculate miles per gallon:
        MPG=mil/gal

        self.value.set(MPG)

if __name__ == '__main__':
    MPG_calc=CalculatorGUI()



























