import tkinter as tk
import sqlite3
from tkinter import filedialog
import openpyxl


def insertar_desde_excel():
   
    archivo_excel = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx")])
    
    if archivo_excel:
       
        conexion = sqlite3.connect('usuarios.db')
        cursor = conexion.cursor()
        
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                          (nombre TEXT, edad INTEGER)''')
        
        
        wb = openpyxl.load_workbook(archivo_excel)
        hoja = wb.active
        for fila in hoja.iter_rows(values_only=True):
            nombre, edad = fila
            cursor.execute("INSERT INTO usuarios VALUES (?, ?)", (nombre, edad))
        
        
        conexion.commit()
        conexion.close()


ventana = tk.Tk()
ventana.title('Inserción de datos desde Excel')


marco = tk.Frame(ventana)
marco.pack(padx=10, pady=10)


boton_insertar_excel = tk.Button(marco, text='Insertar desde Excel', command=insertar_desde_excel)
boton_insertar_excel.pack(padx=5, pady=5)


ventana.mainloop()