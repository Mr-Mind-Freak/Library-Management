import tkinter as tk
from typing import Final
import New_Account as NA ,Open_Account as OA, LogIn  
import Book_Management as bm 

class HomePage():
    '''This class is used to create welcome page and set up the menu bar.'''
    def __init__(self):
        self.window = tk.Tk()
        pic1 = tk.PhotoImage(file='liabrary_image.png') 
        self.window.title('Welcome Page')
        self.window.config(bg='#0d0342',)
        self.window.iconphoto(True,pic1)  
        WIDTH  : Final[int]= 500  
        HEIGHT : Final [int] = 500  
        x = int(self.window.winfo_screenwidth()/2 - WIDTH/2)
        y = int(self.window.winfo_screenheight()/2 - HEIGHT/2)
        self.window.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")
        self.welcome_frame = tk.Frame(self.window,bg='#0d0342')   
        self.welcome_frame.pack(pady=20)
        tk.Label(self.welcome_frame,text = 'Welcome To Liabrary',image=pic1,compound=tk.TOP,\
                 font =("Comic Sans MS", 20, "bold"),fg='white',bg='#0d0342').pack()
        button = tk.Button(self.welcome_frame,text = 'Next',bg='#00ff86',font=('Aharoni',15,'bold'),width=6,\
                  relief = tk.RAISED,command = self.createmenu,cursor = 'hand2')
        button.pack(pady=10)
        button.focus_set() 
        button.bind("<Return>",self.createmenu)
        self.window.mainloop()

    def createmenu(self,*args):
        self.welcome_frame.destroy()
        menubar = tk.Menu(self.window)
        menu_val = { 
            "File" : { 
            "New Account" : lambda: NA.create_new_account(self.window),
            "Open Account" : lambda: OA.open_account(self.window),
            "Exit" : quit
            },
            "Login" : lambda: LogIn.login_account(self.window),
            "Add Book" : lambda: bm.add_book(self.window),
            "Get Book" : lambda: bm.get_book(self.window),
            "Renual Book" : lambda: bm.renual_book(self.window),
            "Return Book" : lambda: bm.return_book(self.window),
            "Search Book" : lambda: bm.search_book(self.window),
            "Exit" : quit
        }
        for key,val in menu_val.items(): 
            if isinstance(val,dict):
                file = tk.Menu(menubar,tearoff=0)
                menubar.add_cascade(label=key,menu=file)
                for key2,val2 in val.items():
                    if key2 == 'Exit':
                        file.add_separator()
                    file.add_command(label=key2,command=val2)   
            else:
                menubar.add_separator()
                menubar.add_command(label=key,command=val) #
        self.window.config(menu = menubar)

def main():
    HomePage()  
    

if __name__ == '__main__':
    main()