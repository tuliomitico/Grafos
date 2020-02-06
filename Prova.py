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

def procura(pai, i): 
        if pai[i] == i: 
            return i 
        return procura(pai, pai[i]) 
  
     
     
def uniao(pai, rank, x, y): 
        xraiz = procura(pai, x) 
        yraiz = procura(pai, y) 
   
        if rank[xraiz] < rank[yraiz]: 
            pai[xraiz] = yraiz 
        elif rank[xraiz] > rank[yraiz]: 
            pai[yraiz] = xraiz 
  
          
         
        else : 
            pai[yraiz] = xraiz
            rank[xraiz] += 1        

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
def prim(file):
    file = np.asarray(file,dtype=np.int64)
    vertices = file.shape[0]
    
    n = 2**64
    key = [n] * vertices
    pai = [None] * vertices
    key[0] = 0
    conj_spt= [False] * vertices

    pai[0] = -1
    
    aux = n
    for i in range(vertices):
        for k in range(vertices):
            if key[k] < aux and conj_spt[k] == False:
                aux = key[k]
                min_index = k
    
        conj_spt[min_index]
        for j in range(vertices):
             if file[min_index][j] > 0 and conj_spt[j] == False and key[j] > file[min_index][j]: 
                        key[j] = file[min_index][j] 
                        pai[j] = min_index 

    print ("Arestas \t Custo")
    for i in range(1, vertices): 
        print (i, "-", pai[i], "\t", file[i][ pai[i] ] )


def kruskal(file):

    file = np.asarray(file,dtype=np.int64)
    vertices = file.shape[0]
    file_adap = gerar_matriz_do_algoritmo(file)

    resultado=[]

    i,e = 0,0

    file_adap = qsort(file_adap, 0, len(file_adap) - 1)

    pai, rank = [],[]

    for no in range(vertices):
        pai.append(no)
        rank.append(0)

    while e < vertices - 1:

        a,b,c = file_adap[i]
        i+=1
        x,y = procura(pai,a),procura(pai,b)

        if x != y:
            e+=1
            resultado.append([a,b,c])
            uniao(pai,rank,x,y)
    
    print ("Arvore Geradore Minima")
    for a,v,custo  in resultado: 
        
        print ("%d -- %d == %d" % (a,v,custo))



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

bellman(lista2,0)
djkistra(lista2,0)
kruskal(lista2)
prim(lista2)