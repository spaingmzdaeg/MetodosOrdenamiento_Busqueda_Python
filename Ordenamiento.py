from time import time
import random
from math import log
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

    def insercion(self,unaLista):
        intercambios=0
        pasadas=0
        comparaciones=0
        tiempoInicial = time()
        for indice in range(1, len(unaLista)):
            comparaciones=comparaciones+1

            valorActual = unaLista[indice]
            posicion = indice

            while posicion > 0 and unaLista[posicion - 1] > valorActual:
                intercambios=intercambios+1
                unaLista[posicion] = unaLista[posicion - 1]
                posicion = posicion - 1
            pasadas=pasadas+1

            unaLista[posicion] = valorActual
        tiempoFinal = time()
        tiempoEjecucion = tiempoFinal - tiempoInicial
        print(unaLista)
        print("Cantidad Pasadas:" + str(pasadas))
        print("Cantidad comparaciones:" + str(comparaciones))
        print("Cantidad intercambios:" + str(intercambios))
        print("Tiempo de ejecucion:" + str(tiempoEjecucion) + " ms ")

    def seleccion(self,unaLista):
        intercambios = 0
        pasadas = 0
        comparaciones = 0
        tiempoInicial = time()
        for llenarRanura in range(len(unaLista) - 1, 0, -1):
            posicionDelMayor = 0
            for ubicacion in range(1, llenarRanura + 1):
                comparaciones=comparaciones+1
                if unaLista[ubicacion] > unaLista[posicionDelMayor]:
                    posicionDelMayor = ubicacion
                pasadas=pasadas+1
            intercambios = intercambios + 1

            temp = unaLista[llenarRanura]
            unaLista[llenarRanura] = unaLista[posicionDelMayor]
            unaLista[posicionDelMayor] = temp

        tiempoFinal = time()
        tiempoEjecucion = tiempoFinal - tiempoInicial
        print(unaLista)
        print("Cantidad Pasadas:" + str(pasadas))
        print("Cantidad comparaciones:" + str(comparaciones))
        print("Cantidad intercambios:" + str(intercambios))
        print("Tiempo de ejecucion:" + str(tiempoEjecucion) + " ms ")

    def shell(self,lista, tam):
        intercambios = 0
        pasadas = 0
        comparaciones = 0
        tiempoInicial = time()
        inc = 1
        for inc in range(1, tam, inc * 3 + 1):
            pasadas=pasadas+1
            while inc > 0:
                for i in range(inc, tam):
                    comparaciones=comparaciones+1
                    j = i
                    temp = lista[i]
                    while j >= inc and lista[j - inc] > temp:
                        intercambios=intercambios+1
                        lista[j] = lista[j - inc]
                        j = j - inc
                    lista[j] = temp
                inc = inc / 2
        tiempoFinal = time()
        tiempoEjecucion = tiempoFinal - tiempoInicial
        print(lista)
        print("Cantidad Pasadas:" + str(pasadas))
        print("Cantidad comparaciones:" + str(comparaciones))
        print("Cantidad intercambios:" + str(intercambios))
        print("Tiempo de ejecucion:" + str(tiempoEjecucion) + " ms ")

    def quicksort(lista):
        izquierda = []
        centro = []
        derecha = []
        if len(lista) > 1:
            pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
                return izquierda + centro + derecha
            else:
                return lista
    #la implementacion del metodo radix en pytrhon es compleja y consta de varios metodos
    def getDigit(self,num, base, digit_num):
        # pulls the selected digit
        return (num // base ** digit_num) % base

    def makeBlanks(self,size):
        # create a list of empty lists to hold the split by digit
        return [[] for i in range(size)]

    def split(self,a_list, base, digit_num):
        buckets = self.makeBlanks(base)
        for num in a_list:
            # append the number to the list selected by the digit
            buckets[self.getDigit(num, base, digit_num)].append(num)
        return buckets

    # concatenate the lists back in order for the next step
    def merge(self,a_list):
        new_list = []
        for sublist in a_list:
            new_list.extend(sublist)
        return new_list

    def maxAbs(self,a_list):
        # largest abs value element of a list
        return max(abs(num) for num in a_list)

    def split_by_sign(self,a_list):
        # splits values by sign - negative values go to the first bucket,
        # non-negative ones into the second
        buckets = [[], []]
        for num in a_list:
            if num < 0:
                buckets[0].append(num)
            else:
                buckets[1].append(num)
        return buckets

    def radixSort(self,a_list, base):
        # there are as many passes as there are digits in the longest number
        passes = int(round(log(self.maxAbs(a_list), base)) + 1)
        new_list = list(a_list)
        for digit_num in range(passes):
            new_list = self.merge(self.split(new_list, base, digit_num))
        return self.merge(self.split_by_sign(new_list))

    import time
    import random

    randfile = open("Random.txt", "w")

    start = int(input('Enter lower limit of random numbers: '))
    end = int(input('Enter upper limit of random numbers: '))

    for i in range(int(input('How many to generate?: '))):
        line = str(random.randint(start, end))
        randfile.write(line + '\n')
        print(line)

    randfile.close()

    # example of selection sort algorithm : needs modification

    def swap(a, i, j):
        (a[i], a[j]) = (a[j], a[i])

    def selectionSort(a):
        n = len(a)
        for startIndex in range(n):
            minIndex = startIndex
            for ind in range(startIndex + 1, n):
                if a[ind] < a[minIndex]:
                    minIndex = ind
            swap(a, startIndex, minIndex)

    lst = []
    with open("Random.txt", "r") as f:
        for line in f:
            lst.append(int(line.strip()))

    start_time = time.time()
    selectionSort(lst)
    end_time = time.time()

    file = open("selectionSortResult", "w")
    for x in lst:
        file.write(str(x) + "\n")
    file.close()
    print('Sorted Selection Sort List: ', lst)
    print('Elapsed time for Selection Sort: {:.20f} seconds'.format(end_time - start_time))

    def merge_sort(A):
        """
        Sort list A into order, and return result.
        """
        n = len(A)
        if n == 1:
            return A
        mid = n // 2  # floor division
        L = merge_sort(A[:mid])
        R = merge_sort(A[mid:])
        return merge(L, R)

    def merge(L, R):
        """
        Given two sorted sequences L and R, return their merge.
        """
        i = 0
        j = 0
        answer = []
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                answer.append(L[i])
                i += 1
            else:
                answer.append(R[j])
                j += 1
        if i < len(L):
            answer.extend(L[i:])
        if j < len(R):
            answer.extend(R[j:])
        return answer

    lst = []
    # opens and reads 'Random.txt'
    with open("Random.txt", "r") as f:
        for line in f:
            lst.append(int(line.strip()))

    start_time = time.time()
    lst = merge_sort(lst)
    end_time = time.time()

    # opens and
    def intercalacionArchivos(self):
        archivo3 = open("ArchivoSalida.txt", "w")
        archivo1 = open("Archivo1.txt", "r")
        archivo2 = open("Archivo2.txt", "r")
        repetir = True

        lineaArchivo1 = archivo1.readline()
        lineaArchivo2 = archivo2.readline()

        '''Se realizan comparaciones mientras la bandera no cambie'''
        while (repetir):
            if (int(lineaArchivo1) < int(lineaArchivo2)):
                archivo3.write(lineaArchivo1)
                lineaArchivo1 = archivo1.readline()
                if (lineaArchivo1 == ""):
                    archivo3.write("\n")
                    archivo3.write(lineaArchivo2)
                    lineaArchivo2 = archivo2.readline()
                    while (lineaArchivo2 != ""):
                        archivo3.write(lineaArchivo2)
                        lineaArchivo2 = archivo2.readline()
                    repetir = False
            elif (int(lineaArchivo1) > int(lineaArchivo2)):
                archivo3.write(lineaArchivo2)
                lineaArchivo2 = archivo2.readline()
                if (lineaArchivo2 == ""):
                    archivo3.write("\n")
                    archivo3.write(lineaArchivo1)
                    lineaArchivo1 = archivo1.readline()
                    while (lineaArchivo1 != ""):
                        archivo3.write(lineaArchivo1)
                        lineaArchivo1 = archivo1.readline()
                    repetir = False
            else:
                archivo3.write(lineaArchivo1)
                archivo3.write(lineaArchivo2)
                lineaArchivo1 = archivo1.readline()
                if (lineaArchivo1 == ""):
                    archivo3.write("\n")
                    archivo3.write(lineaArchivo2)
                    lineaArchivo2 = archivo2.readline()
                    while (lineaArchivo2 != ""):
                        archivo3.write(lineaArchivo2)
                        lineaArchivo2 = archivo2.readline()
                    repetir = False
                lineaArchivo2 = archivo2.readline()
                if (lineaArchivo2 == ""):
                    archivo3.write("\n")
                    archivo3.write(lineaArchivo1)
                    lineaArchivo1 = archivo1.readline()
                    while (lineaArchivo1 != ''):
                        archivo3.write(lineaArchivo1)
                        lineaArchivo1 = archivo1.readline()
                    repetir = False
        archivo2.close
        archivo1.close
        print("Archivos combinados y ordenados correctamente")
        archivo3.close


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
    opcion = input(
        "----Seleccione Algoritmo-----\n A)Burbuja_1\nB)Burbuja_2\nC)Burbuja_3\nD)Insercion\nE)Seleccion\nF)Shell\nG)Quicksort\nH)RADIX\nI)Intercalacion\nJ)Mezlca directa\nK)Mezcla Natural").upper()
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
    elif opcion == "D":
        var = input(
            "eliga cantidad de numeros para la prueba de estres...\nA)1000\nB)10,000\nC)100,000\nD)Un Millon").upper()
        if var == "A":
            listaAux = listaA.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.insercion(listaAux)
        elif var == "B":
            listaAux = listaB.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.insercion(listaAux)
        elif var == "C":
            listaAux = listaC.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.insercion(listaAux)
        elif var == "D":
            listaAux = listaD.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.insercion(listaAux)
    elif opcion=="E":
        var = input(
            "eliga cantidad de numeros para la prueba de estres...\nA)1000\nB)10,000\nC)100,000\nD)Un Millon").upper()
        if var == "A":
            listaAux = listaA.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.seleccion(listaAux)
        elif var == "B":
            listaAux = listaB.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.seleccion(listaAux)
        elif var == "C":
            listaAux = listaC.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.seleccion(listaAux)
        elif var == "D":
            listaAux = listaD.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.seleccion(listaAux)
    elif opcion == "F":
        var = input(
            "eliga cantidad de numeros para la prueba de estres...\nA)1000\nB)10,000\nC)100,000\nD)Un Millon").upper()
        if var == "A":
            listaAux = listaA.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.shell(listaAux, len(listaAux))
        elif var == "B":
            listaAux = listaB.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.shell(listaAux, len(listaAux))
        elif var == "C":
            listaAux = listaC.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.shell(listaAux, len(listaAux))
        elif var == "D":
            listaAux = listaD.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.shell(listaAux,len(listaAux))
    elif opcion=="G":
        var = input(
            "eliga cantidad de numeros para la prueba de estres...\nA)1000\nB)10,000\nC)100,000\nD)Un Millon").upper()
        if var == "A":
            listaAux = listaA.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.quicksort(listaAux)
        elif var == "B":
            listaAux = listaB.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.quicksort(listaAux)
        elif var == "C":
            listaAux = listaC.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.quicksort(listaAux)
        elif var == "D":
            listaAux = listaD.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.quicksort(listaAux)
    elif opcion=="H":
        var = input(
            "eliga cantidad de numeros para la prueba de estres...\nA)1000\nB)10,000\nC)100,000\nD)Un Millon").upper()
        if var == "A":
            listaAux = listaA.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.radixSort(listaAux, 10)
        elif var == "B":
            listaAux = listaB.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.radixSort(listaAux, 10)
        elif var == "C":
            listaAux = listaC.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.radixSort(listaAux, 10)
        elif var == "D":
            listaAux = listaD.copy()
            print("lista desordenada:")
            print(listaAux)
            print("lista ordenada:")
            obj.radixSort(listaAux,10)
    elif opcion == "I":
        obj.intercalacionArchivos()
    elif opcion == "J":
        listaAux=listaA.copy()
        obj.merge(listaAux)
    elif opcion == "H":
        obj.merge_sort()










