
from tkinter import *

root = Tk()

layar = Entry(root, width=27, borderwidth=5)
layar.grid(column=0, row=0, columnspan=3)

def tambahAngka(angka):
	angkaPer = layar.get()
	layar.delete(0, END)
	layar.insert(0, str(angkaPer) + str(angka))

def samaDengan():
	angka_kedua = layar.get()
	layar.delete(0, END)

	if math == "tambah":
		layar.insert(0, angkaFirst + int(angka_kedua))

def tambah():
	angka_pertama = layar.get()
	layar.delete(0, END)
	global angkaFirst
	global math
	angkaFirst = int(angka_pertama)
	math = "tambah"


angka1 = Button(root, text=1, padx=40, pady=20, command=lambda: tambahAngka(1))
angka2 = Button(root, text=2, padx=40, pady=20, command=lambda: tambahAngka(2))
angka3 = Button(root, text=3, padx=40, pady=20, command=lambda: tambahAngka(3))
angka4 = Button(root, text=4, padx=40, pady=20, command=lambda: tambahAngka(4))
angka5 = Button(root, text=5, padx=40, pady=20, command=lambda: tambahAngka(5))
angka6 = Button(root, text=6, padx=40, pady=20, command=lambda: tambahAngka(6))
angka7 = Button(root, text=7, padx=40, pady=20, command=lambda: tambahAngka(7))
angka8 = Button(root, text=8, padx=40, pady=20, command=lambda: tambahAngka(8))
angka9 = Button(root, text=9, padx=40, pady=20, command=lambda: tambahAngka(9))
angka0 = Button(root, text=0, padx=40, pady=20, command=lambda: tambahAngka(0))

tambah = Button(root, text="+", padx=40, pady=20, command=tambah)
samaDengan = Button(root, text="=", padx=40, pady=20, command=samaDengan)


angka1.grid(column=0, row=1)
angka2.grid(column=1, row=1)
angka3.grid(column=2, row=1)

angka4.grid(column=0, row=2)
angka5.grid(column=1, row=2)
angka6.grid(column=2, row=2)

angka7.grid(column=0, row=3)
angka8.grid(column=1, row=3)
angka9.grid(column=2, row=3)

angka0.grid(column=1, row=4)

tambah.grid(column=0, row=4)
samaDengan.grid(column=2, row=4)




root.mainloop()







