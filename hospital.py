from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
  def __init__(self,root):
    self.root=root
    self.root.title('Hospital Management System')
    self.root.geometry("1350x800+0+0")

    self.Nameoftablets=StringVar()
    self.ref=StringVar()
    self.Dose=StringVar()
    self.NumberOfTablets=StringVar()
    self.Lot=StringVar()
    self.IssueDate=StringVar()
    self.ExpDate=StringVar()
    self.DailyDose=StringVar()
    self.SideEffects=StringVar()
    self.FutherInformation=StringVar()
    self.StorageAdvice=StringVar()
    self.DrivingUsingMachine=StringVar()
    self.HowToUseMedication=StringVar()
    self.PatientId=StringVar()
    self.NhsNumber=StringVar()
    self.PatientName=StringVar()
    self.DateOfBirth=StringVar()
    self.PatientAddress=StringVar()

    lbltitle=Label(self.root,bd=20,relief=RIDGE,text='HOSPITAL MANAGEMENT SYSTEM',fg='red',bg='white',font=('times new roman',50,'bold'))
    lbltitle.pack(side=TOP,fill=X)

    #-------------------Data Frame----------------#
    Dataframe=Frame(self.root,bd=10,relief=RIDGE)
    Dataframe.place(x=0,y=130,width=1350,height=350)

    DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                             font=('times new roman',12,'bold'),text='Patient Information')
    DataframeLeft.place(x=0,y=5,width=980,height=350)

    DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                             font=('times new roman',12,'bold'),text='Prescription')
    DataframeRight.place(x=990,y=5,width=330,height=350)

    #--------------------Buttons Frame-----------------------
    Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
    Buttonframe.place(x=0,y=480,width=1350,height=80)

    #--------------------Details Frame-----------------------
    Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
    Detailsframe.place(x=0,y=550,width=1350,height=170)

    #-------------------DataframeLeft-----------------------------
    lblNameTablet=Label(DataframeLeft,text="Names Of Tablet",font=('times new roman',12,'bold'),padx=2,pady=6)
    lblNameTablet.grid(row=0,column=0)

    comNametablet=ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets,font=('arial',12,'bold'),
                               width=30)
    comNametablet['values']=('Nice','Corona Vacacine','Acetaminophen','Addreall','Amlodipine','Ativan')
    comNametablet.grid(row=0,column=1)

    lblref=Label(DataframeLeft,font=('arial',12,'bold'),text='Refrence No:',padx=2)
    lblref.grid(row=1,column=0,sticky=W)
    textref=Entry(DataframeLeft,textvariable=self.ref,font=('arial',13,'bold'),width=35)
    textref.grid(row=1,column=1)

    lblDose=Label(DataframeLeft,font=('arial',12,'bold'),text='Dose:',padx=2,pady=4)
    lblDose.grid(row=2,column=0,sticky=W)
    txtDose=Entry(DataframeLeft,textvariable=self.Dose,font=('arial',13,'bold'),width=35)
    txtDose.grid(row=2,column=1)

    lblNoOftablets=Label(DataframeLeft,font=('arial',12,'bold'),text='No Of tablets:',padx=2,pady=6)
    lblNoOftablets.grid(row=3,column=0,sticky=W)
    txtNoOftablets=Entry(DataframeLeft,textvariable=self.NumberOfTablets,font=('arial',13,'bold'),width=35)
    txtNoOftablets.grid(row=3,column=1)

    lblLot=Label(DataframeLeft,font=('arial',12,'bold'),text='Lot:',padx=2,pady=6)
    lblLot.grid(row=4,column=0,sticky=W)
    txtLot=Entry(DataframeLeft,textvariable=self.Lot,font=('arial',13,'bold'),width=35)
    txtLot.grid(row=4,column=1)

    lblissueDate=Label(DataframeLeft,font=('arial',12,'bold'),text='Issue Date:',padx=2,pady=6)
    lblissueDate.grid(row=5,column=0,sticky=W)
    txtissueDate=Entry(DataframeLeft,textvariable=self.IssueDate,font=('arial',13,'bold'),width=35)
    txtissueDate.grid(row=5,column=1)

    lblExpDate=Label(DataframeLeft,font=('arial',12,'bold'),text='Exp Dte:',padx=2,pady=6)
    lblExpDate.grid(row=6,column=0,sticky=W)
    txtExpDate=Entry(DataframeLeft,textvariable=self.ExpDate,font=('arial',13,'bold'),width=35)
    txtExpDate.grid(row=6,column=1)

    lblDailyDose=Label(DataframeLeft,font=('arial',12,'bold'),text='Daily Dose:',padx=2,pady=4)
    lblDailyDose.grid(row=7,column=0,sticky=W)
    txtDailyDose=Entry(DataframeLeft,textvariable=self.DailyDose,font=('arial',13,'bold'),width=35)
    txtDailyDose.grid(row=7,column=1)

    lblSideEffect=Label(DataframeLeft,font=('arial',12,'bold'),text='Side Effect:',padx=2,pady=6)
    lblSideEffect.grid(row=8,column=0,sticky=W)
    txtSideEffect=Entry(DataframeLeft,textvariable=self.SideEffects,font=('arial',13,'bold'),width=35)
    txtSideEffect.grid(row=8,column=1)

    lblFurtherinfo=Label(DataframeLeft,font=('arial',12,'bold'),text='Further Information:',padx=2)
    lblFurtherinfo.grid(row=0,column=2,sticky=W)
    txtFurtherinfo=Entry(DataframeLeft,textvariable=self.FutherInformation,font=('arial',12,'bold'),width=35)
    txtFurtherinfo.grid(row=0,column=3)

    lblBloodPressure=Label(DataframeLeft,font=('arial',12,'bold'),text='Blood Pressure:',padx=2,pady=6)
    lblBloodPressure.grid(row=1,column=2,sticky=W)
    txtBloodPressure=Entry(DataframeLeft,textvariable=self.DrivingUsingMachine,font=('arial',12,'bold'),width=35)
    txtBloodPressure.grid(row=1,column=3)

    lblStorage=Label(DataframeLeft,font=('arial',12,'bold'),text='Storage Advice:',padx=2,pady=6)
    lblStorage.grid(row=2,column=2,sticky=W)
    txtStorage=Entry(DataframeLeft,textvariable=self.StorageAdvice,font=('arial',12,'bold'),width=35)
    txtStorage.grid(row=2,column=3)

    lblMedicine=Label(DataframeLeft,font=('arial',12,'bold'),text='Medication:',padx=2,pady=6)
    lblMedicine.grid(row=3,column=2,sticky=W)
    txtMedicine=Entry(DataframeLeft,textvariable=self.HowToUseMedication,font=('arial',12,'bold'),width=35)
    txtMedicine.grid(row=3,column=3)

    lblPatientId=Label(DataframeLeft,font=('arial',12,'bold'),text='Patient Id:',padx=2,pady=6)
    lblPatientId.grid(row=4,column=2,sticky=W)
    txtPatientId=Entry(DataframeLeft,textvariable=self.PatientId,font=('arial',12,'bold'),width=35)
    txtPatientId.grid(row=4,column=3)

    lblNhsNumber=Label(DataframeLeft,font=('arial',12,'bold'),text='NHS Number:',padx=2,pady=6)
    lblNhsNumber.grid(row=5,column=2,sticky=W)
    txtNhsNumber=Entry(DataframeLeft,textvariable=self.NhsNumber,font=('arial',12,'bold'),width=35)
    txtNhsNumber.grid(row=5,column=3)

    lblPatientName=Label(DataframeLeft,font=('arial',12,'bold'),text='Patient Name:',padx=2,pady=6)
    lblPatientName.grid(row=6,column=2,sticky=W)
    txtPatientName=Entry(DataframeLeft,textvariable=self.PatientName,font=('arial',12,'bold'),width=35)
    txtPatientName.grid(row=6,column=3)

    lblDateOfBirth=Label(DataframeLeft,font=('arial',12,'bold'),text='Date Of Birth:',padx=2,pady=6)
    lblDateOfBirth.grid(row=7,column=2,sticky=W)
    txtDateOfBirth=Entry(DataframeLeft,textvariable=self.DateOfBirth,font=('arial',12,'bold'),width=35)
    txtDateOfBirth.grid(row=7,column=3)

    lblPatientAddress=Label(DataframeLeft,font=('arial',12,'bold'),text='Patient Address:',padx=2,pady=6)
    lblPatientAddress.grid(row=8,column=2,sticky=W)
    txtPatientAddress=Entry(DataframeLeft,textvariable=self.PatientAddress,font=('arial',12,'bold'),width=35)
    txtPatientAddress.grid(row=8,column=3)

    #--------------------------DataframeRight----------------------------
    self.txtPrescription=Text(DataframeRight,font=('arial',12,'bold'),width=30,height=16,padx=2,pady=6)
    self.txtPrescription.grid(row=0,column=0)

    #-------------------------------Buttons------------------------------------------
    btnPrescription=Button(Buttonframe,text="Prescription",bg='green',fg='white',font=('arial',12,'bold'),width=21,padx=2,pady=6,command=self.iPrescription)
    btnPrescription.grid(row=0,column=0)

    btnPrescriptionData=Button(Buttonframe,text="Prescription Data",bg='green',fg='white',font=('arial',12,'bold'),width=21,padx=2,pady=6,command=self.iPrescriptionData)
    btnPrescriptionData.grid(row=0,column=1)

    btnUpdate=Button(Buttonframe,text="Update",bg='green',fg='white',font=('arial',12,'bold'),width=21,padx=2,pady=6,command=self.update_data)
    btnUpdate.grid(row=0,column=2)

    btnDelete=Button(Buttonframe,text="Delete",bg='green',fg='white',font=('arial',12,'bold'),width=21,padx=2,pady=6,command=self.idelete)
    btnDelete.grid(row=0,column=3)
    
    btnClear=Button(Buttonframe,text="Clear",bg='green',fg='white',font=('arial',12,'bold'),width=21,padx=2,pady=6,command=self.clear)
    btnClear.grid(row=0,column=4)

    btnExit=Button(Buttonframe,text="Exit",bg='green',fg='white',font=('arial',12,'bold'),width=21,padx=2,pady=6,command=self.iExit)
    btnExit.grid(row=0,column=5)

    #----------------------------------------Table----------------------------------
    #---------------------------------ScrollBar------------------
    scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
    self.hospital_table=ttk.Treeview(Detailsframe,columns=('nameoftablets','ref','dose','nooftablets','lot','issuedate','expdate','dailydose','storage','nhsnumber','pname','dob','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
    scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

    self.hospital_table.heading('nameoftablets',text='Name Of Tablets')
    self.hospital_table.heading('ref',text='Reference No.')
    self.hospital_table.heading('dose',text='Dose')
    self.hospital_table.heading('nooftablets',text='No Of Tablets')
    self.hospital_table.heading('lot',text='Lot')
    self.hospital_table.heading('issuedate',text='Issue Date')
    self.hospital_table.heading('expdate',text='Exp Date')
    self.hospital_table.heading('dailydose',text='Daily Dose')
    self.hospital_table.heading('storage',text='Storage')
    self.hospital_table.heading('nhsnumber',text='NHS Number')
    self.hospital_table.heading('pname',text='Patient Name')
    self.hospital_table.heading('dob',text='DOB')
    self.hospital_table.heading('address',text='Address')

    self.hospital_table['show']='headings'

    self.hospital_table.pack(fill=BOTH,expand=1)

    self.hospital_table.column('nameoftablets',width=100)
    self.hospital_table.column('ref',width=100)
    self.hospital_table.column('dose',width=100)
    self.hospital_table.column('nooftablets',width=100)
    self.hospital_table.column('lot',width=100)
    self.hospital_table.column('issuedate',width=100)
    self.hospital_table.column('expdate',width=100)
    self.hospital_table.column('dailydose',width=100)
    self.hospital_table.column('storage',width=100)
    self.hospital_table.column('nhsnumber',width=100)
    self.hospital_table.column('pname',width=100)
    self.hospital_table.column('dob',width=100)
    self.hospital_table.column('address',width=100)

    self.hospital_table.pack(fill=BOTH,expand=1)
    self.hospital_table.bind('<ButtonRelease-1>',self.get_cursor)
    self.fetch_data()


    #----------------------------------Functionality Declaration--------------------------------
  def iPrescriptionData(self):
    if self.Nameoftablets.get() == "" or self.ref.get() == "":
        messagebox.showerror("Error", "All fields are required")
    else:
        try:
            conn = mysql.connector.connect(
                host='localhost',
                username='root',
                password='your_mysql_password_here',  # Ensure password is correct
                database='aidata'
            )
            my_cursor = conn.cursor()
            
            sql_query = '''INSERT INTO hospitalm
                (nameoftablets, ref, dose, nooftablets, lot, issuedate, expdate, 
                 dailydose, storage, nhsnumber, pname, dob, address) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            
            values = (
                self.Nameoftablets.get(),
                self.ref.get(),
                self.Dose.get(),
                self.NumberOfTablets.get(),
                self.Lot.get(),
                self.IssueDate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.StorageAdvice.get(),
                self.NhsNumber.get(),
                self.PatientName.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get()
            )

            my_cursor.execute(sql_query, values)
            conn.commit()
            self.fetch_data()
            conn.close()

            messagebox.showinfo("Success", "Data inserted successfully!")

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
            print("Error:", e)

  def update_data(self):
    try:
        # Establish connection
        conn = mysql.connector.connect(
            host='localhost',
            username='root',
            password='your_mysql_password_here',  # Ensure password is correct
            database='aidata'
        )
        my_cursor = conn.cursor()

        # Corrected SQL Query
        sql = '''UPDATE hospitalm 
                 SET nameoftablets=%s, dose=%s, nooftablets=%s, lot=%s, 
                     issuedate=%s, expdate=%s, dailydose=%s, storage=%s, 
                     nhsnumber=%s, pname=%s, dob=%s, address=%s
                 WHERE ref=%s'''  # Using 'ref' as the unique identifier

        # Ensure correct data mapping
        values = (
            self.Nameoftablets.get(),
            self.Dose.get(),
            self.NumberOfTablets.get(),
            self.Lot.get(),
            self.IssueDate.get(),
            self.ExpDate.get(),
            self.DailyDose.get(),
            self.StorageAdvice.get(),
            self.NhsNumber.get(),
            self.PatientName.get(),
            self.DateOfBirth.get(),
            self.PatientAddress.get(),
            self.ref.get()  # 'ref' should be at the end for the WHERE clause
        )

        # Execute the query
        my_cursor.execute(sql, values)
        self.fetch_data()
        conn.commit()
        messagebox.showinfo("Success", "Record updated successfully!")

    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Database error: {e}")

    finally:
        # Close connection
        conn.close()
      

  def fetch_data(self):
            conn = mysql.connector.connect(
                host='localhost',
                username='root',
                password='your_mysql_password_here',  
                database='aidata'
            )
            my_cursor = conn.cursor()
            my_cursor.execute('select * from hospitalm')
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.hospital_table.delete(*self.hospital_table.get_children())
                for i in rows:
                    self.hospital_table.insert("",END,values=i)
                conn.commit()
            conn.close()

  def get_cursor(self,event):
      cursor_row=self.hospital_table.focus()
      content=self.hospital_table.item(cursor_row)
      row=content['values']
      if not row:  
        print("No data selected.")
        return
      self.Nameoftablets.set(row[0])
      self.ref.set(row[1])
      self.Dose.set(row[2])
      self.NumberOfTablets.set(row[3])
      self.Lot.set(row[4])
      self.IssueDate.set(row[5])
      self.ExpDate.set(row[6])
      self.DailyDose.set(row[7])
      self.StorageAdvice.set(row[8])
      self.NhsNumber.set(row[9])
      self.PatientName.set(row[10])
      self.DateOfBirth.set(row[11])
      self.PatientAddress.set(row[12])

  def iPrescription(self):
      self.txtPrescription.insert(END,'Name Of Tablets:\t\t'+self.Nameoftablets.get()+'\n')
      self.txtPrescription.insert(END,'Refernce No:\t\t'+self.ref.get()+'\n')
      self.txtPrescription.insert(END,'Dose:\t\t'+self.Dose.get()+'\n')
      self.txtPrescription.insert(END,'Number Of Tablets:\t\t'+self.NumberOfTablets.get()+'\n')
      self.txtPrescription.insert(END,'Lot:\t\t'+self.Lot.get()+'\n')
      self.txtPrescription.insert(END,'Issue Date:\t\t'+self.IssueDate.get()+'\n')
      self.txtPrescription.insert(END,'Exp Date:\t\t'+self.ExpDate.get()+'\n')
      self.txtPrescription.insert(END,'Daily Dose:\t\t'+self.DailyDose.get()+'\n')
      self.txtPrescription.insert(END,'Side Effects:\t\t'+self.SideEffects.get()+'\n')
      self.txtPrescription.insert(END,'Further Inforamtion:\t\t'+self.FutherInformation.get()+'\n')
      self.txtPrescription.insert(END,'Storage Advice:\t\t'+self.StorageAdvice.get()+'\n')
      self.txtPrescription.insert(END,'DrivingUsingMachine:\t\t'+self.DrivingUsingMachine.get()+'\n')
      self.txtPrescription.insert(END,'Patient Id:\t\t'+self.PatientId.get()+'\n')
      self.txtPrescription.insert(END,'NHSNumber:\t\t'+self.NhsNumber.get()+'\n')
      self.txtPrescription.insert(END,'Patient Name:\t\t'+self.PatientName.get()+'\n')
      self.txtPrescription.insert(END,'Date Of Birth:\t\t'+self.DateOfBirth.get()+'\n')
      self.txtPrescription.insert(END,'Patient Address:\t\t'+self.PatientAddress.get()+'\n')

  def idelete(self):
      conn = mysql.connector.connect(
                host='localhost',
                username='root',
                password='your_mysql_password_here',  # Ensure password is correct
                database='aidata'
            )
      my_cursor = conn.cursor()
      query="delete from hospitalm where ref=%s "
      value=(self.ref.get(),)
      my_cursor.execute(query,value)

      conn.commit()
      self.fetch_data()
      conn.close()
      messagebox.showinfo('Deleted','Patient information has been deleted successfully')
  
  def clear(self):
      self.Nameoftablets.set('')
      self.ref.set('')
      self.Dose.set('')
      self.NumberOfTablets.set('')
      self.Lot.set('')
      self.IssueDate.set('')
      self.ExpDate.set('')
      self.DailyDose.set('')
      self.SideEffects.set('')
      self.FutherInformation.set('')
      self.StorageAdvice.set('')
      self.DrivingUsingMachine.set('')
      self.HowToUseMedication.set('')
      self.PatientId.set('')
      self.NhsNumber.set('')
      self.PatientName.set('')
      self.DateOfBirth.set('')
      self.PatientAddress.set('')
      self.txtPrescription.delete('1.0',END)

  def iExit(self):
      iExit=messagebox.askyesno('Hospital Management System','Cofirm you want to exit')
      if iExit>0:
          root.destroy()
          return



     
            







                             


root=Tk()
ob=Hospital(root)
root.mainloop()
