import  tkinter as tk
from tkinter import messagebox
import pickle
from k_shift_encryption import *
def login_in():
    ## basic setting up, the dictionary is for, if you enter 3 times wrong, you will be locked out
    login_in_window = tk.Tk()
    login_in_window.title( "Welcome to NYUSH Chat System" )
    login_in_window.geometry( '450x300' )
    Wrong_Times = dict()

    ## define a function to read the previous wrong record of password input
    def load_dictionary():
        fileobject = open('Wrong_Times.txt','r')
        line = fileobject.readline()
        while len(line) > 1:
            linelist=line.strip().split()
            Wrong_Times[linelist[0]] = linelist[1]
            line = fileobject.readline()
        fileobject.close()
        
    ## define a function to dump the current dictionary to the file txt.
    def dump_dictionary():
        fileobject = open('Wrong_Times.txt','w')
        for account, wrong_times in Wrong_Times.items():
            fileobject.write(account+' '+str(wrong_times)+'\n')
        fileobject.close()
    ##load the dictionary record
    load_dictionary()
    
    ## make the NYUSH badge
    canvas = tk.Canvas( login_in_window, height = 200, width = 500)
    nyush_image = tk.PhotoImage(file = 'NYUSH.gif')
    image = canvas.create_image( 0, 0, anchor = 'nw', image = nyush_image)
    canvas.pack(side = 'top')    

    ## make the username and password Labels and entry boxes
    user_account = tk.StringVar()
    user_password = tk.StringVar()
    user_account.set( 'Joyce@nyu.edu' )## Here gives user an example of what the account looks like
    user_account_label = tk.Label( login_in_window, text = 'User account: ',font = ("Helvetica","16","bold italic")).place(x = 50, y = 150)
    user_password_label=tk.Label( login_in_window,text = 'Password: ',font = ("Helvetica","16","bold italic")).place(x = 50,y = 190) 
    user_account_entry = tk.Entry( login_in_window, textvariable = user_account).place(x = 160,y = 150)
    user_password_entry = tk.Entry(login_in_window, textvariable = user_password,show = '*').place(x = 160,y = 190)

    ## make the two buttons and the function associated with it
    def try_login():
        account = user_account.get()
        password = user_password.get()
        fileobject = open( 'account_info.txt','r')
        line = fileobject.readline()
        Found_Name_Statue = False
        Successful_Login = False
        while len(line)>1:
            linelist = k_shift_decrypt(line.strip()).split()# all the lines are of the form "Joyce@nyu.edu jy123123 JoyceFu(account password username)"
            if account == linelist[0]:
                Found_Name_Statue = True
                if password == linelist[1]:##in this case, login is successful, use the username to continue to the interface
                    if int(Wrong_Times.get(account, 0)) < 3:
                        Successful_Login = True
                        username = linelist[2]
                        temporary_file = open('temporary_login_name.txt','w')
                        temporary_file.write(username)
                        temporary_file.close()
                        Wrong_Times[account] = 0
                        dump_dictionary()
                        login_in_window.destroy()
                    else:
                        tk.messagebox.showerror(title = 'Locked out', message = 'Your account has been locked.\nPlz contact 宇昆 jy2363@nyu.edu to unlock your account')
                   
                else:
                    Wrong_Times[account] = int(Wrong_Times.get(account, 0)) + 1
                    dump_dictionary()
                    if  Wrong_Times[account] < 3:
                        tk.messagebox.showerror( title = 'Error', message = 'Error, your password is wrong, try again.\n'+'You have '+str(3-Wrong_Times[account])+' chances left before being locked')
                    else:
                        tk.messagebox.showerror(title = 'Locked out', message = 'Your account has been locked.\nPlz contact 宇昆 jy2363@nyu.edu to unlock your account')
            line = fileobject.readline()
        fileobject.close()
        if Found_Name_Statue == False:
            want_sign_up = tk.messagebox.askyesno( title='UnFound', message = 'You have not signed up. Sign up today?')
            if want_sign_up == True:##if user choose to sign up, then pop out the sign_up_window
                sign_up_window()
                
    def sign_up_window():
        #basic setting up of the sub_window,making the 4 Labels and Entry boxes and the 'sign up' botton
        sign_up_window = tk.Toplevel( login_in_window)
        sign_up_window.geometry('350x200')
        sign_up_window.title('Sign Up Window')
        sign_account = tk.StringVar()
        sign_account.set('Joyce@nyu.edu')
        sign_password = tk.StringVar()
        sign_password_confirm = tk.StringVar()
        sign_username = tk.StringVar()

        tk.Label( sign_up_window,text = 'User Account: ', font = ("Helvetica","14","bold italic")).place(x = 10,y = 10)
        new_account_entry = tk.Entry( sign_up_window, textvariable = sign_account).place(x = 150,y = 10)

        tk.Label( sign_up_window, text = 'Password: ', font = ("Helvetica","14","bold italic")).place(x = 10,y = 50)
        new_password_entry = tk.Entry(sign_up_window,textvariable = sign_password,show = '*').place(x = 150,y = 50)

        tk.Label(sign_up_window,text = 'Comfirm Password: ',font = ("Helvetica","14","bold italic")).place(x = 10,y = 90)
        new_password_confirm_entry = tk.Entry( sign_up_window,textvariable = sign_password_confirm,show = '*').place(x = 150,y = 90)

        tk.Label(sign_up_window,text = 'User Name: ',font = ("Helvetica","14","bold italic")).place(x = 10,y = 130)
        new_user_name_entry = tk.Entry(sign_up_window,textvariable = sign_username).place(x = 150,y = 130)

        # define the sign_up function here, which to be used in the button
        def try_sign_up():
            account = sign_account.get()
            password = sign_password.get()
            password_confirm = sign_password_confirm.get()
            username = sign_username.get()
            fileobject = open('account_info.txt','r')
            line = fileobject.readline()
            # 3 Boolen variable we needs to use
            Account_Used = False
            Password_Inconsistent = False
            Username_Used = False
            if password != password_confirm:
                Password_Inconsistent = True
            
            while len(line)>0:
                linelist = k_shift_decrypt(line.strip()).split()
                if account == linelist[0]:
                    Account_Used = True
                else:
                    if username == linelist[2]:
                        Username_Used = True
                line = fileobject.readline()
            fileobject.close()
            if Account_Used == True:
                tk.messagebox.showerror(title = 'Error',message = 'Account already signed up, plz try another')
            elif Password_Inconsistent == True:
                tk.messagebox.showerror(title ='Error',message ='Passwords are not consistent, plz check it')
            elif Username_Used == True:
                tk.messagebox.showerror(title ='Error',message ='Username already signed up,plz try another')
            else: ##everything is fine, correct this new account in the .txt file and close the sign_up window
                fileobject = open('account_info.txt','a')
                fileobject.write(k_shift_encrypt('\n'+account+' '+password+' '+username))
                fileobject.close()
                tk.messagebox.showinfo(title = 'Welcome',message = 'You have successfully signed up')
                sign_up_window.destroy()
         #this is the button that would use the sign up function we created above, it's on the sub_window       
        try_sign_up_button=tk.Button(sign_up_window,text='Sign Up',command=try_sign_up).place(x=150,y=170)
        
    #these 2 are the buttons on the main_window
    login_button=tk.Button(login_in_window,text='Login',command=try_login).place(x=170,y=230)
    sign_up_button=tk.Button(login_in_window,text='Sign up',command=sign_up_window).place(x=270,y=230)
    
    ## do the mainloop
    login_in_window.mainloop()

def main():
    login_in()

if __name__ == '__main__':
    main()
