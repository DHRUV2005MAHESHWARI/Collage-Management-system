from tkinter import * 
import os
import platform 
import Marksheet_Backend
import Marksheet
import tkinter.messagebox

class Window_1():
       def __init__(self, master):
              self.master = master
              self.master.title('Search Page')
              self.master.geometry('1350x750')
              self.master.config(bg = 'light blue')

              self.roll = StringVar()
              frame = LabelFrame(self.master, width = 1000, height = 100, font = ('Sniglet', 20), relief = 'ridge', bg = 'light blue')
              frame.grid(row = 1, column = 0, padx = 200, pady = 200)

              label = Label(frame, text = 'Enter Roll Number:', font = ('Walter Turncoat', 20), bg = 'light blue' )
              label.grid(row = 0, column = 0, padx = 100, pady = 10)

              entry = Entry(frame, font = ('Sniglet', 20), textvariable = self.roll)
              entry.grid(row = 0, column = 1, padx = 30, pady = 20)

              def Search():
                     if(len(self.roll.get()) != 0):
                           row = Marksheet_Backend.search(str(self.roll.get()))
                           print(row)
                           Marksheet.search_result_marksheet(row)
                     else:
                            tkinter.messagebox.askokcancel('Attention','Please enter valid Roll No.')
                            return

              def new():
                     filename = 'Marksheet.py'
                     
                     if platform.system() == 'Windows':
                            os.system('python ' + filename)
                            
                     elif platform.system() == 'Darwin':
                            os.system('python3 ' + filename)
                            
                     else:
                            os.system('python3 ' + filename)
                            
                           

              btnSearch = Button(frame, text = 'Search', width = 15, font = ('Walter Turncoat',17), command=Search)
              btnSearch.grid(row = 1, column = 0, padx = 50)
              btnNew = Button(frame, text = 'Create New', width = 15, font = ('Walter Turncoat',17), command=new)
              btnNew.grid(row = 1, column = 1, padx = 50, pady = 20 )

root = Tk()
root.title('Search Page')
Window_1(root)
root.mainloop()
