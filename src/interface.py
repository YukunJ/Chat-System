import  tkinter as tk
from tkinter import filedialog



class INTERFACE:
    
    def __init__(self,username):
        ##initialize the window
        self.root = tk.Tk()
        self.root.title("ICS Final Project Show--Graphical User Interface")
        self.root.geometry = ('1000x1000')
        self.text_out = []
        self.Initialize_Username(username)
        self.Make_Frame()
        self.Make_Title()
        self.Make_Outputbox()
        self.Make_Enterbox()
        self.Make_Txtbutton()
        self.Make_clearbutton()
        self.Make_Enterbutton()
        self.Make_Menu()
        self.root.bind("<Return>",self.connect_enter_press)
    def Make_Menu(self):
        overall_menubar = tk.Menu(self.root)
        first_list_menubar = tk.Menu(overall_menubar, tearoff = 0)
        overall_menubar.add_cascade( label = 'Shakespeare', menu = first_list_menubar)
        def show_shakespeare1():
            sub_window = tk.Toplevel( self.root)
            sub_window.geometry('350x200')
            sub_window.title('I')
            tk.Label( sub_window, text = '\nMy bounty is as boundless as the sea,\n\nMy love as deep; the more I give to thee,\n\nThe more I have, for both are infinite.\n\n                 ————< Romeo and Juliet >',font = ("Helvetica","14","bold italic")).pack()
        first_list_menubar.add_command( label = 'I', command = show_shakespeare1)
        def show_shakespeare2():
            sub_window = tk.Toplevel( self.root)
            sub_window.geometry('350x200')
            sub_window.title('II')
            tk.Label( sub_window, text = '\nHear my soul speak: \n\nThe very instant that I saw you, did \n\nMy heart fly to your service.\n\n                 ————< The Tempest >',font = ("Helvetica","14","bold italic")).pack()
        first_list_menubar.add_command( label = 'II', command = show_shakespeare2)
        def show_shakespeare3():
            sub_window = tk.Toplevel( self.root)
            sub_window.geometry('350x200')
            sub_window.title('III')
            tk.Label( sub_window, text = '\nIf thou remember’st not the slightest folly \n\nThat ever love did make thee run into, \n\nThou hast not loved.    \n\n                 ————< As You Like It >',font = ("Helvetica","14","bold italic")).pack()
        first_list_menubar.add_command( label = 'III', command = show_shakespeare3)
        def show_shakespeare4():
            sub_window = tk.Toplevel( self.root)
            sub_window.geometry('350x200')
            sub_window.title('IV')
            tk.Label( sub_window, text = '\nLove alters not with his brief hours and weeks, \n\nBut bears it out even to the edge of doom. \n\nIf this be error and upon me proved, \n\n I never writ, nor no man ever loved. \n\n               ————< Sonnet 116 >',font = ("Helvetica","14","bold italic")).pack()
        first_list_menubar.add_command( label = 'IV', command = show_shakespeare4)
        def show_shakespeare5():
            sub_window = tk.Toplevel( self.root)
            sub_window.geometry('350x200')
            sub_window.title('V')
            tk.Label( sub_window, text = '\nDoubt thou the stars are fire;\n\nDoubt that the sun doth move;\n\nDoubt truth to be a liar;\n\n But never doubt I love.\n\n               ————< Hamlet >',font = ("Helvetica","14","bold italic")).pack()
        first_list_menubar.add_command( label = 'V', command = show_shakespeare5)
        def show_shakespeare6():
            sub_window = tk.Toplevel( self.root)
            sub_window.geometry('350x200')
            sub_window.title('VI')
            tk.Label( sub_window, text = '\nWhen Love speaks, the voice of all the gods\n\nMakes heaven drowsy with the harmony.\n\n               ————< Love’s Labour’s Lost >',font = ("Helvetica","14","bold italic")).pack()
        first_list_menubar.add_command( label = 'VI', command = show_shakespeare6)
        def show_shakespeare7():
            sub_window = tk.Toplevel( self.root)
            sub_window.geometry('350x200')
            sub_window.title('VII')
            tk.Label( sub_window, text = '\nLove is a spirit all compact of fire.\n\n               ————< Venus and Adonis >',font = ("Helvetica","14","bold italic")).pack()
        first_list_menubar.add_command( label = 'VII', command = show_shakespeare7)
        def show_shakespeare8():
            sub_window = tk.Toplevel( self.root)
            sub_window.geometry('400x200')
            sub_window.title('VIII')
            tk.Label( sub_window, text = '\nLove goes toward love as school-boys from their books,\n\nBut love from love, toward school with heavy looks.\n\n               ————< Romeo and Juliet >',font = ("Helvetica","14","bold italic")).pack()
        first_list_menubar.add_command( label = 'VIII', command = show_shakespeare8)
        def show_shakespeare9():
            sub_window = tk.Toplevel( self.root)
            sub_window.geometry('350x200')
            sub_window.title('IX')
            tk.Label( sub_window, text = '\nIf music be the food of love, play on;\n\nGive me excess of it, that, surfeiting,\n\n The appetite may sicken, and so die.\n\n              ————< Twelfth Night >',font = ("Helvetica","14","bold italic")).pack()
        first_list_menubar.add_command( label = 'IX', command = show_shakespeare9)
        def show_shakespeare10():
            sub_window = tk.Toplevel( self.root)
            sub_window.geometry('400x200')
            sub_window.title('X')
            tk.Label( sub_window, text = '\nI can express no kinder sign of love, than this kind kiss.\n\nYou got something better? We’d love to hear it.\n\n   ————< Cymbeline>',font = ("Helvetica","14","bold italic")).pack()
        first_list_menubar.add_command( label = 'X', command = show_shakespeare10)
        self.root.config(menu= overall_menubar)
    def Make_Frame(self):
        ##create Frame and sub-Frame(up one and down one)
        frame = tk.Frame(self.root)
        self.frame = frame
        frame.pack()
        frame_up = tk.Frame(frame).pack(side = 'top')
        self.frame_up = frame_up
        frame_down = tk.Frame(frame).pack(side = 'bottom')
        self.frame_down = frame_down
        frame_bottom = tk.Frame(frame).pack(side = 'bottom')
        self.frame_bottom = frame_bottom

    def Make_Title(self):
        title_text = self.username + ", Final is coming! Study Hard! "
        title_label = tk.Label(self.frame_up, text = title_text, font = ("Helvetica","16","bold italic"))
        title_label.pack()
        
    def Make_Outputbox(self): 
        ##create outputbox on the upper frame
        self.outputbox = tk.Text(self.frame_up, bg = "#F0F8FF", font = ("Arial",13), width = 70, height = 25)
        self.outputbox.pack(anchor = 'w')
        
    def Make_Enterbox(self):
        ##create enterbox on the lower frame left position
        self.enterboxvariable = tk.StringVar()
        self.enterbox = tk.Entry(self.frame_down, bg = "#F0F8FF", font = ("Arial",15), textvariable = self.enterboxvariable, show = None, width = 50)
        self.enterbox.pack(side = 'left')
        
        
    def Make_Enterbutton(self):
        ##create enterbutton on the lower frame right position
        self.enterbutton = tk.Button(self.frame_down, text = "Enter", width = 6,
                              height = 2, command = self.output_to_server)
        self.enterbutton.pack(side = 'right')
        
        
    def Make_Txtbutton(self):
        ##choose a txt file and get its name. we read it and record it and then send it to the Enter box
        def up_load_txt():
            filename = tk.filedialog.askopenfilenames(title="choose a txt. file to send")
            fileobject = open(filename[0], 'r',encoding='utf-8')
            content = fileobject.readlines()
            fileobject.close()
            ##on your peer's screen, show what you have sent
            start_message = "--Start file transfer:  "+"<"+filename[0]+">--"
            self.enterboxvariable.set(start_message)
            self.output_to_server()
            for each_line in content:
                self.enterboxvariable.set(each_line.strip())
                self.output_to_server()
            end_message = "--File transfer ended.--"
            self.enterboxvariable.set(end_message)
            self.output_to_server()
            
            
        txt_button = tk.Button(self.frame_bottom, text = "file transfer", width = 9,
                               height = 2, command = up_load_txt)
        txt_button.pack(side = 'right')
        
    def Make_clearbutton(self):
        clearbutton = tk.Button(self.frame_down, text = "Clear", width = 6,
                                height =2, command = self.clear)
        clearbutton.pack(side = 'right')
        
    def clear(self):
            self.outputbox.delete('1.0','end')      
    def Initialize_Username(self,username):
        ##initialize user name,this will be used as you finish the login interface and you store your username here
        self.username = username
        self.text_out = [username]

    def connect_enter_press(self,event):
        self.text_out += [self.enterboxvariable.get()]
        self.enterboxvariable.set('')

    def output_to_server(self):
        self.text_out += [self.enterboxvariable.get()]
        self.enterboxvariable.set('')
    
    def get_message_print(self,message):
        self.outputbox.insert('end',message)
        
        
    
def main():
    Root = INTERFACE('Jason')
    Root.root.mainloop()




if __name__=='__main__':
    main()
