
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font as font


reconcile_form = tk.Tk()
reconcile_form.title("finsYs")
reconcile_form.geometry("1000x1000")
reconcile_form['bg'] = '#2f516a'
wrappen = ttk.LabelFrame(reconcile_form)
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
credit_heading = Label(heading_frame, text="RECONCILED", fg='#fff',
                       bg='#243e55', height=2, bd=5, relief="groove", font=headingfont, width=75)
credit_heading.pack(padx=0, pady=0)

# form fields
sub_headingfont = font.Font(family='Times New Roman', size=20,)
form_frame = Frame(mycanvas, width=1600, height=800, bg='#243e55')
mycanvas.create_window((0, 150), window=form_frame, anchor="nw")

text1 = font.Font(family='Times New Roman', size=13,)
text1 = Label(form_frame, text="Open your statement and we'll get started.",
              bg='#243e55', fg='#fff', font=text1)
text1.place(x=520, y=0,)

text2 = font.Font(family='Times New Roman', size=18,)
text2 = Label(form_frame,
              text="Which account do you want to reconcile?", bg='#243e55', font=text2, fg='#fff')
text2.place(x=260, y=80,)


title_lab = tk.Label(form_frame, text="Account",
                     bg='#243e55', fg='#fff', font=text1)
place_input = StringVar()
drop2 = ttk.Combobox(form_frame, textvariable=place_input)

drop2['values'] = ("PAYEE1 PAYEE2 PAYEE3 PAYEE4")

title_lab.place(x=240, y=130, height=15, width=100)
drop2.place(x=260, y=160, height=40, width=450)
wrappen.pack(fill='both', expand='yes',)


text3 = font.Font(family='Times New Roman', size=18,)
text3 = Label(form_frame,
              text="Add the following information", bg='#243e55', font=text3, fg='#fff')
text3.place(x=260, y=240,)


begining_date = Label(form_frame, text="Begining Balance",
                      bg='#243e55', fg='#fff', font=text1)
begining_date.place(x=260, y=280,)
begining_date_input = Entry(form_frame, width=25, bg='#243e55', fg='#fff')
begining_date_input.place(x=260, y=310, height=40)

ending_balance = Label(form_frame, text="Ending Balance",
                       bg='#243e55', fg='#fff', font=text1)
ending_balance.place(x=450, y=280,)
ending_balance_input = Entry(form_frame, width=25, bg='#243e55', fg='#fff')
ending_balance_input.place(x=450, y=310, height=40)

ending_date = Label(form_frame, text="Ending Date",
                    bg='#243e55', fg='#fff', font=text1)
ending_date.place(x=635, y=280,)
ending_date_input = Entry(form_frame, width=25, bg='#243e55', fg='#fff')
ending_date_input.place(x=635, y=310, height=40)


text4 = font.Font(family='Times New Roman', size=18,)
text4 = Label(form_frame,
              text="Enter the service charge or interest earned, if necessary", bg='#243e55', font=text4, fg='#fff')
text4.place(x=260, y=370,)


date = Label(form_frame, text="Date",
             bg='#243e55', fg='#fff', font=text1)
date.place(x=260, y=420,)
date_input = Entry(form_frame, width=25, bg='#243e55', fg='#fff')
date_input.place(x=260, y=450, height=40)

service_charge = Label(form_frame, text="Service Charge",
                       bg='#243e55', fg='#fff', font=text1)
service_charge.place(x=450, y=420,)
service_charge_input = Entry(form_frame, width=25, bg='#243e55', fg='#fff')
service_charge_input.place(x=450, y=450, height=40)

expense_account = Label(form_frame, text="Expense Account",
                        bg='#243e55', fg='#fff', font=text1)
expense_account.place(x=635, y=420,)
expense_account_input = Entry(form_frame, width=25, bg='#243e55', fg='#fff')
expense_account_input.place(x=635, y=450, height=40)


date1 = Label(form_frame, text="Date",
              bg='#243e55', fg='#fff', font=text1)
date1.place(x=260, y=515,)
date1_input = Entry(form_frame, width=25, bg='#243e55', fg='#fff')
date1_input.place(x=260, y=545, height=40)

interest_earned = Label(form_frame, text="Interest Earned",
                        bg='#243e55', fg='#fff', font=text1)
interest_earned.place(x=450, y=515,)
interest_earned_input = Entry(form_frame, width=25, bg='#243e55', fg='#fff')
interest_earned_input.place(x=450, y=545, height=40)

income_account = Label(form_frame, text="Income Account",
                       bg='#243e55', fg='#fff', font=text1)
income_account.place(x=635, y=515,)
income_account_input = Entry(form_frame, width=25, bg='#243e55', fg='#fff')
income_account_input.place(x=635, y=545, height=40)


button = tk.Button(form_frame, text="Start Reconciling",)
button.place(x=490, y=620, width=100)

reconcile_form.mainloop()
