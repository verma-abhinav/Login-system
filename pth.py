from tkinter import*
from  PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()


#messagebox.showerror("error","error not found")

class login_system:
    def __init__(self, root):
        self.root = root
        self.root.title(' LOGIN SYSTEM ')
        self.root.geometry('512x512+0+0')


        #==========ALL IMAGES========================



        bg= Image.open('dcjj.jpg')
        bg= bg.resize((1360, 720))

        ug = Image.open('uicon1.png')
        ug = ug.resize((40, 40))

        pg = Image.open('sdsa.png')
        pg = pg.resize((80, 80))
        lg = Image.open('jlkk.jpg')
        lg = lg.resize((150, 150))



        self.bg_icon = ImageTk.PhotoImage(bg)
        self.user_icon = ImageTk.PhotoImage(ug)
        self.p_icon = ImageTk.PhotoImage(pg)
        self.logo_icon= ImageTk.PhotoImage(lg)

        #============Variables====================

        self.uname = StringVar()
        self.passn = StringVar()




        bg_lbl= Label(self.root,image= self.bg_icon).pack()

        title= Label(self.root,text='FACIAL RECOGNITION BASED ATTENDANCE SYSTEM',font= ('times new roman',30,'bold'), bg='grey',fg='white',bd=5,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        login_frame= Frame(self.root,bg='white')
        login_frame.place(x=450,y=150)

        logolbl= Label(login_frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)

        lbluser = Label(login_frame, text='Student Name', image=self.user_icon, compound=LEFT,
                        font= ('times new roman',15,'bold'),bg='white',).grid(row=1,column=0,padx=0,pady=0)
        txtuser = Entry(login_frame,bd=5,textvariable=self.uname, relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)

        lblpass = Label(login_frame, text='College ID', image=self.p_icon, compound=LEFT,
                        font=('times new roman', 15, 'bold'), bg='white', ).grid(row=2, column=0, padx=0, pady=0)
        txtpass = Entry(login_frame, bd=5,textvariable=self.passn, relief=GROOVE, font=("", 15)).grid(row=2, column=1, padx=20)

        btn = Button(login_frame,text='LOGIN',width=15,font=('times new roman',14, 'bold'),bg='black',fg='white').grid(row=3,column=1,pady=10)


        #messagebox.showerror("error","erroooerrergsd")



    #==============function===================
    def login(self):
        if self.uname.get()=="" or self.passn.get()=="":
            messagebox.showerror("Error", " ALL Fields Are Required ")

        elif self.uname.get()=="Abhinav" and self.passn.get()=="9634":
            messagebox.showinfo("Successful", f"Welcome {self.uname.get()}")

        else:
            messagebox.showerror("Error", "Invalid Student name or Password")


obj = login_system(root)
root.mainloop()