from logging import root
import time
import tkinter.scrolledtext
from tkinter.font import Font
from datetime import datetime
import subprocess
import os
from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter import scrolledtext


currTime = datetime.now()
year = str((currTime.year))
month = str((currTime.month))
day = str((currTime.day))

def speichern():
      newpath = "C:/ProgramData/Tagebucheintraege"
      if not os.path.exists(newpath):
       os.makedirs(newpath)
      lbenter = etEingabe.get(1.0, END)
      path= "C:/ProgramData/Tagebucheintraege"
      f = ("/"+day+"-"+month+ "-" + year)
      g= ".txt"
      h= path+f+g
      with open(h,'a+') as w:
         w.write(lbenter)
      w.close
      etEingabe.delete(1.0, tkinter.END)
      etEingabe.insert(1.0,"Eintrag gespeichert!")

      
def oeffnen():
   path = r"C:/ProgramData/Tagebucheintraege"
   path = os.path.realpath(path)
   os.startfile(path)

fenster = tkinter.Tk()
fenster.title("Tagebuch")
fenster.resizable(False, False)
fenster.columnconfigure(0, weight=1)
fenster.rowconfigure(0, weight=1)
img = PhotoImage(file="diary.png")
canvas = Canvas(fenster, width = 120, height = 50)   
canvas.create_image(500,400,image=img)
canvas.grid(column=0,padx=0,pady=0,sticky='nsew')  

canvas.columnconfigure(0, weight=1)
canvas.rowconfigure(0, weight=1)




etEingabe = tkinter.Text(fenster,  width =100, height =35, bg="light blue")
etEingabe.grid(row=0,column=0,padx=50,pady=0,sticky='news')
etEingabe.configure(font=(14))
etEingabe.insert(1.9,(day+"."+month+ "." + year +"\n \n"))

etEingabe.insert(3.0,"Liebes Tagebuch, \n \n ")




buSpeichern = tkinter.Button(fenster, text="Speichern", command=speichern, width=20, bg="light blue")
buSpeichern.grid(row=2, column=0, padx=100, pady=10)


buOpen = tkinter.Button(fenster, text="Tagebucheinträge", command=oeffnen, width=20, bg="light blue")
buOpen.grid(row=2, column=0, padx=170, pady=10, sticky="w")
fenster.mainloop()
