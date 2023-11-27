from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import datetime
import Fee_Backend


class Fee():
    def __init__(self, master):
        self.master = master
        self.master.title('Fee Information')
        self.master.geometry('1350x750')
        self.master.config(bg='light blue')

        #Declaring Variables
        self.recpt = StringVar()
        self.name = StringVar()
        self.admsn = StringVar()
        self.date = StringVar()
        self.branch = StringVar()
        self.sem = StringVar()
        self.total = DoubleVar()
        self.paid = DoubleVar()
        self.due = DoubleVar()

        #Functions
        def Tuple(event):
            try:
                global st
                index = self.list.curselection()[0]
                st = self.list.get(index)

                self.recpt_entry.delete(0, END)
                self.recpt_entry.insert(END, st[1])
                self.name_entry.delete(0, END)
                self.name_entry.insert(END, st[2])
                self.admsn_entry.delete(0, END)
                self.admsn_entry.insert(END, st[3])
                self.Date_entry.delete(0, END)
                self.Date_entry.insert(END, st[4])
                self.branch_entry.delete(0, END)
                self.branch_entry.insert(END, st[5])
                self.sem_entry.delete(0, END)
                self.sem_entry.insert(END, st[6])
                self.total_entry.delete(0, END)
                self.total_entry.insert(END, st[7])
                self.paid_entry.delete(0, END)
                self.paid_entry.insert(END, st[8])
                self.due_entry.delete(0, END)
                self.due_entry.insert(END, st[9])
            except IndexError:
                pass

        def Insert():
            if (len(self.admsn.get()) != 0):
                try:
                    x1 = float(self.total.get())
                    x2 = float(self.paid.get())
                    x3 = x1 - x2
                    self.due.set(x3)
                except ValueError:
                    tkinter.messagebox.showerror("Input Error", "Total and Paid fields must be numeric")
                    return
                Fee_Backend.insert(self.recpt.get(), self.name.get(), self.admsn.get(), self.date.get(), self.branch.get(), self.sem.get(), self.total.get(), self.paid.get(), self.due.get())
                self.list.delete(0, END)
                self.list.insert(END, (self.recpt.get(), self.name.get(), self.admsn.get(), self.date.get(),self.branch.get(), self.sem.get(), self.total.get(), self.paid.get(), self.due.get()))

        def View():
            self.list.delete(0, END)
            for row in Fee_Backend.view():
                self.list.insert(END, row, str(' '))

        def Reset():
            self.recpt.set(' ')
            self.name.set(' ')
            self.admsn.set(' ')
            self.date.set(datetime.date.today())
            self.branch.set(' ')
            self.sem.set(' ')
            self.total.set(0.0)
            self.paid.set(0.0)
            self.due.set(0.0)
            self.Display.delete('1.0', END)
            self.list.delete(0, END)

        def Delete():
            Fee_Backend.delete(st[0])
            Reset()
            View()

        def Search():
            self.list.delete(0, END)
            for row in Fee_Backend.search(self.recpt.get(), self.name.get(), self.admsn.get(), self.date.get(), self.branch.get(), self.sem.get(), self.total.get(), self.paid.get(), self.due.get()):
                self.list.insert(END, row, str(' '))

        def Update():
            Fee_Backend.delete(st[0])
            Insert()

        def Exit():
            Exit = tkinter.messagebox.askyesno('Attention', 'Confirm, if you want to Exit')
            if Exit > 0:
                root.destroy()
                return

        #Frames
        Main_Frame = LabelFrame(self.master, width = 1300, height = 500, font = ('Sniglet', 20), bg = 'light blue', relief = 'ridge')
        Main_Frame.grid(row = 0, column = 0, padx = 10, pady = 20)

        Title_Frame = LabelFrame(Main_Frame, width=1350, height=100, bg='light blue', relief='flat')
        Title_Frame.grid(row = 0, column = 0, padx = 10, pady = 20)

        self.lblTitle = Label(Title_Frame, font=('Walter Turncoat', 30), text='Fee Information', bg='light blue', padx=13, relief='flat')
        self.lblTitle.grid(padx=100)

        Frame_1 = LabelFrame(Main_Frame, width = 600, height = 400, font = ('Walter Turncoat', 20), relief = 'ridge', bg = 'light blue', text = 'Information')
        Frame_1.grid(row = 1, column = 0, padx = 15, pady = 15)

        Frame_2 = LabelFrame(Main_Frame, width = 750, height = 400, font = ('Walter Turncoat', 20), relief = 'ridge', bg = 'light blue', text = 'Fee Database')
        Frame_2.grid(row = 1, column = 1, padx = 5)

        Button_Frame = Frame(master, width = 1200, height = 100, bg = 'light blue', relief = 'ridge')
        Button_Frame.grid(row = 2, column = 0, pady = 10)

        #Labels using Frames
        self.recpt_label = Label(Frame_1, text='Receipt No. : ', font=('Sniglet', 20), bg='light blue')
        self.recpt_label.grid(row=0, column=0, padx=15, sticky=W)

        self.name_label = Label(Frame_1, text='Student Name : ', font=('Sniglet', 20), bg='light blue')
        self.name_label.grid(row=1, column=0, padx=15, sticky=W)

        self.admsn_label = Label(Frame_1, text='Admission No. : ', font=('Sniglet', 20), bg='light blue')
        self.admsn_label.grid(row=2, column=0, padx=15, sticky=W)

        self.Date_label = Label(Frame_1, text='Date : ', font=('Sniglet', 20), bg='light blue')
        self.Date_label.grid(row=3, column=0, padx=15, sticky=W)

        self.branch_label = Label(Frame_1, text='Branch : ', font=('Sniglet', 20), bg='light blue')
        self.branch_label.grid(row=4, column=0, padx=15, sticky=W)

        self.sem_label = Label(Frame_1, text='Semester : ', font=('Sniglet', 20), bg='light blue')
        self.sem_label.grid(row=5, column=0, padx=15, sticky=W)

        self.total_label = Label(Frame_1, text='TOTAL AMOUNT : ', font=('Sniglet', 20), bg='light blue')
        self.total_label.grid(row=6, column=0, padx=15, sticky=W)

        self.paid_label = Label(Frame_1, text='PAID AMOUNT : ', font=('Sniglet', 20), bg='light blue')
        self.paid_label.grid(row=7, column=0, padx=15, sticky=W)

        self.due_label = Label(Frame_1, text='BALANCE : ', font=('Sniglet', 20), bg='light blue')
        self.due_label.grid(row=8, column=0, padx=15, sticky=W)

        #Entries using Frames
        d1 = datetime.date.today()
        self.date.set(d1)

        self.recpt_entry = Entry(Frame_1, font=('Sniglet', 17), textvariable=self.recpt)
        self.recpt_entry.grid(row=0, column=1, padx=15, pady=5)

        self.name_entry = Entry(Frame_1, font=('Sniglet', 17), textvariable=self.name)
        self.name_entry.grid(row=1, column=1, padx=15, pady=5)

        self.admsn_entry = Entry(Frame_1, font=('Sniglet', 17), textvariable=self.admsn)
        self.admsn_entry.grid(row=2, column=1, padx=15, pady=5)

        self.Date_entry = Entry(Frame_1, font=('Sniglet', 17), textvariable=self.date)
        self.Date_entry.grid(row=3, column=1, padx=15, pady=5)

        self.branch_entry = ttk.Combobox(Frame_1, values=(' ', 'CSE', 'IT', 'ETC/ET&T', 'Mechanical', 'Civil', 'EE', 'EEE'), font=('Sniglet', 17), width=19, textvariable=self.branch)
        self.branch_entry.grid(row=4, column=1, padx=15, pady=5)

        self.sem_entry = ttk.Combobox(Frame_1, values=(' ', 'FIRST', 'SECOND', 'THIRD', 'FOURTH', 'FIFTH', 'SIXTH', 'SEVENTH', 'EIGHTH'), font=('Sniglet', 17), width=19, textvariable=self.sem)
        self.sem_entry.grid(row=5, column=1, padx=15, pady=5)

        self.total_entry = Entry(Frame_1, font=('Sniglet', 17), width=20, textvariable=self.total)
        self.total_entry.grid(row=6, column=1, padx=15, pady=5)

        self.paid_entry = Entry(Frame_1, font=('Sniglet', 17), width=20, textvariable=self.paid)
        self.paid_entry.grid(row=7, column=1, padx=15, pady=5)

        self.due_entry = Entry(Frame_1, font=('Sniglet', 17), width=20, textvariable=self.due, state='readonly')
        self.due_entry.grid(row=8, column=1, padx=15, pady=5)

        #Frame_2
        self.Display = Text(Frame_2, width=42, height=12, font=('Sniglet', 20))
        self.Display.grid(row=0, column=0, padx=3)

        #List and Scroll Bar
        sb = Scrollbar(Frame_2)
        sb.grid(row=0, column=1, sticky='ns')

        self.list = Listbox(Frame_2, font = ('Walter Turncoat', 12), width=75, height=19)
        self.list.bind('<<ListboxSelect>>', Tuple)
        self.list.grid(row=0, column=0)
        sb.config(command=self.list.yview)

        #Buttons
        btnSave = Button(Button_Frame, text = 'Save', font = ('Walter Turncoat',17), width = 8, command=Insert)
        btnSave.grid(row=0, column=0, padx=5, pady=5)

        btnDisplay = Button(Button_Frame, text = 'Display', font = ('Walter Turncoat',17), width = 8, command=View)
        btnDisplay.grid(row=0, column=1, padx=5, pady=5)

        btnReset = Button(Button_Frame, text = 'Reset', font = ('Walter Turncoat',17), width = 8, command=Reset)
        btnReset.grid(row=0, column=2, padx=5, pady=5)

        btnReset = Button(Button_Frame, text = 'Update', font = ('Walter Turncoat',17), width = 8, command=Update)
        btnReset.grid(row=0, column=3, padx=5, pady=5)

        btnDelete = Button(Button_Frame, text = 'Delete', font = ('Walter Turncoat',17), width = 8, command=Delete)
        btnDelete.grid(row=0, column=4, padx=5, pady=5)

        btnSearch = Button(Button_Frame, text = 'Search', font = ('Walter Turncoat',17), width = 8, command=Search)
        btnSearch.grid(row=0, column=5, padx=5, pady=5)

        btnExit = Button(Button_Frame, text = 'Exit', font = ('Walter Turncoat',17), width = 8, command=Exit)
        btnExit.grid(row=0, column=7, padx=5, pady=5)

root = Tk()
obj = Fee(root)
root.mainloop()
