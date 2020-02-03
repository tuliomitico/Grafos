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

def particao(v,esq,direi):
    pivo = v[direi][2]
    i = esq - 1
    for j in range(esq,direi):
        if v[j][2] < pivo:
            i+=1
            v[i],v[j] = v[j],v[i]
    v[i+1],v[direi] = v[direi],v[i+1]
    return i+1
        

def qsort(v,esq,direi):
    while esq < direi:
        p = particao(v,esq,direi)
        if p < esq < direi - p:
            qsort(v,esq,p - 1)
            esq = p + 1
        else:
            qsort(v,p+1,direi)
            direi = p - 1
    return v
#Algoritmos de Arvore Minima
#----------------------------

def kruskal(file):

    file = np.asarray(dtype=np.int64)
    vertices = file.shape[0]
    file_adap = gerar_matriz_do_algoritmo(file)

    resultado=[]

    a,b = 0,0

    file_adap = qsort(file_adap, 0, len(file_adap) - 1)

    pai, rank = [],[]

    for no in range(vertices):


#Algoritmos de Arvore Geradora
#-----------------------------    

def djkistra(file,v_origem):

    file = np.asarray(file,dtype=np.int64)

    nr_vertices = file.shape[0]
    
    mini = (2**64) - 1
    
    distancia = [mini] * nr_vertices
    distancia[v_origem] = 0
    
    conj_spt = [False] * nr_vertices

    for i in range(nr_vertices):
        for j in range(nr_vertices):
            if distancia[j] < mini and conj_spt[j] == False:
                mini = conj_spt[j]
                mini_index = j
        
        conj_spt[mini_index] = True

        for k in range(nr_vertices):
            if file[mini_index][k] > 0 and conj_spt[k] == False and \
                distancia[k] > distancia[mini_index] + file[mini_index][k]:
                distancia[k] = distancia[mini_index] + file[mini_index][k]
    print("Vertice \t distancia da origem")
    for l in range(nr_vertices):
        print("%d\t%d" %(l,distancia[l]))

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

#Chamadas das funções

lista1 = gerar_matriz_do_algoritmo(matrizlocona)
print(qsort(lista1,0,len(lista1)-1))
bellman(lista2,0)
djkistra(lista2,0)