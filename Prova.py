# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 14:26:14 2020

@author: Túlio
"""
import numpy as np

               # A B C  
matrizlocona = [[0,2,3], 
                [4,0,6], 
                [7,8,0]]

matriz_adj = open("janio.txt")                
lista = []
lista2 = []
for i in matriz_adj:
    lista = lista + i.split(",")
for j in lista:
    lista2.append(eval(j))
lista2 = np.asarray(lista2,dtype=np.int64).reshape(3,3)
                
def gerar_matriz_do_algoritmo(matriz):
    nova_matriz = []
    #dic = {}
    for i in range(len(matriz)):
        
        
        for j in range(len(matriz[i])):
            
            if matriz[i][j] != 0:
                nova_matriz.append([i,j,matriz[i][j]])
                
    return nova_matriz
    
                
def bellman(file,v_origem):
    file = np.asarray(file,dtype=np.int64)
    nr_vertices = file.shape[0]
    file_adap = gerar_matriz_do_algoritmo(file)
    distancia = [(2**64)-1] * nr_vertices
    arestas = len(file_adap)
    distancia[v_origem] = 0
        
    
    for i in range(nr_vertices-1):
        for j in range(arestas):
            if  distancia[file_adap[j][0]] + \
                file_adap[j][2] < distancia[file_adap[j][1]]:
                distancia[file_adap[j][1]] = distancia[file_adap[j][0]] + \
                file_adap[j][2]
    
    for i in range(arestas): 
        x = file_adap[i][0] 
        y = file_adap[i][1] 
        custo = file_adap[i][2] 
        if distancia[x] != (2**64) - 1 and distancia[x] + custo < distancia[y]: 
            print("Grafo contém ciclo de custo negativo") 
  
    print("Distancia do vértice a origem") 
    for i in range(nr_vertices): 
        print("%d\t\t%d" % (i, distancia[i])) 

    
bellman(lista2,0)

    
                
