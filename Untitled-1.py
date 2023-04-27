from tkinter import*

import random
top = Tk()
top.geometry("300x150")
top.title("Password Generator")
top.resizable(0,0)

top.columnconfigure(0,weight=1)
top.columnconfigure(1,weight=1)
top.columnconfigure(2,weight=1)
top.rowconfigure(0,weight=1)
top.rowconfigure(1,weight=1)
top.rowconfigure(2,weight=1)

label = Label(top, text ="Kata Sandi:")
entri = Entry(top)

def HasilkanPass():
    kecil ="abcdefghijklmnopqrstuvwxyz"
    besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    angka = "0123456789"
    simbol ="(){}[],.-/_*#%@!$<>"

    semua = kecil+besar+angka+simbol
    panjang = 11
    password = "".join(random.sample(semua, panjang))
    entri.insert(0,password)

    
tombol = Button (top, text ="Hasilkan Password")
tombol.bind('<Button-1>',HasilkanPass())
tombol.pack()
tombol.grid(row=2,column=1,padx=10,pady=20)
label.grid(row=0,column=0,padx=10,pady=5)
entri.grid(row=0,column=1,sticky=W,padx=5,pady=10)

top.mainloop()