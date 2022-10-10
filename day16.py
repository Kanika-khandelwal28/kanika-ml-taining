
import tkinter as ttk
app=ttk.Tk()
app.title('reccomendation system')
app.geometry('400x600')

result=ttk.Variable(app)
box=ttk.Listbox(app,height=10)
box.place(x=10,y=50)

def get_movie():
    pass

ttk.Button(app,text='find reccomendation'