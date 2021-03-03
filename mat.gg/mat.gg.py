from tkinter import*
list_=["J","H","G","S","A","F"]

def list_to_txt(event):
    txt.delete(0.0,END)#
    valik=lbox.curselection()#
    txt.insert(END,lbox.get(valik[0]))#

def list_to_list(event):
    text=txt.get(0.0,END)
    text=text[-2:-1]
    if text=="\n":
        pass
    else:
        list_.append(text)
        print(list_)
        lbox.config(height=len(list_))
        lbox.insert(END,text)
        txt.delete(0.0,END)

win=Tk()

lbox=Listbox(win,width=20,height=len(list_),selectmode=SINGLE)#
for element in list_:#вести в цыкл
    lbox.insert(END,element)#
lbox.pack()#
lbox.bind("<<ListboxSelect>>",list_to_txt)

txt=Text(win,height=1,width=20,wrap=WORD)
txt.pack()
txt.bind("<Return>",list_to_list)
win.mainloop()