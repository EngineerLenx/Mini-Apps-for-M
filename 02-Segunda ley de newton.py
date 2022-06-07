#Antonio Hernández Mía Valentina 4ATM
from tkinter import *
from tkinter import ttk

def Calcular():
    opc = Combobox_decision.get()
    if opc == "Fuerza":
        fuerza()
    if opc == "Masa":
        masa()
    if opc == "Aceleración":
        aceleracion()

root = Tk()
root.title("Calculadora de la segunda ley de Newton")
root.geometry("250x300")
root.resizable(0, 0)

#Entradas
entrada_fuerza = ttk.Entry(root, width= 9)
entrada_fuerza.place(x = 80, y = 100)
entrada_masa = ttk.Entry(root, width= 9)
entrada_masa.place(x = 80, y = 150)
entrada_aceleracion = ttk.Entry(root, width= 9)
entrada_aceleracion.place(x = 80, y = 200)

titulo = Label(root, text = "SEGUNDA LEY DE NEWTON")
titulo.config(font = ("arial bold mt", 12))
titulo.place(x = 20, y = 10)

l_fuerza = Label(root, text = "Fuerza")
l_fuerza.place(x = 22.5, y = 100)
l_masa = Label(root, text = "Masa")
l_masa.place(x = 25, y = 150)
l_aceleracion = Label(root, text = "Aceleracion")
l_aceleracion.place(x = 10, y = 200 )

l_unidadfuerza = Label(root, text = "N")
l_unidadfuerza.place(x = 145, y = 100)
l_unidadmasa = Label(root, text = "Kg")
l_unidadmasa.place(x = 145, y = 150)
l_unidadaceleracion = Label(root, text = "m/s^2")
l_unidadaceleracion.place(x = 145, y = 200)

label_resultado = ttk.Label(root, text = "", width = 10)
label_resultado.place(x = 150, y = 261)

unidad_resultado = ttk.Label(root, text = "", width = 6)
unidad_resultado.place(x = 180, y = 261)

indicador = Label(root, text = "Resultado:")
indicador.place(x = 85, y = 260)

#Combobox
Combobox_decision = ttk.Combobox(root, width= 10, state = "readonly", values = ("Fuerza", "Masa", "Aceleración"))
Combobox_decision.place(x = 75 , y = 45)
Combobox_decision.current(0)

def fuerza():
    masa = entrada_masa.get()
    masa = float(masa)
    aceleracion = entrada_aceleracion.get()
    aceleracion = float(aceleracion)
    fuerza = masa*aceleracion
    label_resultado.config(text = '{:.5}'.format(fuerza))
    unidad_resultado.config(text = "N")
def aceleracion():
    fuerza = entrada_fuerza.get()
    fuerza = float(fuerza)
    masa = entrada_masa.get()
    masa = float(masa)
    aceleracion = fuerza / masa
    label_resultado.config(text = '{:.5}'.format(aceleracion))
    unidad_resultado.config(text = "m/s^2")
def masa():
    fuerza = entrada_fuerza.get()
    fuerza = float(fuerza)
    aceleracion = entrada_aceleracion.get()
    aceleracion = float(aceleracion)
    masa = fuerza / aceleracion
    label_resultado.config(text = '{:.5}'.format(masa))
    unidad_resultado.config(text = "Kg")
def borrar():
    entrada_masa.delete(0, END)
    entrada_masa.insert(0, " ")
    entrada_aceleracion.delete(0, END)
    entrada_aceleracion.insert(0, " ")
    entrada_fuerza.delete(0, END)
    entrada_fuerza.insert(0, " ")
    label_resultado.config(text = "")
    unidad_resultado.config(text = "")

boton_calculo = ttk.Button(root, text = "Calcular", command = Calcular, width=10)
boton_calculo.place(x = 25, y = 230)

boton_borrar = ttk.Button(root, text="Borrar", command = borrar, width = 7)
boton_borrar.place(x = 140, y = 230)

root.mainloop()