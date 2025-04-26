#Title: program_2.py
#By: Sabria Fafach
#Date: April 4, 2025

import tkinter
import tkinter.messagebox


class Joes_AutoGUI:
    def __init__(self):
        #Create main window:
        self.main_window=tkinter.Tk()

        #Create three frames:
        self.top_frame=tkinter.Frame(self.main_window)
        self.mid_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)

        #Create seven IntVar objects to use with the C-buttons:
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()
        #Set the IntVar objects to 0:
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)

        #Create the Checkbutton widgets in the top frame:
        self.cb1=tkinter.Checkbutton(self.top_frame,text="Oil Change - $30.00")
        self.cb2=tkinter.Checkbutton(self.top_frame,text="Lube Job - $20.00")
        self.cb3=tkinter.Checkbutton(self.top_frame,text="Radiator Flush - $40.00")
        self.cb4=tkinter.Checkbutton(self.top_frame,text="Transmission Fluid - $100.00")
        self.cb5=tkinter.Checkbutton(self.top_frame,text="Inspection - $35.00")
        self.cb6=tkinter.Checkbutton(self.top_frame,text="Muffler replacement - $200.00")
        self.cb7=tkinter.Checkbutton(self.top_frame,text="Tire Rotation - $20.00")

        #Pack the checkbuttons:
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()

        # Create widgets for the middle frame:
        self.descr_label = tkinter.Label(self.mid_frame, text="Total Charges:")
        self.value = tkinter.StringVar()
        self.Total_label = tkinter.Label(self.mid_frame, textvariable=self.value)

        # Pack middle frame's widgets:
        self.descr_label.pack(side="left")
        self.Total_label.pack(side="left")

        #Create a calculate button a quit button:
        self.calc_button=tkinter.Button(self.bottom_frame,text="Calculate Total",
                                        command=self.calc_total)
        self.quit_button=tkinter.Button(self.bottom_frame,text="Quit",
                                        command=self.main_window.destroy)

        #Pack the buttons:
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")

        #Pack the frames:
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        #Start the mainloop:
        tkinter.mainloop()

        # The calc_total method is the callback for the Calc button:

    def calc_total(self):
        #Create an accumulation variable:
        total=0
        if self.cb_var1.get()==1:
            total+=30
        if self.cb_var2.get()==1:
            total+=20
        if self.cb_var3.get()==1:
            total+=40
        if self.cb_var4.get()==1:
            total+=100
        if self.cb_var5.get()==1:
            total+=35
        if self.cb_var6.get()==1:
            total+=200
        if self.cb_var7.get()==1:
            total+=20

        total_mes=f"${total:,.2f}"
        self.value.set(total_mes)


if __name__ == '__main__':
    auto=Joes_AutoGUI()












