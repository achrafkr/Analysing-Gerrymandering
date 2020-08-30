# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 18:18:30 2020

@author: Achraf
"""
import numpy as np 
import shapely.geometry as geom
import geopandas as gpd

import json
import pandas as pd
import matplotlib.pyplot as plt
import shapefile 
import Curve_gradient_descent as gd 
import Curve_utils

def polsby_popper(closed_curve): 
    region = geom.Polygon(closed_curve)
    return (4 * np.pi * region.area) / (region.length ** 2)

def Polsby_evo(curve,steps):
    Evo = np.zeros(steps+1)
    Evo[0] = polsby_popper(curve)
    for i in range(steps):
        Evo[i+1] = polsby_popper(flow1(curve,i))
    return Evo  #Retourne un vecteur contenant l'evolution de la compacité de la courbe

def curve_from_shapefile_json(filename, data): #modificado para que funcione para archivos .json con con pandas

    if data == 'narrow': #extrait le
        district = int(input('Choisissez une circonscription ')) #car input renvoit une chaine de caracteres
        file = pd.read_json(filename) #on utilise la librairie pandas
        fd = file['fields']
        if 'geo_shape' in fd[district]:
            if fd[district]['geo_shape']['type'] == 'Polygon':
                curve_outline = fd[district]['geo_shape']['coordinates'][0] #liste contenant les coordonnées de la circonscription
            else: #type 'MultiPolygon' car on a que 2 types
                nbPol = len(fd[district]['geo_shape']['coordinates']) #nbe de Polygones dans la liste 'coordinates'
                Pol = int(input('Quelle circonscription voulez-vous choissir sur {} éléments?'.format(nbPol)))
                while Pol>= nbPol: #ajouté pour eviter l'affichage d'erreurs en entrée
                    Pol = int(input('Quelle circonscription voulez-vous choissir sur {} éléments?'.format(nbPol)))
                curve_outline = fd[district]['geo_shape']['coordinates'][Pol][0] #Soit Pol in [0,nbPol-1] soit on prend Pol-1
            return np.array(curve_outline)   #format pour mieux traiter les données
        else:
            print('Champ manquant; impossible de produir une courbe')
            return 0
            
    if data == 'wide': #a completer
        district = int(input('Choisissez une circonscription '))
        with open(filename, 'r') as f: #'r', 'w', '+' pour lecture, écriture et lecture+écriture
            file = json.load(f)
        #Puisque le 'type' de tous les éléments du dictionnaire ...['geometry'] sont 'Polygon', on utilisera len pour differencier
        #s'il s'agit d'un MultiPolygon
        if len(file['features'][district]['geometry']['coordinates']) == 1: #Polynome simple
            curve_outline = file['features'][district]['geometry']['coordinates'][0]
        else:
            nbPol = len(file['features'][district]['geometry']['coordinates'])
            Pol = int(input('Quelle circonscription voulez-vous choissir sur {} éléments?'.format(nbPol)))
            curve_outline = file['features'][district]['geometry']['coordinates'][Pol]
        return np.array(curve_outline)
    else: 
        print('Format inconnu')
    
