from tkinter import* 
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Management System")

        #Variables
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_designition=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproofcomb=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()

        lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('arial',37,'bold'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1530,height=50)

        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=220,width=1500,height=560)

        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information',font=('arial',11,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1480,height=270)

        #Department
        lbl_dept=Label(upper_frame,text="Department", font=('arial',12,'bold'), bg='white')
        lbl_dept.grid(row=0, column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep, font=('arial',11,'bold'), width=17, state='readonly')
        combo_dep['value']=('Select Department', 'HR', 'Administrative', 'IT', 'Operations', 'Marketing', 'Sales', 'Finance', 'Production')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Name
        lbl_Name=Label(upper_frame,text="Name:", font=('arial',12,'bold'), bg='white')
        lbl_Name.grid(row=0, column=2,padx=2,pady=7,sticky=W)

        txt_Name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial',11,'bold'))
        txt_Name.grid(row=0,column=3,padx=2,pady=7)

        #Designition
        lbl_Designition=Label(upper_frame,text="Designition:", font=('arial',12,'bold'), bg='white')
        lbl_Designition.grid(row=1, column=0,padx=2,pady=7,sticky=W)

        txt_Designition=ttk.Entry(upper_frame,textvariable=self.var_designition,width=22,font=('arial',11,'bold'))
        txt_Designition.grid(row=1,column=1,padx=2,pady=7)

        #Email
        lbl_email=Label(upper_frame,textvariable=self.var_designition,text="Email:", font=('arial',12,'bold'), bg='white')
        lbl_email.grid(row=1, column=2,padx=2,pady=7,sticky=W)

        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=('arial',11,'bold'))
        txt_email.grid(row=1,column=3,padx=2,pady=7)

        #Address 
        lbl_address=Label(upper_frame,text="Address:", font=('arial',12,'bold'), bg='white')
        lbl_address.grid(row=2, column=0,padx=2,pady=7,sticky=W)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('arial',11,'bold'))
        txt_address.grid(row=2,column=1,padx=2,pady=7)

        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information Table',font=('arial',11,'bold'),fg='red')
        down_frame.place(x=10,y=280,width=1480,height=270)

        #Married 
        lbl_married=Label(upper_frame,text="Maritial Status:", font=('arial',12,'bold'), bg='white')
        lbl_married.grid(row=2, column=2,padx=2,pady=7,sticky=W)

        combo_married=ttk.Combobox(upper_frame,textvariable=self.var_married, font=('arial',11,'bold'), width=18, state='readonly')
        combo_married['value']=('Married','Unmarried')
        combo_married.current(0)
        combo_married.grid(row=2,column=3,padx=2,pady=7,sticky=W)

        #DOB 
        lbl_dob=Label(upper_frame,text="Date of Birth:", font=('arial',12,'bold'), bg='white')
        lbl_dob.grid(row=3, column=0,padx=2,pady=7,sticky=W)

        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font=('arial',11,'bold'))
        txt_dob.grid(row=3,column=1,padx=2,pady=7)

        #DOJ 
        lbl_doj=Label(upper_frame,text="Date joined:", font=('arial',12,'bold'), bg='white')
        lbl_doj.grid(row=3, column=2,padx=2,pady=7,sticky=W)

        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=('arial',11,'bold'))
        txt_doj.grid(row=3,column=3,padx=2,pady=7)

        #ID
        com_txt_proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb, font=('arial',12,'bold'), width=18, state='readonly')
        com_txt_proof['value']=('Select ID Type','Drivers License','Work permit', 'Canadian Citizen', 'Permanent Resident')
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=0,padx=2,pady=7,sticky=W)  

        txt_proof=ttk.Entry(upper_frame,textvariable=self.var_idproof,width=22, font=('arial',11,'bold'))
        txt_proof.grid(row=4,column=1,padx=2,pady=7,sticky=W)  

        #Gender
        lbl_gender=Label(upper_frame,text="Gender:", font=('arial',12,'bold'), bg='white')
        lbl_gender.grid(row=4, column=2,padx=2,pady=7,sticky=W)

        com_txt_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender, font=('arial',12,'bold'), width=18, state='readonly')
        com_txt_gender['value']=('Male', 'Female', 'Other')
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4,column=3,padx=2,pady=7,sticky=W) 

        #Phone
        lbl_phone=Label(upper_frame,text="Phone No:", font=('arial',12,'bold'), bg='white')
        lbl_phone.grid(row=0, column=4,padx=2,pady=7,sticky=W)

        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=22,font=('arial',11,'bold'))
        txt_phone.grid(row=0,column=5,padx=2,pady=7)

        #Country 
        lbl_country=Label(upper_frame,text="Country:", font=('arial',12,'bold'), bg='white')
        lbl_country.grid(row=1, column=4,padx=2,pady=7,sticky=W)

        txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,width=22,font=('arial',11,'bold'))
        txt_country.grid(row=1,column=5,padx=2,pady=7)

        #Salary
        lbl_salary=Label(upper_frame,text="Annual Salary:", font=('arial',12,'bold'), bg='white')
        lbl_salary.grid(row=2, column=4,padx=2,pady=7,sticky=W)

        txt_salary=ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=('arial',11,'bold'))
        txt_salary.grid(row=2,column=5,padx=5,pady=7)

        #Button Frame
        Button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        Button_frame.place(x=1290,y=10,width=170,height=210)

        btn_add=Button(Button_frame,command=self.add_data, text="Add",font=('arial',15,'bold'),width=13,bg='black',fg='white')
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

        self.employee_table=ttk.Treeview(table_frame,columns=("dep","name","desig","email","address","married","dob","doj","idtype","idproof","gender","phone","country","salary",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)
        
        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('desig',text='Designation')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('address',text='Address')
        self.employee_table.heading('married',text='Married Status')
        self.employee_table.heading('dob',text='D.O.B(irth)')
        self.employee_table.heading('doj',text='D.O.J(oining)')
        self.employee_table.heading('idtype',text='ID Type')
        self.employee_table.heading('idproof',text='ID Proof')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('phone',text='Phone')
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('salary',text='Salary')

        self.employee_table['show']='headings'

        self.employee_table.column("dep",width=100)
        self.employee_table.column("name",width=100)
        self.employee_table.column("desig",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("married",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("doj",width=100)
        self.employee_table.column("idtype",width=100)
        self.employee_table.column("idproof",width=100)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("country",width=100)
        self.employee_table.column("salary",width=100)
        
        
        self.employee_table.pack(fill=BOTH,expand=1)

#--------------------Functions------------------#
        
    def add_data(self):
        if self.var_dep.get() == '' or self.var_email.get() == '':
            messagebox.showerror('Error', 'All Fields are required')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Test@123',
                                               database='mydata')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into employee1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                                  (self.var_dep.get(), self.var_name.get(), self.var_designition.get(),
                                   self.var_email.get(), self.var_address.get(), self.var_married.get(),
                                   self.var_dob.get(), self.var_doj.get(), self.var_idproofcomb.get(),
                                   self.var_idproof.get(), self.var_gender.get(), self.var_phone.get(),
                                   self.var_country.get(), self.var_salary.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo('Success', 'Employee has been added!', parent=self.root)
            except Exception as es:
                messagebox.showerror('Error', f'Due To: {str(es)}', parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=Employee(root )
    root.mainloop()