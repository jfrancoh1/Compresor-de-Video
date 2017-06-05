from math import cos,sin,pi
from scipy.fftpack import dct,idct
import numpy as np
import random
from PIL import Image, ImageDraw, ImageFont
import os
from cdt import *


#Tamano de la imagen: Funcion que determina el tamano de la imagen original
def tamImage(imagen):
    tam = os.stat(imagen)
    return tam.st_size

#Funcion de carga la imagen desde el archivo
def cargarImage(imagen):
    image = Image.open(imagen)
    ancho, altura = image.size
    pixels = image.load()
    return ancho,altura,pixels,image

#Proceso final:
def escala(imagen, ran):
    ancho,altura,pixels,image = cargarImage(imagen)
    for i in range(ancho):
        for j in range(altura):
            (a,b,c) = pixels[i,j]
            suma = a+b+c
            prom = int(suma/3)
            a = prom #Igualamos
            b = prom
            c = prom
            pixels[i,j] = (a,b,c)
    image.save("Vid%04d.jpg" %ran)
    #image.save("comprimida.jpeg") #Se guarda la imagen nueva
    return
    
#Inicia el proceso de compreseion
def comprimir(imagen, ran):
    escala(imagen, ran) #Se pasa la imagen original a escala de gris
    ancho,altura,pixels,image = cargarImage(imagen) #Cargamos la imagen a gris
    i = 0
    j = 0
    #print ("Altura de la imagen: {}".format(altura)) #Nos da el alto de la imagen
    arreglo = []
    i = 0
    j = 0
    while i < altura: #Recorre la imagen (los bloques de 8 pixeles)
        while j < ancho:
            if ancho - j >= 8 and altura - i >= 8:
                mat = []
                for k in range(8): #Bloques de ocho pixeles
                    mat.append([])
                    for l in range(8):
                        mat[k].append(pixels[l+j,k+i][0]) #Guarda la matriz con lo nuevos valores
                mat = matrixTemporal(mat) #Llevamos la nueva matriz a la extension NUMPY para operar correctamente con ella
                mat = CDT(mat) #Aplicamos la transformada a la matriz y le hacemos la cuantificacion
                conts = 0
                array = []
                for k in range(8):
                    for l in range(8):
                        if mat[k][l] != 0 and abs(mat[k][l]) < 1: #Se da un valor maximo y se modifica la matriz cuantificada
                            mat[k][l]  = 0.0
                            array.append(pixels[j+l,i+k][0])
                            conts += 1
                finaly = InversaCDT(mat) #Se aplica LA INVERSA DELA TRANSFORMADA DEL DISCRETA DEL COSENO (DCT III)
                for k in range(8): #Dibujamos nuevamente la imagen
                    for l in range(8):
                        pixels[j+l,i+k] = (int(finaly[k][l]),int(finaly[k][l]),int(finaly[k][l]))
                j = j + 8
            else:
                j = j + 1
        i = i + 8
        j = 0
    image.save("Vid%04d.jpg" %ran)  #RESULTADO FINAL DE LA COMPRESION
    print("comprimió", ran)
    return
