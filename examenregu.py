# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 15:57:10 2020

@author: 
        Garcia Garcia Efrain 15590287
"""

"""
Cada numero vale 33 pts

Recursividad

1) Usando funciones recursivas haga una funcion capaz de imprimir
una lista de caracteres eliminando los espacios en blanco.

def noblanco(L):
	pass
	

noblanco(list("hola como estas"))
#holacomoestas
"""

def noblanco(L):
    L.remove(" ")
    L.remove(" ")
    separador =""
    L= separador.join(L)
    print(L)
    
	
	
noblanco(list("hola como estas"))

      
"""
2) Palindromo realice una funcion que nos idique si una lista de
caracteres es un palindromo

def palindromo
	pass
	
R = palindromo(list("ana"))
print(R)
#True
"""
def palindromo(p):
    if (p) == (p)[::-1]:
        return True
    else:
        return False
R = palindromo(list("ana"))
print(R)



"""
3) Realice una funcion que permita imprimir una matriz al revez

def imprimeMatR(M):
	pass
	
M = [
	[1,2],
	[3,4]
]

imprimeMatR(M)
# [3,4]
# [1,2]

"""
def imprimeMatR(M):
    if not M:
        return
    
    M[1:]
    print (M[1])
    print (M[0])
    return M
    
        
	
M = [
	[1,2],
	[3,4]
]

imprimeMatR(M)
