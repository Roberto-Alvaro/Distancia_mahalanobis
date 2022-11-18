
import pandas as pd # Importacion estandar de la libreria Pandas
import numpy  as np # Importacion estandar de la libreria NumPy
from collections import Counter


def calculoMahalanobis(ruta):
    df = pd.read_excel(ruta, sheet_name = 'Hoja1')
    print(df)
    filas, columnas = df.shape
    #print("Numero de columnas", columnas)
    print("Numero de columnas: ", filas)
    df_centroide, lista_centroide = centroide(df,filas)
    df_matriz, df_df = operacionesDF(df,df_centroide,filas)
    distanciasM(df,filas,df_matriz,lista_centroide)

def centroide(df,filas):
    lista_matriz = []
    lista_centroide = []

    for key in df:
        centroide = 0
        centroide = df[key].sum()
        centroide = centroide / filas
        lista_centroide.append(centroide)
    #print(lista_centroide)
    for i in range(filas):
        lista_matriz.append(lista_centroide)
    #print(lista_matriz)
    df2 = pd.DataFrame(lista_matriz)
    print("The DataFrame generated from the NumPy array is:")
    print(df2)
    return df2,lista_centroide

def operacionesDF(df1,df2,filas):
    print("-------------------------------------------------------------")
    matriz = []
    matriz2 = []
    matriz = df1.values
    matriz2 = df2.values
    A = ((np.transpose(matriz - matriz2)))
    B = (matriz - matriz2)
    f = np.dot(A,B)
    f = np.divide(f, filas-1)
    f2 = pd.DataFrame(f)
    print(f2)
    return f,f2

def distanciasM(df, filas,df_matriz,lista_centroide):
    print("-------------------------------------------------------------")
    #print(df.iloc[0])
    matriz = df.values
    matriz2 = matriz
    contador = 1
    list_aux = []
    bandera = False
    #lista_guarda2 = []
    matriz_final = []
    #matriz_ceros = np.zeros((filas,filas))
    for i in matriz:
        #print("un lista numero", contador, i)
        list_aux = i
        
        #print("esto es ", list_aux)
        bandera3 = False
        for j in matriz2:
            bandera = Counter (i) == Counter(j)
            bandera2 = (Counter (list_aux) == Counter(j))
            if((len(i) != 0) and bandera == False and bandera3):
                #print("la resta de ", i, "y" , j)
                resta = (i - j)
                inversa = np.linalg.inv(df_matriz)
                transpuesta = ((np.transpose(resta)))
                multiplicacion = np.dot(inversa,transpuesta)
                distancia = np.dot(resta,multiplicacion)
                print(distancia)
                lista_guarda.append(distancia)
            elif(bandera2 == True):
                resta = list_aux-lista_centroide
                inversa = np.linalg.inv(df_matriz)
                transpuesta = ((np.transpose(resta)))
                multiplicacion = np.dot(inversa,transpuesta)
                distancia = np.dot(resta,multiplicacion)
                lista_guarda = []
                print("digonal: ", distancia)
                lista_guarda.append(distancia)
                bandera3 = True
            #lista_guarda2.append(lista_guarda2)
            #lista_guarda = []
        #print(lista_guarda)
        while len(lista_guarda) < filas:
            lista_guarda.insert(0, 0)
        matriz_final.append(lista_guarda)
        contador = 1 + contador
    #print(matriz_final)
    df_final = pd.DataFrame(matriz_final)
    print("-------------------------------------------------------------")
    print(df_final)
ruta = ("C:/Users/espar/Desktop/Algoritmos-agrupamiento/Libro1.xlsx")
result  = calculoMahalanobis(ruta)


