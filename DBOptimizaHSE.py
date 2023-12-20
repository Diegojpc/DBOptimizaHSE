import tkinter as tk
from tkinter import filedialog
import pandas as pd

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("DBOptimizaHSE")
        self.geometry("400x200")

        # Botón para seleccionar el archivo Excel
        self.btn_cargar = tk.Button(self, text="Cargar Excel", command=self.cargar_excel)
        self.btn_cargar.pack(pady=10)

        # Etiqueta para mostrar el resultado
        self.lbl_resultado = tk.Label(self, text="")
        self.lbl_resultado.pack(pady=10)

    def cargar_excel(self):
        # Diálogo para seleccionar el archivo Excel
        archivo_path = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx")])

        if archivo_path:
            # Leer datos desde el archivo Excel
            try:
                df = pd.read_excel(archivo_path)
                
                # Realizar algún procesamiento con los datos (aquí se muestra la suma de una columna)
                resultado = df['Columna_a_procesar'].sum()

                # Mostrar el resultado en la interfaz gráfica
                self.lbl_resultado.config(text=f"Resultado: {resultado}")

            except Exception as e:
                self.lbl_resultado.config(text="Error al procesar el archivo Excel")
                print(e)

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
