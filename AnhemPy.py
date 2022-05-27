import tkinter.messagebox
from tkinter import *


def on_click():
    atividade1 = entrada1.get()
    if entrada1.get().isalpha():
        tkinter.messagebox.showinfo('Erro', 'Informe apenas números!')
    else:
        atividade1 = float(entrada1.get())
    atividade2 = entrada2.get()
    if entrada2.get().isalpha():
        tkinter.messagebox.showinfo('Erro', 'Informe apenas números!')
    else:
        atividade2 = float(entrada2.get())
    atividade3 = entrada3.get()
    if entrada3.get().isalpha():
        tkinter.messagebox.showinfo('Erro', 'Informe apenas números!')
    else:
        atividade3 = float(entrada3.get())
    atividade4 = entrada4.get()
    if entrada4.get().isalpha():
        tkinter.messagebox.showinfo('Erro', 'Informe apenas números!')
    else:
        atividade4 = float(entrada4.get())
    avaliacao1 = entrada5.get()
    if entrada5.get().isalpha():
        tkinter.messagebox.showinfo('Erro', 'Informe apenas números!')
    else:
        avaliacao1 = float(entrada5.get())
    avaliacao2 = entrada6.get()
    if entrada6.get().isalpha():
        tkinter.messagebox.showinfo('Erro', 'Informe apenas números!')
    else:
        avaliacao2 = float(entrada6.get())
    avaliacao3 = entrada7.get()
    if entrada7.get().isalpha():
        tkinter.messagebox.showinfo('Erro', 'Informe apenas números!')
    else:
        avaliacao3 = float(entrada7.get())
    avaliacao4 = entrada8.get()
    if entrada8.get().isalpha():
        tkinter.messagebox.showinfo('Erro', 'Informe apenas números!')
    else:
        avaliacao4 = float(entrada8.get())
    atividades = float((atividade1 + atividade2 + atividade3 + atividade4) / 10)
    avaliacoes = float((avaliacao1 + avaliacao2 + avaliacao3 + avaliacao4) / 6)
    n1['text'] = f'Média N1: {atividades:.1f}'
    n2['text'] = f'Média N2: {avaliacoes:.1f}'
    total = float(atividades + avaliacoes)
    if total >= 6.0:
        resultado['text'] = f'Nota final: {total:.1f}\nAprovado!'
    else:
        resultado['text'] = f'Nota final: {total:.1f}\nReprovado!'


root = Tk()
root.title('AnhemPy')
root.geometry('400x240+950+400')
root.configure(background='#20B2AA')

titulo1 = Label(root, text='Notas N1')
titulo1.configure(background='red', font=('Arial Black', 12))
titulo1.place(x=0, y=0)

label1 = Label(root, text='Atividade 1')
label1.configure(background='white', font=('Arial Black', 8))
label1.place(x=0, y=40)

entrada1 = Entry(root)
entrada1.configure(width=5)
entrada1.place(x=80, y=40)

label2 = Label(root, text='Atividade 2')
label2.configure(background='white', font=('Arial Black', 8))
label2.place(x=0, y=80)

entrada2 = Entry(root)
entrada2.configure(width=5)
entrada2.place(x=80, y=80)

label3 = Label(root, text='Atividade 3')
label3.configure(background='white', font=('Arial Black', 8))
label3.place(x=0, y=120)

entrada3 = Entry(root)
entrada3.configure(width=5)
entrada3.place(x=80, y=120)

label4 = Label(root, text='Atividade 4')
label4.configure(background='white', font=('Arial Black', 8))
label4.place(x=0, y=160)

entrada4 = Entry(root)
entrada4.configure(width=5)
entrada4.place(x=80, y=160)

titulo2 = Label(root, text='Notas N2')
titulo2.configure(background='red', font=('Arial Black', 12))
titulo2.place(x=120, y=0)

label5 = Label(root, text='Avaliação 1')
label5.configure(background='white', font=('Arial Black', 8))
label5.place(x=120, y=40)

entrada5 = Entry(root)
entrada5.configure(width=5)
entrada5.place(x=200, y=40)

label6 = Label(root, text='Avaliação 2')
label6.configure(background='white', font=('Arial Black', 8))
label6.place(x=120, y=80)

entrada6 = Entry(root)
entrada6.configure(width=5)
entrada6.place(x=200, y=80)

label7 = Label(root, text='Avaliação 3')
label7.configure(background='white', font=('Arial Black', 8))
label7.place(x=120, y=120)

entrada7 = Entry(root)
entrada7.configure(width=5)
entrada7.place(x=200, y=120)

label8 = Label(root, text='Avaliação 4')
label8.configure(background='white', font=('Arial Black', 8))
label8.place(x=120, y=160)

entrada8 = Entry(root)
entrada8.configure(width=5)
entrada8.place(x=200, y=160)

n1 = Label(root)
n1.configure(background='#20B2AA', font=('Arial Black', 8))
n1.place(x=0, y=190)

n2 = Label(root)
n2.configure(background='#20B2AA', font=('Arial Black', 8))
n2.place(x=122, y=190)

botao = Button(root, text='Calcular', command=on_click)
botao.configure(width=8, height=1, font=('Arial Black', 18))
botao.place(x=240, y=40)

resultado = Label(root)
resultado.configure(background='#20B2AA', font=('Arial Black', 12))
resultado.place(x=250, y=120)

root.resizable(False, False)
root.mainloop()
