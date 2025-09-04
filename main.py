import tkinter as tk

ventana = tk.Tk()
ventana.title("CALCULADORA")
ventana.geometry("600x400")

etiqueta1 = tk.Label(ventana, text="Ingrese num1:")
etiqueta1.pack(pady=5)
entrada1 = tk.Entry(ventana)
entrada1.pack(pady=5)


etiqueta2 = tk.Label(ventana, text="Ingrese num2:")
etiqueta2.pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack(pady=5)

etiqueta_resultado = tk.Label(ventana, text="El RESULTADO ES: ")
etiqueta_resultado.pack(pady=10)

def sumar():

    a = float(entrada1.get())
    b = float(entrada2.get())
    resultado = a + b
    etiqueta_resultado.config(text=f"El RESULTADO ES: {resultado}")

def restar():
    a = float(entrada1.get())
    b = float(entrada2.get())
    resultado = a - b
    etiqueta_resultado.config(text=f"El RESULTADO ES: {resultado}")

def multiplicar():
    a = float(entrada1.get())
    b = float(entrada2.get())
    resultado = a * b
    etiqueta_resultado.config(text=f"El RESULTADO ES: {resultado}")

def dividir():
    a = float(entrada1.get())
    b = float(entrada2.get())
    resultado = a / b
    etiqueta_resultado.config(text=f"El RESULTADO ES: {resultado}")

def limpiar():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    etiqueta_resultado.config(text="El RESULTADO ES: ")

boton_sumar = tk.Button(ventana, text="SUMAR", command=sumar)
boton_sumar.pack(pady=5)

boton_restar = tk.Button(ventana, text="RESTAR", command=restar)
boton_restar.pack(pady=5)

boton_multiplicar = tk.Button(ventana, text="MULTIPLICAR", command=multiplicar)
boton_multiplicar.pack(pady=5)

boton_dividir = tk.Button(ventana, text="DIVIDIR", command=dividir)
boton_dividir.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack(pady=5)

boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack(pady=5)

ventana.mainloop()
