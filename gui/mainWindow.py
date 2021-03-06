import tkinter
from domain.Processor import Processor
from tkinter import *
from tkinter import scrolledtext, messagebox


class MainWindow:

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry("400x600")
        self.window.title(string="Solucionari")
        self.window.minsize(width=500,height=600)
        self.frame = Frame(self.window)
        self.camp_label = Label(self.frame,text="Introdueix les lletres (primer l'obligatòria):")
        self.camp_label.grid(row=0, column=0)
        self.camp_lletres = Entry(self.frame, width=20)
        self.camp_lletres.grid(row=0, column=1)
        self.genera_boto = Button(self.frame, text="Genera", command=self.onclick)
        self.genera_boto.grid(row=0, column=2)
        self.sol_label = Label(self.frame, text="Paraules del dia:")
        self.sol_label.grid(row=1, column=0)
        self.text = scrolledtext.ScrolledText(self.frame, width=50, height=30)
        self.text.grid(row=2, column=0, columnspan=2)
        self.frame.pack(fill=tkinter.BOTH, side=tkinter.LEFT)

    def onclick(self):
        self.text.delete('1.0',END)
        letters = self.camp_lletres.get()
        if len(letters) != 7:
            messagebox.showerror("Error","No hi ha prou lletres")
            return
        p = Processor()
        sol, tutis = p.generate_solution(letters)
        label = Label(self.frame,text="Paraules: "+str(len(sol)+len(tutis)))
        label.grid(row=3, column=1)
        self.text.insert(tkinter.INSERT, chars="Tutis:\n")
        for word in tutis:
            self.text.insert(tkinter.INSERT, chars=word)
        self.text.insert(tkinter.INSERT, chars="Resta:\n")
        for word in sol:
            self.text.insert(tkinter.INSERT, chars=word)


