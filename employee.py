from tkinter import* 
from tkinter import ttk
from PIL import Image, ImageTk


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Management System")


        lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('arial',37,'bold'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1530,height=50)

        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=220,width=1500,height=560)

        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information',font=('arial',11,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1480,height=270)



if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()