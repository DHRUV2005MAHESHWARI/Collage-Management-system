from tkinter import*
import os
import platform

def Marksheet():
       filename = 'Marksheet_Search.py'

       # Determine the operating system
       if platform.system() == 'Windows': 
              # Windows-specific command
              os.system('python ' + filename)  # Assuming 'python' works on the user's Windows setup
                  # Open with VS Code on Windows
       elif platform.system() == 'Darwin':
              # macOS-specific command
              os.system('python3 ' + filename)  # macOS usually uses 'python3'
               # Replace with the macOS text editor command
       else:
              # Linux or other Unix-like OS
              os.system('python3 ' + filename)
                # Open with gedit on Linux

def Library():
       filename = 'Library.py'
       
       if platform.system() == 'Windows':
              os.system('python ' + filename)
              
       elif platform.system() == 'Darwin':
              os.system('python3 ' + filename)
              
       else:
              os.system('python3 ' + filename)
              


def StudentInformation():
       filename = 'Student_Information.py'

       if platform.system() == 'Windows':
              os.system('python ' + filename)
              
       elif platform.system() == 'Darwin':
              os.system('python3 ' + filename)
              
       else:
              os.system('python3 ' + filename)
              


def Fee():
       filename = 'Fee.py'
    
       if platform.system() == 'Windows':
              os.system('python ' + filename)
              
       elif platform.system() == 'Darwin':
              os.system('python3 ' + filename)
              
       else:
              os.system('python3 ' + filename)
              

       
def menu():
       root = Tk()
       root.title('Menu')
       root.geometry('1350x750')
       root.config(bg = 'light blue')
       
       title_Frame = LabelFrame(root, font = ('Walter Turncoat',50), width = 1000, height = 100, bg = 'light blue')
       title_Frame.grid(row = 0, column = 0, pady = 50)
       
       title_Label = Label(title_Frame, text = 'College Management System!', font = ('Walter Turncoat', 30), bg = 'light blue')
       title_Label.grid(row = 0, column = 0, padx = 50)

       #Frames
       Frame_1 = LabelFrame(root, font = ('Walter Turncoat',17), width = 1000, height = 100, bg = 'light blue')
       Frame_1.grid(row = 1, column = 0, padx = 280, pady = 7)
       Frame_2 = LabelFrame(root, font = ('Walter Turncoat',17), width = 1000, height = 100, bg = 'light blue')
       Frame_2.grid(row = 2, column = 0, padx = 280, pady = 7)
       Frame_3 = LabelFrame(root, font = ('Walter Turncoat',17), width = 1000, height = 100, bg = 'light blue')
       Frame_3.grid(row = 3, column = 0, padx=280, pady = 7)
       Frame_4 = LabelFrame(root, font = ('Walter Turncoat',17), width = 1000, height = 100, bg = 'light blue')
       Frame_4.grid(row = 4, column = 0, padx=280, pady = 7)
       
       #Labels
       Label_1 = Label(Frame_1, text = 'Student Profile', font = ('Walter Turncoat',25), bg = 'light blue')
       Label_1.grid(row = 0, column = 0, padx = 61, pady = 5)
       Label_2 = Label(Frame_2, text = 'Fee Information', font = ('Walter Turncoat',25), bg = 'light blue')
       Label_2.grid(row = 0, column = 0, padx = 58, pady = 5)
       Label_3 = Label(Frame_3, text = 'Library System', font = ('Walter Turncoat',25), bg = 'light blue')
       Label_3.grid(row = 0, column = 0, padx = 63, pady = 5)
       Label_4 = Label(Frame_4, text = 'Marksheet', font = ('Walter Turncoat',25), bg = 'light blue')
       Label_4.grid(row = 0, column = 0, padx = 90, pady = 5)
       
       #Buttons
       Button_1 = Button(Frame_1, text = 'Open', font = ('Sniglet',16), width = 8, command = StudentInformation)
       Button_1.grid(row = 0, column = 3, padx = 50)
       Button_2 = Button(Frame_2, text = 'Open', font = ('Sniglet',16), width = 8, command = Fee)
       Button_2.grid(row = 0, column = 3, padx = 50)
       Button_3 = Button(Frame_3, text = 'Open', font = ('Sniglet',16), width = 8, command = Library)
       Button_3.grid(row = 0, column = 3, padx = 50)
       Button_4 = Button(Frame_4, text = 'Open', font = ('Sniglet',16), width = 8, command = Marksheet)
       Button_4.grid(row = 0, column = 3, padx = 50)

       root.mainloop()
  
if __name__ == '__main__':
       menu()
