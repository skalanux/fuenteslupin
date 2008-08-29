#!/usr/bin/env python
# -*- coding: latin-1 -*-

# Script para Gimp en Python
# Realizado por Juan Manuel Schillaci
# http://www.lanux.org.ar


from gimpfu import *
import re

def simularEscritura(img, drawable, author, globo_texto):
    INTERLETREADO = 0
    #Ahora separamos el texto por letra y vamos escribiendo una letra al lado de la otra.
    #Fijarse el autor, Respetar los saltos de linea, ver negrita italica, ver diferentes epocas del autor, fijarse tambien de hacer un random de letras para que no se note tanto ver acentos negritas signos de exclamacion etc
    posx = 0;
    sistemPath = "/home/ska/Escritorio/"
    letterPath = "let/"
    for letra in globo_texto:
        if letra!=' ':
            file = sistemPath + letterPath + author + "/" + letra.lower()+'.gif'
            try:
                layerletra = pdb.gimp_file_load_layer(img,file)
                img.add_layer(layerletra, 0)
                #Para saber cuanto muevo tengo que medir el ancho de la letra ya que no es monoespaciado, por ejemplo la i va a tener diferente ancho que la g
                #pdb.gimp_message(posx)
                pdb.gimp_layer_translate(layerletra, posx, 0)
                posx=posx +layerletra.width + INTERLETREADO
            except:
                pass
        else:
            posx=posx + 2

# función principal
if __name__ == '__main__':

	# llamada a función register
    register(
		"fuenteslupin",
		"Fuentes Lupin",
		"Fuentes Lupin",
		"Juan Manuel Schillaci",
		"Juan Manuel Schillaci",
		"2008",
		"<Image>/Python-Fu/Simula escritura de dibujantes de lupin",
		"RGB*, GRAY*",
		[
            (PF_RADIO, "author", "Elija el autor", "dol", (("DOL","dol"), ("Guerrero","guerrero"), ("Hercu","hercu"))),
			(PF_STRING, "globo_texto", "Ingrese texto", "Hola este es texto para la lupin"),
        ],
        [],
		simularEscritura)
    main()
