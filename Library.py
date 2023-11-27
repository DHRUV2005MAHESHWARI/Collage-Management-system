from tkinter import*
from tkinter import ttk
from datetime import date, timedelta, datetime
import tkinter.messagebox
import Library_Backend

class Library:
       
       def __init__(self, root):
              self.root = root
              self.root.title('Library Management System')
              self.root.geometry('1350x750')
              self.root.config(bg = 'light blue')

              #Frames
              Main_Frame = Frame(self.root, bg = 'light blue')
              Main_Frame.grid()

              Title_Frame_1 = Frame(Main_Frame, width = 1350, bg = 'light blue', relief = RIDGE, padx = 20)
              Title_Frame_1.pack(side = TOP)

              self.lblTitle = Label(Title_Frame_1, font = ('Walter Turncoat', 30), text = 'Library Management System', bg = 'light blue', padx = 13)
              self.lblTitle.grid()

              Button_Frame = Frame(Main_Frame, width = 1350, height = 50, relief = RIDGE, bg = 'light blue')
              Button_Frame.pack(side = BOTTOM)

              Detail_Frame = Frame(Main_Frame, width = 1350, height = 100, relief = RIDGE, bg = 'light blue')
              Detail_Frame.pack(side = BOTTOM)

              Data_Frame = Frame(Main_Frame, width = 1350, height = 400, relief = RIDGE, bg = 'light blue')
              Data_Frame.pack(side = BOTTOM)

              Frame_1 = LabelFrame(Data_Frame, width = 800, height = 400, relief = RIDGE, bg = 'light blue', text = "Library Membership Info:", padx = 5, font = ('Walter Turncoat', 20))
              Frame_1.pack(side = LEFT, padx = 3)

              #Variables
              self.ID = StringVar()
              self.title = StringVar()
              self.author = StringVar()
              self.edsn = StringVar()
              self.yop = StringVar()
              self.borrow = StringVar()
              self.due = StringVar()
              self.issued_days = StringVar()
              self.overdue_status = StringVar()
              self.selected_x = None
              self.List_of_Books = Library_Backend.get_all_books()
              self.initialize_dates()
              self.tree = ttk.Treeview(Detail_Frame)
              self.tree['columns'] = ("x", "ID", "Title", "Author", "Edition", "Year of Publication", "Date Borrowed", "Date Due", "Issued Days", "Overdue Status")
       
              for col in self.tree['columns']:
                     self.tree.heading(col, text=col)
                     self.tree.column(col, width=100)

              self.tree.grid(row=0, column=0, sticky='nsew')
              self.Display()


              #Labels
              self.Label_1 = Label(Frame_1, text = 'Book ID', font = ('Sniglet', 20), pady = 2, bg = 'light blue' )
              self.Label_1.grid(row = 0, column = 0, sticky = W)
              self.Label_2 = Label(Frame_1, text = 'Book Title', font = ('Sniglet', 20), pady = 2, bg = 'light blue' )
              self.Label_2.grid(row = 1, column = 0, sticky = W)
              self.Label_3 = Label(Frame_1, text = 'Author', font = ('Sniglet', 20), pady = 2, bg = 'light blue' )
              self.Label_3.grid(row = 2, column = 0, sticky = W)
              self.Label_4 = Label(Frame_1, text = 'Edition', font = ('Sniglet', 20), pady = 2, bg = 'light blue' )
              self.Label_4.grid(row = 3, column = 0, sticky = W)
              self.Label_5 = Label(Frame_1, text = 'Year of Publication', font = ('Sniglet', 20), pady = 2, bg = 'light blue' )
              self.Label_5.grid(row = 4, column = 0, sticky = W)
              self.Label_6 = Label(Frame_1, text = 'Date Borrowed', font = ('Sniglet', 20), pady = 2, bg = 'light blue' )
              self.Label_6.grid(row = 5, column = 0, sticky = W)
              self.Label_7 = Label(Frame_1, text = 'Date Due', font = ('Sniglet', 20), pady = 2, bg = 'light blue' )
              self.Label_7.grid(row = 6, column = 0, sticky = W)
              self.Label_8 = Label(Frame_1, text = 'Book issued for', font = ('Sniglet', 20), pady = 2, bg = 'light blue' )
              self.Label_8.grid(row = 7, column = 0, sticky = W)
              self.Label_9 = Label(Frame_1, text = 'Overdue Status', font = ('Sniglet', 20), pady = 2, bg = 'light blue' )
              self.Label_9.grid(row = 8, column = 0, sticky = W)

              #Entries
              self.Entry_0 = Entry(Frame_1, font = ('Sniglet', 20), width = 25, textvariable = self.ID)
              self.Entry_0.grid(row = 0, column = 4, padx = 15)
              self.Entry_1 = Entry(Frame_1, font = ('Sniglet', 20), width = 25, textvariable = self.title)
              self.Entry_1.grid(row = 1, column = 4, padx = 15)
              self.Entry_2 = Entry(Frame_1, font = ('Sniglet', 20), width = 25, textvariable = self.author)
              self.Entry_2.grid(row = 2, column = 4, padx = 15)
              self.Entry_3 = Entry(Frame_1, font = ('Sniglet', 20), width = 25, textvariable = self.edsn)
              self.Entry_3.grid(row = 3, column = 4, padx = 15)
              self.Entry_4 = Entry(Frame_1, font = ('Sniglet', 20), width = 25, textvariable = self.yop)
              self.Entry_4.grid(row = 4, column = 4, padx = 15)
              self.Entry_5 = Entry(Frame_1, font = ('Sniglet', 20), width = 25, textvariable = self.borrow)
              self.Entry_5.grid(row = 5, column = 4, padx = 15)
              self.Entry_6 = Entry(Frame_1, font = ('Sniglet', 20), width = 25, textvariable = self.due, state='readonly')
              self.Entry_6.grid(row = 6, column = 4, padx = 15)            
              self.Entry_7 = Entry(Frame_1, font = ('Sniglet', 20), width = 25, textvariable = self.issued_days, state='readonly')
              self.Entry_7.grid(row = 7, column = 4, padx = 15)      
              self.Entry_8 = Entry(Frame_1, font = ('Sniglet', 20), width = 25, textvariable = self.overdue_status, state='readonly')
              self.Entry_8.grid(row = 8, column = 4, padx = 15)      
                            
              #Listbox and Scrollbar               
              tree_scroll = ttk.Scrollbar(Detail_Frame, orient="vertical", command=self.tree.yview)
              tree_scroll.grid(row=0, column=1, sticky='ns')
              self.tree.configure(yscrollcommand=tree_scroll.set)
              self.tree.bind('<<TreeviewSelect>>', self.on_tree_select)

              #Buttons
              Button_1 = Button(Button_Frame, text = 'Save', font = ('Walter Turncoat',17), width = 10, command = lambda:[self.update_issue_info(), self.Insert()])
              Button_1.grid(row = 0, column = 0, padx = 8, pady = 5)
              Button_2 = Button(Button_Frame, text = 'Display', font = ('Walter Turncoat',17), width = 10, command = self.Display)
              Button_2.grid(row = 0, column = 1, padx = 8)
              Button_3 = Button(Button_Frame, text = 'Reset', font = ('Walter Turncoat',17), width = 10, command = self.Reset)
              Button_3.grid(row = 0, column = 2, padx = 8)
              Button_4 = Button(Button_Frame, text = 'Update', font = ('Walter Turncoat',17), width = 10, command = self.Update)
              Button_4.grid(row = 0, column = 3, padx = 8)
              Button_5 = Button(Button_Frame, text = 'Search', font = ('Walter Turncoat',17), width = 10, command = self.Search)
              Button_5.grid(row = 0, column = 4, padx = 8)
              Button_6 = Button(Button_Frame, text = 'Delete', font = ('Walter Turncoat',17), width = 10, command = self.Delete)
              Button_6.grid(row = 0, column = 5, padx = 8)
              Button_7 = Button(Button_Frame, text = 'Exit', font = ('Walter Turncoat',17), width = 10, command = self.Exit)
              Button_7.grid(row = 0, column = 6, padx = 8)

       #Functions
       def Display(self):
               # Clear the Treeview
              for item in self.tree.get_children():
                     self.tree.delete(item)

              # Fetch the updated data from the database
              records = Library_Backend.view()

              # Repopulate the Treeview with the updated data
              for row in records:
                     self.tree.insert("", 'end', values=row)
              self.root.update_idletasks()  # Force GUI update
              self.root.update()
                            
       def Insert(self):
              if(len(self.title.get()) != 0):
                     Library_Backend.insert(self.ID.get(), self.title.get(), self.author.get(), self.edsn.get(), self.yop.get(), self.borrow.get(), self.due.get(), self.issued_days.get(), self.overdue_status.get())
                     self.List_of_Books.append(self.title.get())
                     all_rows = Library_Backend.view()  # Fetch all rows
                     self.refresh_book_list(all_rows)
                                                       
       def Exit(self):
              Exit = tkinter.messagebox.askyesno('Library Management System','Confirm if you want to Exit')
              if Exit > 0:
                     root.destroy()
                     return
                                                               
       def Reset(self):
              self.ID.set('')
              self.title.set('')
              self.author.set('')
              self.edsn.set('')
              self.yop.set('')
              self.issued_days.set('')
              self.overdue_status.set('')
              self.initialize_dates()

       def Search(self):
              search_results = Library_Backend.search(self.ID.get(), self.title.get(), self.author.get(), self.edsn.get(), self.yop.get(), self.borrow.get())
              self.refresh_book_list(search_results)

       def update_issue_info(self):
              try:
                     borrowed_date_str = self.borrow.get()
                     borrowed_date = datetime.strptime(borrowed_date_str, "%Y-%m-%d").date()
                     due_date = borrowed_date + timedelta(days=14)
                     current_date = date.today()
                     issued_days_count = (current_date - borrowed_date).days

                     self.issued_days.set(str(issued_days_count))
                     self.due.set(str(due_date))

                     if issued_days_count > 14:
                            self.overdue_status.set("Overdue")
                     elif issued_days_count == 14:
                            self.overdue_status.set("Due Today")
                     else:
                            self.overdue_status.set("Not Overdue")
              except ValueError:
                     # Handle case where date is not set properly
                     self.issued_days.set("N/A")
                     self.overdue_status.set("N/A")


       def on_tree_select(self, event):
        # Get selected item
              selected_item = self.tree.selection()

              if selected_item:  # Check if something is actually selected
              # Assuming the first column in Treeview is the ID
                     item = self.tree.item(selected_item)
                     row = item['values']

                     # Update the textboxes
                     # Assuming you have Entry widgets named like self.Entry_0, self.Entry_1, ...
                     selected_x = row[0]
                     self.selected_x = selected_x
                     self.ID.set(row[1])
                     self.title.set(row[2])
                     self.author.set(row[3])
                     self.edsn.set(row[4])
                     self.yop.set(row[5])
                     self.borrow.set(row[6])
                     self.due.set(row[7])
                     self.issued_days.set(row[8])
                     self.overdue_status.set(row[9])

              # ... continue for other entries ...

       def Delete(self):
              if self.selected_x:  # Ensure a row is selected
                     Library_Backend.delete(self.selected_x)
                     all_rows = Library_Backend.view()  # Fetch all rows
                     self.refresh_book_list(all_rows)

       def Update(self):
              if self.selected_x:  # Ensure a row is selected
                     Library_Backend.update(self.selected_x, self.ID.get(), self.title.get(), self.author.get(), self.edsn.get(), self.yop.get(), self.borrow.get(), self.due.get(), self.issued_days.get(), self.overdue_status.get())
                     all_rows = Library_Backend.view()  # Fetch all rows
                     self.refresh_book_list(all_rows)

       def refresh_book_list(self, rows):
              for i in self.tree.get_children():
                     self.tree.delete(i)

              # Repopulate the Treeview with the given rows
              for row in rows:
                     self.tree.insert("", 'end', values=row)

       def initialize_dates(self):
              today = date.today()
              due_date = today + timedelta(days=14)
              self.due.set(due_date.strftime("%Y-%m-%d"))
              self.borrow.set(today.strftime("%Y-%m-%d"))
       
       
if __name__ == '__main__':
       root = Tk()
       applicaton = Library(root)
       root.mainloop()
