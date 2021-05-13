from tkinter import *


class Persona:
    nombre = ""
    edad = ''
    apellido = ''

    def setName(name):
        Persona.nombre = name

    def setApellido(lastName):
        Persona.apellido = lastName


window = Tk()


def setApellido():
    lastName = txt.get()
    Persona.setApellido(lastName)
    lbl.configure(text="Bienvenido! " + Persona.nombre +
                  " " + Persona.apellido)


def setName():
    name = txt.get()
    Persona.setName(name)
    lbl.configure(text="Su nombre es " + Persona.nombre +
                  ' ,ahora introduzca su apellido')
    btn.configure(text='Hazme click para continuar', command=setApellido)


if (Persona.nombre == ''):
    lbl = Label(window, text='Hola muy buenas!, introduzca su nombre',
                font=('Arial Bond', 20))
    txt = Entry(window, width=30)
    txt.grid(row=0, column=1)
    lbl.grid(row=0, column=0)
    btn = Button(text="Hazme click al terminar", command=setName)

    btn.grid(row=1, column=0)
elif (Persona.nombre != ''):
    text = Label(window, text='Bienvenido ' + Persona.nombre)
    text.grid(row=1, column=1)

window.geometry('900x500')
window.title("Bienvenido a mi aplicacion")


window.mainloop()
