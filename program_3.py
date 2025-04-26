#Title: program_3.py
#By: Sabria Fafach
#Date: April 4, 2025


import tkinter
import tkinter.messagebox

class LD_CallsGUI:
    def __init__(self):
        #Create the main window:
        self.main_window=tkinter.Tk()

        #Create three frames:
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #Create an IntVar object to use with the radio buttons:
        self.radio_var=tkinter.IntVar()
        #Set the intVar object to 1:
        self.radio_var.set(1)

        #Create the Radiobutton widgets in the top frame:
        self.rb1=tkinter.Radiobutton(self.top_frame,text="Daytime (6:00 A.M. - 5:59 P.M.)",
                                     variable=self.radio_var,value=1)
        self.rb2=tkinter.Radiobutton(self.top_frame,text="Evening (6:00 P.M. - 11:59 P.M.)",
                                     variable=self.radio_var,value=2)
        self.rb3=tkinter.Radiobutton(self.top_frame,text="Off-Peak (Midnight - 5:59 A.M.)",
                                     variable=self.radio_var,value=3)

        #Pack the radiobuttons:
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Create widgets for middle frame:
        self.prompt_label = tkinter.Label(self.mid_frame
                                            , text="Enter the length of your call in "
                                                   "minutes:")
        self.time_entry = tkinter.Entry(self.mid_frame, width=10)
        # Pack the widgets in the middle frame:
        self.prompt_label.pack(side="left")
        self.time_entry.pack(side="left")

        #Create the buttons in the bottom frame:
        self.calc_button=tkinter.Button(self.bottom_frame,text="Calculate Cost",
                                        command=self.calc_cost)
        self.quit_button=tkinter.Button(self.bottom_frame,text="Quit",
                                        command=self.main_window.destroy)
        #Pack the buttons:
        self.calc_button.pack()
        self.quit_button.pack()

        #Pack the frames:
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        #Enter the tkinter main loop:
        tkinter.mainloop()

        #The calc_cost method is a call back for the calc button:
    def calc_cost(self):
        #Get the value entered by the user:
        mins=float(self.time_entry.get())
        cost_message=()

        if self.radio_var.get()==1:
             cost_message=(f"Your call costs {mins*2:,.2f} cents.")

        if self.radio_var.get()==2:
           cost_message=(f"Your call costs {mins*12:,.2f} cents.")

        if self.radio_var.get()==3:
            cost_message=(f"Your call costs {mins*5:,.2f} cents.")

    # Display the message in an info dialogue box:
        tkinter.messagebox.showinfo("Call Cost",cost_message)

if __name__ == '__main__':
    Call=LD_CallsGUI()







