from skimage.transform import (hough_line, hough_line_peaks)
import numpy as np
import cv2
import math

def angulo(image,debug=False):
    '''
    A esta funcion se le pasa una imagen en negro con dos lineas y te calcula el ángulo entre las líneas
    '''
    #image = cv2.imread('2.png')

    # Compute arithmetic mean
    #image = np.mean(image,axis=2)

    # Perform Hough Transformation to detect lines
    
    # hspace, angles, distances = hough_line(image)

    # # Find angle
    # angle=[]
    # for _, a , distances in zip(*hough_line_peaks(hspace, angles, distances,min_angle=1,min_distance=1)):
    #     angle.append(a)

    # # Obtain angle for each line
    # angles = [a*180/np.pi for a in angle]

    # # Compute difference between the two lines
    # angle_difference = np.max(angles) - np.min(angles)

    # if debug:
    #     print(angle_difference)

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
    angle_neck = math.atan2(neck[1] - nose[1], neck[0] - nose[0]) * 180.0 /np.pi; 
    diff = angle_neck - 90
    return abs(diff)


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

    return diff #-0
    pass

def comprueba_brazos(l_elbow,l_shoulder,r_elbow,r_shoulder):

    pass


if __name__ == "__main__":

    #angle = comprueba_cuello((405,271),(402,424))
    l_shoulder = (497,423)
    r_shoulder = (306,426)
    angle = comprueba_cuello((0,400),(800,400))
    angle2 = comprueba_hombros(r_shoulder,l_shoulder)
    print(angle)
    print(angle2)
