from tkinter import *
import tkinter.messagebox as tmsg 
import keyboard
from ReadWriteMemory import ReadWriteMemory
import threading as th
import os

# Import Complete

# base = 0x01400000
# main_hacking_pointer_value = "hw.dll"+00EA1274

try:
	root = Tk()
	root.title('CSGO 1.6 TRAINER BY AADITYA')

	root.geometry('600x300')

	health_value = IntVar()

	rm = ReadWriteMemory()
	game = rm.get_process_by_name('hl.exe')
	game.open()

	#04930000

	base_address =0x04930000+0x00EA1274

	health_pointer = game.get_pointer(base_address, offsets=[0x430, 0x88, 0x90, 0xF0, 0x19F4])

	# 4 Bytes, 1000 Conversion = 1148846080
	# Original 4 Bytes = 1120403456

	def change_value():

		while True:
			value = game.read(health_pointer)
			game.write(health_pointer, 1148846080)

			if keyboard.is_pressed('ctrl+8'):

				game.write(health_pointer, 1120403456)

				lb4.config(fg="white")
				lb43.config(fg='green')

				break

	# th.Thread(target=value_found()).start()

	def empty():
		Label(text="",bg="black").pack()

	# pm = pymem.Pymem('hl.exe')

	lb = Label(text="CSGO VERSION 1.6 TRAINER....",font="comicsansms 14 bold",bg='black',fg='white')
	lb.pack()

	empty()
	empty()

	lb2 = Label(text="Game: CSGO V1.6 HAS BEEN FOUND....",font="comicsansms 12 italic",bg='black',fg='green')
	lb2.pack()

	empty()
	empty()

	lb4 = Label(text=f"To Hack Your Health Press CTRL+9",bg="black",fg='white',font="comicsansms 12 bold")
	lb4.pack()
	lb43 = Label(text=f"To Make Your Health Back To Normal Press CTRL+8",bg="black",fg='white',font="comicsansms 12 bold")
	lb43.pack()


	root.config(bg="black")

	def on_clicked():

		while True:

			if keyboard.is_pressed('ctrl+9'):
				lb4.config(fg="green")
				lb43.config(fg='white')
				t2 = th.Thread(target=change_value)
				t2.start()

	t1 = th.Thread(target=on_clicked)
	t1.start()

	root.mainloop()
except:
	tmsg.showwarning('Sorry','Game CSGO V1.6 Is Not Running....')