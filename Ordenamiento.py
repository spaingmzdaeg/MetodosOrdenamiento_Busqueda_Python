from time import time
import random
class Ordenamiento:
    def burbuja1(self,Lista):
        tam = len(Lista)
        tiempoInicial=time()
        i=0
        j=1
        temp=0
        pasadas=0
        comparaciones=0
        intercambios=0
        for i in range(0,tam):
            for j in range(i+1,tam):
                comparaciones=comparaciones+1
                if Lista[i]>Lista[j]:
                    intercambios=intercambios+1
                    temp=Lista[i]
                    Lista[i]=Lista[j]
                    Lista[j]=temp
                pasadas = pasadas + 1
        tiempoFinal=time()
        tiempoEjecucion=tiempoFinal-tiempoInicial
        print(Lista)
        print("Cantidad Pasadas:"+str(pasadas))
        print("Cantidad comparaciones:" + str(comparaciones))
        print("Cantidad intercambios:" + str(intercambios))
        print("Tiempo de ejecucion:"+str(tiempoEjecucion)+" ms ")
        #self.mostrarLista(Lista,tam)

    def burbuja2(self, Lista):
        tam=len(Lista)
        tiempoInicial = time()
        i = 0
        j = 1
        temp = 0
        pasadas = 0
        comparaciones = 0
        intercambios = 0
        for i in range(1, tam):
            for j in range(0, tam-1):
                comparaciones = comparaciones + 1
                if Lista[j] > Lista[j+1]:
                    intercambios = intercambios + 1
                    temp = Lista[j]
                    Lista[j] = Lista[j+1]
                    Lista[j+1] = temp
                pasadas = pasadas + 1
        tiempoFinal = time()
        tiempoEjecucion = tiempoFinal - tiempoInicial
        print(Lista)
        print("Cantidad Pasadas:" + str(pasadas))
        print("Cantidad comparaciones:" + str(comparaciones))
        print("Cantidad intercambios:" + str(intercambios))
        print("Tiempo de ejecucion:" + str(tiempoEjecucion) + " ms ")
        # self.mostrarLista(Lista,tam)



    def burbuja3(self,arr):
        n = len(arr)
        comparaciones=0
        intercambios=0
        pasadas=0


        tiempoInicial = time()
        for i in range(n):
            cambio = False


            for j in range(0, n - i - 1):
                comparaciones = comparaciones + 1


                if arr[j] > arr[j + 1]:
                    intercambios = intercambios + 1
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    cambio = True
                pasadas = pasadas + 1


            if cambio == False:
                break
        tiempoFinal = time()
        tiempoEjecucion = tiempoFinal - tiempoInicial
        print(arr)
        print("Cantidad Pasadas:" + str(pasadas))
        print("Cantidad comparaciones:" + str(comparaciones))
        print("Cantidad intercambios:" + str(intercambios))
        print("Tiempo de ejecucion:" + str(tiempoEjecucion) + " ms ")


#este metodo es opcional
    def mostrarLista(self,Lista,tam):
        for i in range(0,tam):
            print ("["+str(Lista[i])+"]")

#funcion estatica numeros aleatorios
def llenarLista(n):
    lista = [0] * n
    for i in range(n):
        lista[i] = random.randint(0, 100)
    return lista


listaA=llenarLista(1000)
listaB=llenarLista(10000)
listaC=llenarLista(100000)
listaD=llenarLista(1000000)
obj=Ordenamiento()
opcion=""
while(not opcion=="Z"):
    opcion = input("----Seleccione Algoritmo-----\nA)Burbuja_1\nB)Burbuja_2\nC)Burbuja_3\nZ)Salir").upper()
    if(opcion == "A"):
        var = input(
            "eliga cantidad de numeros para la prueba de estres...\nA)1000\nB)10,000\nC)100,000\nD)Un Millon").upper()
        if var == "A":
            listaAux = listaA.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.burbuja1(listaAux)
        elif var == "B":
            listaAux = listaB.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.burbuja1(listaAux)
        elif var == "C":
            listaAux = listaC.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.burbuja1(listaAux)
        elif var == "D":
            listaAux = listaD.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.burbuja1(listaAux)
    elif (opcion == "B"):
        var = input(
            "eliga cantidad de numeros para la prueba de estres...\nA)1000\nB)10,000\nC)100,000\nD)Un Millon").upper()
        if var == "A":
            listaAux = listaA.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.burbuja2(listaAux)
        elif var == "B":
            listaAux = listaB.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.burbuja2(listaAux)
        elif var == "C":
            listaAux = listaC.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.burbuja2(listaAux)
        elif var == "D":
            listaAux = listaD.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.burbuja2(listaAux)
    elif (opcion == "C"):
        var = input(
            "eliga cantidad de numeros para la prueba de estres...\nA)1000\nB)10,000\nC)100,000\nD)Un Millon").upper()
        if var == "A":
            listaAux = listaA.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.burbuja3(listaAux)
        elif var == "B":
            listaAux = listaB.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.burbuja3(listaAux)
        elif var == "C":
            listaAux = listaC.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.burbuja3(listaAux)
        elif var == "D":
            listaAux = listaD.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.burbuja3(listaAux)





