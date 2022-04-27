import tkinter as tk
from tkinter import *
from tkinter import VERTICAL, ttk
import tkinter.font as font
from tkcalendar import DateEntry, Calendar


def main():

    global A, data
    A = tk.Tk()
    A.title('suppliers')
    A.geometry('1500x1000')
    A['bg'] = '#2f516f'

    # head frame
    head = tk.LabelFrame(A, borderwidth=0, bg='#243e54')
    f = font.Font(family='Times New Roman', size=30)  # font
    lb = tk.Label(head, text='CHART OF ACCOUNTS', bg='#243e54')
    lb['font'] = f
    lb.place(relx=0.3, rely=0.2)
    head.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

    # contents frame
    hd = tk.Frame(A, bg='#243e54')
    hd.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.5)
    ff = font.Font(family='Times New Roman', size=15)  # font
    bt1 = tk.Button(hd, text='Run Report',
                    command="", bg='#243e54')
    bt2 = tk.Button(hd, text='New',
                    command="", bg='#243e54')
    bt3 = tk.Button(hd, text='Import',
                    command="", bg='#243e54')
    bt1['font'] = ff
    bt2['font'] = ff
    bt3['font'] = ff
    bt1.place(relx=0.65, rely=0.05)
    bt2.place(relx=0.75, rely=0.05)
    bt3.place(relx=0.80, rely=0.05)
    text1 = font.Font(family='Times New Roman', size=13,)
    text1 = Label(A, text="Filter by name",
                  bg='#243e55', fg='#fff', font=text1)
    text1.place(x=160, y=170,)

    # table view

    treevv = ttk.Treeview(hd, height=7, columns=(
        1, 2, 3, 4, 5, 6, 7), show='headings')
    treevv.heading(1, text='NAME')  # headings
    treevv.heading(2, text='TYPE')
    treevv.heading(3, text='DETAIL TYPE')
    treevv.heading(4, text='TAX RATE')
    treevv.heading(5, text='FINSYS AMOUNT')
    treevv.heading(6, text='BANK AMOUNT')
    treevv.heading(7, text='ACTION')
    #treevv.heading(7, text='Actions')

    treevv.column(1, minwidth=30, width=140, anchor=CENTER)  # coloumns
    treevv.column(2, minwidth=30, width=140, anchor=CENTER)
    treevv.column(3, minwidth=30, width=140, anchor=CENTER)
    treevv.column(4, minwidth=30, width=140, anchor=CENTER)
    treevv.column(5, minwidth=30, width=140, anchor=CENTER)
    treevv.column(6, minwidth=30, width=140, anchor=CENTER)
    treevv.column(7, minwidth=30, width=140, anchor=CENTER)
    #treevv.column(7, minwidth=30, width=120,anchor=CENTER)
    data = ['Dhyan Kumar', 'Account Receivable(Debtors)', 'Account Receivable(Debtors)',
            '99120.0', '100000', '']
    data1 = ['Dhyan Kumar', 'Current Assets', 'Deferred Service Tax Input Credit',
             '99120.0', '75048.0', '']
    treevv.insert('', 'end', text=data, values=(data))
    treevv.place(relx=0, rely=0.2, relwidth=1, relheight=0.6)

    A.mainloop()


main()
