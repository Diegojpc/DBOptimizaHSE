import pandas as pd
import numpy as np
import colorspacious as cs
from scipy.stats import shapiro, anderson

# Funcion para procesar data frame de dosis de ruido
def dosis_de_ruido(dataframe):

    # Definicion de paleta de colores:
    def gg_color(n):
        hues = np.linspace(16,375, num=n + 1)
        colors = cs.cspace_converter(cs.CAMO2UCS(), cs.sRGB1_space)(cs.HCLab(h = hues, c = 100, l = 70))
        # Convertir de punto flotante a entero (0-255)
        colors = (colors * 255).astype(int)

        return colors[:-1]  # Excluir el último color para que haya n colores
    
    def GoodFit(x,a):
        n = len(x) - x.isna().sum()
        contador = 0
        for i in range(n):
            if x[i] == 0:
                contador += 1

        repetidos = np.sum(np.array(list(x.values())) >= n)
        if n>4 and n<=5000:
            if contador == 0 and repetidos == 0:
                NM = 1 if shapiro(x)[1] > a else 0
                LN = 1 if shapiro(np.log(x))[1] > a else 0
            elif contador >= 1 and contador < n and repetidos == 0:
                NM = 1 if shapiro(x)[1] > a else 0
                LN = 0
        elif n > 5000:
            if contador == 0 and repetidos == 0:
                NM = 1 if anderson(x, dist='norm')[1] > a else 0
                LN = 1 if anderson(np.log(x), dist='norm')[1] > a else 0
            elif contador >= 1 and contador < n and repetidos == 0:
                NM = 1 if anderson(x, dist='norm')[1] > a else 0
                LN = 0
        else:
            NM, LN = 0, 0

        return np.array([NM, LN])    
 
