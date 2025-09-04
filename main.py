import tkinter as tk



ventana = tk.Tk()
ventana.title("CALCULADORA")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text="ingrese num1:")
etiqueta.pack(pady=5)

entrada = tk.Entry(ventana)
entrada.pack(pady=5)

etiqueta = tk.Label(ventana, text="ingrese num2:")
etiqueta.pack(pady=5)

entrada = tk.Entry(ventana)
entrada.pack(pady=5)

def sumar():
    a = float(entrada.get())
    b = float(entrada.get())
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def limpiar():
    entrada.delete(0, tk.END)
    etiqueta.config(text="Ingrese num1:")

    entrada.delete(0, tk.END)
    etiqueta.config(text="Ingrese num2:")

boton_sumar = tk.Button(ventana, text="SUMAR", command=sumar)
boton_sumar.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack(pady=5)

boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack(pady=5)

ventana.mainloop()
