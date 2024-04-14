# import required library
from tkinter import *

# First we need to read the contents of two files
with open('file 1.docx') as f1:
    s1=f1.read().lower().split()
    l1=[]
    for i in s1:
        if i.isalnum():
            l1.append(i)
with open('file 2.doc') as f2:
    s2=f2.read().lower().split()
    l2=[]
    for i in s2:
        if i.isalnum():
            l2.append(i)

# Finding how many words are common in two files
plag_words=len(set(l1).intersection(set(l2)))

# Finding total number of words in two files
total_words=len(l1)+len(l2)

# Formula to calculate the plagarism percent
plag_percent=100-round((total_words-plag_words*2)/total_words*100)

# Displaying the result
result="      The Plagarized Content Percent among two files is "+str(plag_percent)+"%"
if plag_percent30 and plag_percent60:
    win= Tk()
    win.geometry('800x200')
    canvas= Canvas(win, width= 700, height= 650, bg='Yellow')
    canvas.create_text(300, 100, text=result, fill='black', font=('Helvetica'))
    canvas.pack()
    win.mainloop()
else:
    win= Tk()
    win.geometry('800x200')
    canvas= Canvas(win, width= 700, height= 650, bg='Red')
    canvas.create_text(300, 100, text=result, fill='black', font=('Helvetica'))
    canvas.pack()
    win.mainloop()
