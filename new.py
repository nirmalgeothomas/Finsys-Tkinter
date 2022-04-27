
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font as font


account = tk.Tk()
account.title("finsYs")
account.geometry("1000x1000")
account['bg'] = '#2f516a'
wrappen = ttk.LabelFrame(account)
mycanvas = Canvas(wrappen)
mycanvas.pack(side=LEFT, fill="both", expand="yes")
yscrollbar = ttk.Scrollbar(wrappen, orient='vertical', command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill='y')

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>', lambda e: mycanvas.configure(
    scrollregion=mycanvas.bbox('all')))

full_frame = Frame(mycanvas, width=2000, height=1600, bg='#2f516a')
mycanvas.create_window((0, 0), window=full_frame, anchor="nw")


heading_frame = Frame(mycanvas)
mycanvas.create_window((0, 40), window=heading_frame, anchor="nw")
headingfont = font.Font(family='Times New Roman', size=25,)
credit_heading = Label(heading_frame, text="Account", fg='#fff',
                       bg='#243e55', height=2, bd=5, relief="groove", font=headingfont, width=75)
credit_heading.pack(padx=0, pady=0)

# form fields
sub_headingfont = font.Font(family='Times New Roman', size=20,)
form_frame = Frame(mycanvas, width=1200, height=1200, bg='#243e55')
mycanvas.create_window((75, 150), window=form_frame, anchor="nw")

text1 = font.Font(family='Times New Roman', size=13,)


text2 = font.Font(family='Times New Roman', size=18,)


text3 = font.Font(family='Times New Roman', size=18,)


frame1 = tk.LabelFrame(account, borderwidth=0, bg='#243e54')


l2 = tk.Label(form_frame, text='Account Type', bg='#243e54',
              font=('times new roman', 14))
l2.place(relx=0.04, rely=0.05)
acc = ['Cost of Goods Sold', 'Expenses', 'Other Expense']
cm1 = ttk.Combobox(form_frame, values=acc)
cm1.current(0)
cm1.place(relx=0.04, rely=0.15, relwidth=0.4, relheight=0.065)

l3 = tk.Label(form_frame, text='Name', bg='#243e54', font=(
    'times new roman', 14)).place(relx=0.5, rely=0.05)
e3 = tk.Entry(form_frame).place(relx=0.5, rely=0.15,
                                relwidth=0.4, relheight=0.065)

l4 = tk.Label(form_frame, text='Detail Type', bg='#243e54', font=(
    'times new roman', 14)).place(relx=0.04, rely=0.25)
cont = []
cmb = ttk.Combobox(form_frame, values=cont).place(
    relx=0.04, rely=0.35, relwidth=0.4, relheight=0.065)

l5 = tk.Label(form_frame, text='Description', bg='#243e54', font=(
    'times new roman', 14)).place(relx=0.5, rely=0.25)
e5 = tk.Entry(form_frame).place(relx=0.5, rely=0.35,
                                relwidth=0.4, relheight=0.065)

message = '''Use Cash and Cash Equivalents to track cash or assets, that can be converted into cash immediately.For example marketable securities and Treasury bills.'''
text_box = Text(form_frame)
text_box.place(relx=0.04, rely=0.55, relwidth=0.4, relheight=0.2)
text_box.insert('end', message)
text_box.config(state='disabled')
Checkbutton(form_frame, text="Is sub-account ", bg='#243e54',
            font=('times new roman', 12)).place(relx=0.5, rely=0.45)
bal = ['Deferred CGST', 'Deferred GST Input Credit', 'Deferred Krishi Kalyan Cess',
       'Input Credit', 'Deferred Service Tax Input Credit', 'Deferred SGST', 'Deferred VAT Input Credit',
       'GST Refund', 'Inventory Asset', 'Paid Insurance', 'Service Tax Refund', 'TDS Receivable', 'Uncategorised Asset',
       'Accumulated Depreciation', 'Buildings and Improvements', 'Furniture and Equipment', 'Land', 'Leasehold Improvements',
       'CGST Payable', 'CST Payable', 'CST Suspense', 'GST Payable', 'GST Suspense', 'IGST Payable', 'Input CGST', 'Input CGST Tax RCM',
       'Input IGST', 'Input IGST Tax RCM', 'Input Krishi Kalyan Cess', 'Input Krishi Kalyan Cess RCM', 'Input Service Tax',
       'Input Service Tax RCM', 'Input VAT 14%', 'Input VAT 4%', 'Input VAT 5%', 'Krishi Kalyan Cess Payable', 'Krishi Kalyan Cess Suspense',
       'Output CGST', 'Output CGST Tax RCM', 'Output CST 2%', 'Output IGST', 'Output IGST Tax RCM', 'Output Krishi Kalyan Cess',
       'Output Krishi Kalyan Cess DCM', 'Output Service Tax', 'Output Service Tax RCM', 'Output SGST', 'Output SGST Tax RCM',
       'Output VAT 14%', 'Output VAT 4%', 'Output VAT 5%', 'Service Tax Payable', 'Service Tax Suspense', 'SGST Payable', 'Swachh Bharat Cess Payable',
       'TDS Payable', 'VAT Payable', 'VAT Suspense', 'Opening Balance', 'Equity']

cb = ttk.Combobox(form_frame, values=bal).place(
    relx=0.5, rely=0.55, relwidth=0.4, relheight=0.065)
l6 = tk.Label(form_frame, text='Default Tax Code', bg='#243e54',
              font=('times new roman', 14)).place(relx=0.5, rely=0.63)

val = ['18.0% IGST', ' 14.00% ST', '0% IGST', 'Out of Scope', '0% GST', '14.5% ST', '14.0% VAT', '6.0% IGST', '28.0% IGST', '15.0% ST', '28.0% GST', '12.0% GST', '18.0% GST',
       '3.0% GST', '0.2% IGST', '5.0% GST', '6.0% GST', '0.2% GST', 'Exempt IGST', '3.0% IGST', '4.0% VAT', '5.0% IGST', '12.36% ST', '5.0% VAT', 'Exempt GST', '12.0% IGST', '2.0% CST']
e6 = ttk.Combobox(form_frame, values=val).place(
    relx=0.5, rely=0.7, relwidth=0.4, relheight=0.065)


wrappen.pack(fill='both', expand='yes',)
button = tk.Button(form_frame, text="Submit",)
button.place(x=490, y=990, width=100)

account.mainloop()
