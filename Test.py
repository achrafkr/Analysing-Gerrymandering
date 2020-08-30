# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 18:49:40 2020

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
#↓import Curve_animation as at
from shapely.geometry import Polygon


def polsby_popper(closed_curve): 
    region = geom.Polygon(closed_curve)
    return (4 * np.pi * region.area) / (region.length ** 2)

def curve_from_shapefile(filename, tolerance=0): #modificado para que funcione para archivos .json con con pandas
    """
    Reads in the shapefile at filename specifying a single polygonal outline
    and returns a simplified polygon (default tolerance=0 doesn't simplify read shape).
    """
    shape_data = pd.read_json(filename) 
    curve_outline = shape_data['geometry'][0]
    """ By default a slower algorithm is used that preserves topology. 
    If preserve topology is set to False the much quicker Douglas-Peucker is used.
    """
    return curve_outline.simplify(tolerance, preserve_topology = True) #funciona unicamente para tipos shapely.geometry.polygon.Polygon

MIN_DIST = 0.0125
alpha = 0.020*MIN_DIST
eps = 0.07

def unit_vector(vector):
    """ 
    Returns the unit vector of the vector.  
    """
    return vector / np.linalg.norm(vector)


def point_flow1(pt_index, curve):
    """
    Computes the displacement by which to move a point on the input curve at a step 
    of the discretized curve-shortening flow process. 
    Arguments:
    pt_index -- the index of the desired point in curve. 
    curve -- a numpy array of shape (length, 2). 
    """
    n = len(curve)
    pt = curve[pt_index]
    #puisque les pt 0 et n (ou n-1) sont en effet le même point
    if pt_index == 0:
        prev_pt = curve[((pt_index - 2) % n)]
        next_pt = curve[((pt_index + 1) % n)]
    elif pt_index%n == n-1:
        prev_pt = curve[((pt_index - 1) % n)]
        next_pt = curve[((pt_index + 2) % n)]
    else:
        prev_pt = curve[((pt_index - 1) % n)]
        next_pt = curve[((pt_index + 1) % n)]
    v1 = prev_pt - pt 
    v2 = next_pt - pt
    #print('prev_pt = {}, next_pt = {}'.format(prev_pt,next_pt))
    if geom.Polygon(curve).length<2: #differentiation entre grande et petite circonscription
        return (1/n)**2*(unit_vector(v1) + unit_vector(v2))
    else:
        return (1/n)*(unit_vector(v1) + unit_vector(v2)) #1/n coeff pour applatir? la courbe; on prend 1/n**2 (1/n**3??)
                                                         ##pour les district petits


def preprocess1(curve):
    """
    Performs some cleaning of the input discretized curve for flow stability. Presently 
    just removes points that are too close to each other. 
    """
    #MIN_DIST = 0.0125 #si no, probar con 0.025
    alpha = 0.020*MIN_DIST
    new_curve = np.empty((0,2), float)
    n = len(curve)
    last_pt = curve[-1]
    for pt_index, pt in enumerate(curve): #associa pt_index al punto pt
        dist = np.linalg.norm(pt - last_pt)
        if dist > MIN_DIST: 
            new_curve = np.append(new_curve, [pt], axis=0)
            last_pt = pt
    new_curve = np.append(new_curve,[np.array(new_curve[0])],axis = 0)
    #new_curve = np.vstack((new_curve,new_curve[0])) %mío, cierra la curba pegando los puntos separados
    return new_curve

def flow_step1(curve):
    """
    Performs a step of the discretized curve-shortening flow for the input curve. 
    """
    curve = preprocess1(curve)
    #curve = np.vstack((preprocess(curve),curve[0])) %mio, no es muy útil
    return np.array([pt + point_flow1(pt_index, curve) for pt_index, pt in enumerate(curve)])


def flow1(curve, steps):
    """
    Performs the discretized curve-shortening flow on the input curve for the given 
    number of steps.
    """
    #print('Flowing the curve: {}'.format(curve))
    for i in range(steps):
        curve = flow_step1(curve)
    #print("Finished flowing")
    return curve #%añadido por mi para ver la evolución

def Polsby_evo(curve,steps):
    Evo = np.zeros(steps+1)
    Evo[0] = polsby_popper(curve)
    for i in range(steps):
        Evo[i+1] = polsby_popper(flow1(curve,i))
    return Evo


