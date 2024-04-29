import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo Excel
archivo_excel = 'ruta/a/tu/archivo.xlsx'
datos = pd.read_excel(archivo_excel)

# Mostrar las primeras filas para verificar que se hayan cargado correctamente
print(datos.head())

tipo_variable = input("Son las variables del archivo cualitativas (C) o cuantitativas (Q)? Ingrese C o Q: ")

# Verificar la respuesta del usuario y realizar el analisis correspondiente
if tipo_variable.upper() == 'C':
    
    descripcion = datos.describe(include='object')
    print(descripcion)
elif tipo_variable.upper() == 'Q':

    descripcion = datos.describe()
    print(descripcion)
else:
    print("Respuesta invalida. Por favor, ingrese C o Q.")

# Visualizacion basica si son variables cuantitativas
if tipo_variable.upper() == 'Q':
    sns.pairplot(datos)
    plt.show()


