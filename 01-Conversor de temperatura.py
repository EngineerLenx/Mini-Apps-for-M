#Antonio Hernández Mía Valentina 4ATM
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Conversor de temperatura")
root.geometry("200x250")
root.resizable(0, 0)
#Entrada de grados
entrada_grados = ttk.Entry(root, width= 10)
entrada_grados.place(x = 69, y = 60)

titulo = Label(root, text = "CONVERSOR DE TEMPERATURA")
titulo.place(x = 15, y = 0)

temperaturaEnt = StringVar()
combobox_entrada = ttk.Combobox(root, width= 10, state = "readonly", textvariable= temperaturaEnt, 
values = ("Fahrenheit", "Celsius", "Kelvin"))
combobox_entrada.place(x = 60 , y = 30)
combobox_entrada.current(0)

#Combobox de salida de la conversión
temperaturaSali = StringVar()
combobox_salida = ttk.Combobox(root, width= 10, state = "readonly", textvariable = temperaturaSali, 
values = ("Celsius", "Fahrenheit", "Kelvin"))
combobox_salida.place(x = 60, y = 170)
combobox_salida.current(0)

def convertir():
    temperatura_intr = temperaturaEnt.get()
    temperatura_out = temperaturaSali.get()
    grades = float(entrada_grados.get())
    if temperatura_intr == temperatura_out:
        salida_temperatura = grades
    elif temperatura_intr == "Fahrenheit" and temperatura_out == "Celsius":
        salida_temperatura = (grades -32) * 5.0/9.0
    elif temperatura_intr == "Celsius" and temperatura_out == "Fahrenheit":
        salida_temperatura = (9.0/5.0 * grades +32)
    elif temperatura_intr == "Celsius" and temperatura_out == "Kelvin":
        salida_temperatura = (grades + 273.15)
    elif temperatura_intr == "Kelvin" and temperatura_out == "Celsius":
        salida_temperatura = (grades - 273.15)
    salida_conversion.config(text = '{:.5}'.format(salida_temperatura))

def boton_borrar():
    entrada_grados.delete(0, END)
    entrada_grados.insert(0, "")
    salida_conversion.config(text = "")

boton_conversion= ttk.Button(root, text = "⬇", command = convertir, width=10)
boton_conversion.place(x = 67, y = 120)

salida_conversion = Label(root, text = "", width = 7, bg = "light gray")
salida_conversion.place(x = 75, y = 200)

bott_borrar = ttk.Button(root, text="Borrar", command = boton_borrar, width = 7)
bott_borrar.place(x = 340, y = 70)

root.mainloop()