###############################################################################################################################
def preprocess2(curve):
    """
    Performs some cleaning of the input discretized curve for flow stability. Presently 
    just removes points that are too close to each other. 
    """
    #MIN_DIST = 0.0125 #si no, probar con 0.025
    if geom.Polygon(curve).length < 2: #returns the perimeter of a polygon
        #MIN_DIST = 0.000125 #de maniere approximée
        MIN_DIST = 0.012
    else: 
        MIN_DIST = 0.0125 #suffisamment petit et facile pour pas rendre l'algor très lent
    alpha = 0.020*MIN_DIST
    new_curve = np.empty((0,2), float)
    n = len(curve)
    last_pt = curve[-1]
    for pt_index, pt in enumerate(curve): #associa pt_index al punto pt
        dist = np.linalg.norm(pt - last_pt)
        if dist > MIN_DIST: 
            new_curve = np.append(new_curve, [pt], axis=0)
            last_pt = pt
    new_curve = np.append(new_curve,[np.array(new_curve[0])],axis = 0)
    #new_curve = np.vstack((new_curve,new_curve[0])) %mío, cierra la curba pegando los puntos separados
    return new_curve

def flow_step2(curve, precision):
    """
    Performs a step of the discretized curve-shortening flow for the input curve. 
    """
    curve = preprocess2(curve)
    #curve = np.vstack((preprocess(curve),curve[0])) %mio, no es muy útil
    #Essayer avec un algo de descente par ex si possible
    Curve = np.array([pt + point_flow1(pt_index, curve) for pt_index, pt in enumerate(curve)])
    for pt_index, new_pt in enumerate(Curve):
        step = 1
        while gd.curvature(pt_index, Curve) > precision and step < 100:
            Curve[pt_index] = curve[pt_index] + point_flow1(pt_index,curve)/(step**2)
            step +=1
    return Curve


def flow2(curve, steps):
    """
    Performs the discretized curve-shortening flow on the input curve for the given 
    number of steps.
    """
    Curvature_list = [gd.curvature(pt_index,curve) for pt_index, pt in enumerate(curve)] #liste de la curvature de tous les pts
    Max_curvature = max(list(filter(lambda x: x<10**4, Curvature_list))) #liste filtrée, on enleve les valeurs > 10**4
    #print('Flowing the curve: {}'.format(curve))
    for i in range(steps):
        #curve = flow_step2(curve,Max_curvature/2**(i+1)+6)
        curve = flow_step2(curve,50) #assez suffisant pour eviter l'apparition des arcs très courbés, sans cependant altérer le
                                     #bon fonctionnement de la courbe
    #print("Finished flowing")
    return curve #%añadido por mi para ver la evolución




#Testlist2 = list(filter(lambda x: x<5000, Testlist)) pour filtrer, filter(fonction, iterable)


#with open('circonscriptions-occitanie.json', 'r') as f:
#    circ = json.load(f)


cur = pd.read_json('circonscriptions-occitanie.json')
cur_geo = cur['geometry']
cur_dataid = cur['datasetid']
cur_fd = cur['fields']
cur_rectime = cur['record_timestamp']
cur_id = cur['recordid']

#cur_fd[5]['geo_shape']['coordinates'][0]
#a = np.array(cur_fd[5]['geo_shape']['coordinates'][0]) %funciona bien para el plot

""" ### pour afficher plusieures circonscriptions dans un meme plot
for i in range():
    Arr = curve_from_shapefile_json('circonscriptions-[].json','type')
    plt.plot(Arr[:,0],Arr[:,1])
    plt.fill(Arr[:,0],Arr[:,1],'color') #remplissage couleur
    #autre façon de remplissage: 
    plt.fill("abscisse", "ordonnee", 'color', data={"abscisse": Arr[:,0], "ordonnee": Arr[:,1]})
"""

"""
with open('circonscriptions-paris.json', 'r') as f:
    Paris = json.load(f) #type 'wide' (modifier le nom de 'wide' et 'narrow' par qqch d'autre')
    
with open('circonscriptions-legislatives.json', 'r') as f:
    france = json.load(f)

F = np.array(france['features'][0]['geometry']['coordinates'][0])
plt.xlim(min(F[:,0]), max(F[:,0]))
plt.ylim=(min(F[:,1]), max(F[:,1]))
plt.plot(F[:,0],F[:,1])
plt.show()

### pour determiner si on a bien un format geo lisible
j = 0
for i in range(len(cur_fd)):
    if ('geo_shape' in cur_fd[i]) == False:
        j+=1
        print(i,j)
print(j)

### le type de frome (Polygone ou multipolygone)
for i in range(20):
    
    if 'geo_shape' in cur_fd[i]:
        print(cur_fd[i]['geo_shape']['type'])
    else: 
        print('geo_shape non existante la {}-eme colonne'.format(i))



plt.scatter(Dist2[:,0][::5],Dist2[:,1][::5], color = 'red',marker = '+')
plt.plot(Dist2[:,0],Dist2[:,1],'orange')


Small_dist = []
for i in range(len(cur_fd)):
    if 'geo_shape' in cur_fd[i]:
        if cur_fd[i]['geo_shape']['type'] == 'Polygon':
            if geom.Polygon(np.array(cur_fd[i]['geo_shape']['coordinates'][0])).length < 2:
                            Small_dist.append(np.array(cur_fd[i]['geo_shape']['coordinates'][0]))


"""

