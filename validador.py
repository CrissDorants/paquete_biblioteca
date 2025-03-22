import tkinter as tk
from .utils import validar_dato

class ValidadorEntrada:
    def __init__(self, master, tipo_validacion):
        self.tipo_validacion = tipo_validacion
        self.campo_texto = tk.Entry(master)
        self.etiqueta_mensaje = tk.Label(master, text="")
        self.boton_validar = tk.Button(master, text="Validar", command=self.validar_entrada)
    
        self.campo_texto.pack()
        self.etiqueta_mensaje.pack()
        self.boton_validar.pack()

    def validar_entrada(self):
        texto = self.campo_texto.get()
        if validar_dato(texto, self.tipo_validacion):
            self.etiqueta_mensaje.config(text="Entrada válida", fg="green")
        else:
            self.etiqueta_mensaje.config(text="Entrada no válida", fg="red")
    
    def get_valor_ingresado(self):
        return self.campo_texto.get()