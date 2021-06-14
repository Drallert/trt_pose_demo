from skimage.transform import (hough_line, hough_line_peaks)
import numpy as np
import cv2
import math


zonas_validas = {
    "neck":{
        "0":[range(85,90),range(90,95)],
        "1":[range(96,102),range(78,84)],
        "2":[range(103,114),range(66,77)],
        "3":[range(115,180),range(0,65)]
    }
    ,
    "shoulders":{
        "0":[range(0,5),range(175,180)],
        "1":[range(6,10),range(174,170)],
        "2":[range(11,20),range(169,160)],
        "3":[range(21,159)]
    },
    "arms":{
        "0":[range(77,90),range(90,103)],
        "1":[range(56,76),range(124,144)],
        "2":[range(23,55),range(145,157)],
        "3":[range(0,22),range(158,180)]
    }
    

}


def angulo(image,debug=False):
    '''
    A esta funcion se le pasan dos puntos que conforman una línea y calcula el ángulo de dicha línea
    '''


    

    return angle_difference

def comprueba_cuello(nose,neck,show=False):

    #Pasos: crear imagen en negro con la línea que queremos probar, despues añadir linea de comprobacion y por ultimo usar funcion angulo
    centro_abajo = (400,0)
    centro_arriba = (400,800)
    if show:
        blank = np.zeros((800,800))
        cv2.line(blank,nose,neck,(255,255,255))
        cv2.line(blank,centro_abajo,centro_arriba,(255,255,255))
        cv2.imshow('',blank)
        cv2.waitKey(0)
    #angle = angulo(blank,True)
    angle_neck = math.atan2(nose[1] - neck[1], nose[0] - neck[0]) * 180.0 /np.pi; 
    diff = angle_neck - 90
    return diff


def comprueba_hombros(r_shoulder,l_shoulder,show=False):

    centro_izq = (0,400)
    centro_derecha = (800,400)
    if show:
        blank = np.zeros((800,800))
        cv2.line(blank,r_shoulder,l_shoulder,(255,255,255))
        cv2.line(blank,centro_derecha,centro_izq,(255,255,255))
        cv2.imshow('',blank)
        cv2.waitKey(0)
    #angle = angulo(blank,True)
    angle_neck = math.atan2(l_shoulder[1] - r_shoulder[1], l_shoulder[0] - r_shoulder[0]) * 180.0 /np.pi; 
    diff = angle_neck

    return abs(diff) #-0
    pass

def comprueba_brazos(l_elbow,l_shoulder,r_elbow,r_shoulder,show=False):
    ang_izq = comprueba_cuello(l_elbow,l_shoulder,show)
    ang_derecha = comprueba_cuello(r_elbow,r_shoulder,show)
    return ang_izq,ang_derecha
    pass


if __name__ == "__main__":

    neck = (402,424)
    nose = (405,271)
    l_shoulder = (497,423)
    r_shoulder = (306,426)
    r_elbow = (800-603,800-239)
    l_elbow = (560,603)
    #angle = comprueba_cuello((0,400),(800,400))
    angle = comprueba_cuello(nose,neck,True)
    angle2 = comprueba_hombros(r_shoulder,l_shoulder,True)
    angle3,angle4 = comprueba_brazos(l_elbow,l_shoulder,r_elbow,r_shoulder,True)
    print(angle)
    print(angle2)
    print(angle3,angle4)
