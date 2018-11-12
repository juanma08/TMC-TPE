import random
import math
def CalcularProb(Ciclos):
    Contador=0
    for i in range(0, Ciclos):
        x = Resultado()
        if x != -1:
            Contador= Contador + 1
        i = i+1
    return (Contador/Ciclos)    
    

def PatenteAleatoria():
    patente = random.randint(0, 999)
    return patente

def ListaAleatorios(n):
    lista = []
    while len(lista) < n:
        x = PatenteAleatoria()
        if x not in lista:
            lista.append(x)   
    return lista                
       
def Estacionar(PatentesAutos):
    x = len(PatentesAutos)
    Estacionamiento = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
    Estaciono = 0
    for i in range(0, x-1):
        Estaciono = Estaciono + 1
        Patente = PatentesAutos[i]
        lugar = Patente % 20
        if (Estacionamiento[lugar] == 1):
            return (Estaciono)
        else:
            Estacionamiento[lugar] = 1           
    return (-1)       

def Resultado ():
    CantAutos = 10
    Autos = ListaAleatorios(CantAutos)
    Logro = Estacionar(Autos)
    return (Logro)

def DiferenciaProb (E):
    Condicion = True
    ContLogros = 0
    Contador = 0
    ProbActual = 0
    ProbAnterior = 0
    while Condicion:
        Contador = Contador + 1
        x = Resultado()
        if (x == -1):
            ContLogros = ContLogros + 1
        if ((math.fabs(ProbAnterior-ProbActual) < E) and (Contador > 10)):
            Condicion = False
        else: 
            ProbAnterior = ProbActual
        ProbActual = (ContLogros/Contador)    
    return (Contador)
            
        

Epsilon = 0.01
CantCiclos = 1000
IncisoA = Resultado()
IncisoB = CalcularProb(CantCiclos)
IncisoD = DiferenciaProb(Epsilon)
print (IncisoA)
print (IncisoB)
print (IncisoD)