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

        #Department
        lbl_dept=Label(upper_frame,text="Department", font=('arial',12,'bold'), bg='white')
        lbl_dept.grid(row=0, column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(upper_frame, font=('arial',11,'bold'), width=17, state='readonly')
        combo_dep['value']=('Select Department', 'HR', 'Administrative', 'IT', 'Operations', 'Marketing', 'Sales', 'Finance', 'Production')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Name
        lbl_Name=Label(upper_frame,text="Name:", font=('arial',12,'bold'), bg='white')
        lbl_Name.grid(row=0, column=2,padx=2,pady=7,sticky=W)

        txt_Name=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_Name.grid(row=0,column=3,padx=2,pady=7)

        #Designition
        lbl_Designition=Label(upper_frame,text="Designition:", font=('arial',12,'bold'), bg='white')
        lbl_Designition.grid(row=1, column=0,padx=2,pady=7,sticky=W)

        txt_Designition=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_Designition.grid(row=1,column=1,padx=2,pady=7)

        #Email
        lbl_email=Label(upper_frame,text="Email:", font=('arial',12,'bold'), bg='white')
        lbl_email.grid(row=1, column=2,padx=2,pady=7,sticky=W)

        txt_email=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_email.grid(row=1,column=3,padx=2,pady=7)

        #Address 
        lbl_address=Label(upper_frame,text="Address:", font=('arial',12,'bold'), bg='white')
        lbl_address.grid(row=2, column=0,padx=2,pady=7,sticky=W)

        txt_address=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_address.grid(row=2,column=1,padx=2,pady=7)

        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information Table',font=('arial',11,'bold'),fg='red')
        down_frame.place(x=10,y=280,width=1480,height=270)

        #Married 
        lbl_married=Label(upper_frame,text="Maritial Status:", font=('arial',12,'bold'), bg='white')
        lbl_married.grid(row=2, column=2,padx=2,pady=7,sticky=W)

        combo_dep=ttk.Combobox(upper_frame, font=('arial',11,'bold'), width=18, state='readonly')
        combo_dep['value']=('Married','Unmarried')
        combo_dep.current(0)
        combo_dep.grid(row=2,column=3,padx=2,pady=7,sticky=W)

        #DOB 
        lbl_dob=Label(upper_frame,text="Date of Birth:", font=('arial',12,'bold'), bg='white')
        lbl_dob.grid(row=3, column=0,padx=2,pady=7,sticky=W)

        txt_dob=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_dob.grid(row=3,column=1,padx=2,pady=7)

        #DOJ 
        lbl_doj=Label(upper_frame,text="Date joined:", font=('arial',12,'bold'), bg='white')
        lbl_doj.grid(row=3, column=2,padx=2,pady=7,sticky=W)

        txt_doj=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_doj.grid(row=3,column=3,padx=2,pady=7)

        #ID
        com_txt_proof=ttk.Combobox(upper_frame, font=('arial',12,'bold'), width=18, state='readonly')
        com_txt_proof['value']=('Select ID Type','Drivers License','Work permit', 'Canadian Citizen', 'Permanent Resident')
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=0,padx=2,pady=7,sticky=W)  

        txt_proof=ttk.Entry(upper_frame,width=22, font=('arial',11,'bold'))
        txt_proof.grid(row=4,column=1,padx=2,pady=7,sticky=W)  

        #Gender
        lbl_gender=Label(upper_frame,text="Gender:", font=('arial',12,'bold'), bg='white')
        lbl_gender.grid(row=4, column=2,padx=2,pady=7,sticky=W)

        com_txt_gender=ttk.Combobox(upper_frame, font=('arial',12,'bold'), width=18, state='readonly')
        com_txt_gender['value']=('Male', 'Female', 'Other')
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4,column=3,padx=2,pady=7,sticky=W) 

        #Phone
        lbl_phone=Label(upper_frame,text="Phone No:", font=('arial',12,'bold'), bg='white')
        lbl_phone.grid(row=0, column=4,padx=2,pady=7,sticky=W)

        txt_phone=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_phone.grid(row=0,column=5,padx=2,pady=7)

        #Country 
        lbl_country=Label(upper_frame,text="Country:", font=('arial',12,'bold'), bg='white')
        lbl_country.grid(row=1, column=4,padx=2,pady=7,sticky=W)

        txt_country=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_country.grid(row=1,column=5,padx=2,pady=7)

        #Salary
        lbl_salary=Label(upper_frame,text="Annual Salary:", font=('arial',12,'bold'), bg='white')
        lbl_salary.grid(row=2, column=4,padx=2,pady=7,sticky=W)

        txt_salary=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_salary.grid(row=2,column=5,padx=5,pady=7)

        #Button Frame
        Button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        Button_frame.place(x=1290,y=10,width=170,height=210)

        btn_add=Button(Button_frame, text="Add",font=('arial',15,'bold'),width=13,bg='black',fg='white')
        btn_add.grid(row=0,column=0,padx=1,pady=5)

        btn_update=Button(Button_frame, text="Update",font=('arial',15,'bold'),width=13,bg='black',fg='white')
        btn_update.grid(row=2,column=0,padx=1,pady=5)

        btn_delete=Button(Button_frame, text="delete",font=('arial',15,'bold'),width=13,bg='black',fg='white')
        btn_delete.grid(row=3,column=0,padx=1,pady=5)

        btn_clear=Button(Button_frame, text="clear",font=('arial',15,'bold'),width=13,bg='black',fg='white')
        btn_clear.grid(row=4,column=0,padx=1,pady=5)

        #Search Frame
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text='Search Employee Information',font=('arial',11,'bold'),fg='red')
        search_frame.place(x=0,y=0,width=1470,height=60)

        search_by=Label(search_frame,font=('arial',11,'bold'),text="Search By:",fg="white",bg="red")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        #Search
        com_txt_search=ttk.Combobox(search_frame, font=('arial',12,'bold'), width=18, state='readonly')
        com_txt_search['value']=('Select Option',"Phone","ID")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,padx=5,sticky=W)

        txt_search=ttk.Entry(search_frame,width=22,font=('arial',11,'bold'))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(search_frame, text="Search",font=('arial',11,'bold'),width=14,bg='black',fg='white')
        btn_search.grid(row=0,column=3,padx=5)

        btn_ShowAll=Button(search_frame, text="Show All",font=('arial',11,'bold'),width=14,bg='black',fg='white')
        btn_ShowAll.grid(row=0,column=4,padx=5)

        #Table Frame
        table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,columns=("dep","name","desig","email","address","married","dob","doj","id",))

if __name__=="__main__":
    root=Tk()
    obj=Employee(root )
    root.mainloop()