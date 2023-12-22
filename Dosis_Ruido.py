import pandas as pd
import numpy as np
import colorspacious as cs


# Funcion para procesar data frame de dosis de ruido
def dosis_de_ruido(dataframe):

    # Definicion de paleta de colores:
    def gg_color(n):
        hues = np.linspace(16,375, num=n + 1)
        colors = cs.cspace_converter(cs.CAMO2UCS(), cs.sRGB1_space)(cs.HCLab(h = hues, c = 100, l = 70))
        # Convertir de punto flotante a entero (0-255)
        colors = (colors * 255).astype(int)

        return colors[:-1]  # Excluir el último color para que haya n colores
