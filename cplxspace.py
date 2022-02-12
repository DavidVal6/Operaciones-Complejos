import math

import libreriacomplex as ls

def unitaria(m1):
    identi = identidad(filas(m1))
    procedimiento = multplimtrx(m1, dagger(m1))
    if procedimiento == identidad:
        return True



def product_tensor(m1,m2):
    m = filas(m1)
    m_p = columnas(m1)
    n = filas(m2)
    n_p = columnas(m2)
    t1 = m * n
    t2 = m_p * n_p
    tensor = creador_matriz(t1, t2)
    for i in range(t1):
        for j in range(t2):
            tensor[i][j] = ls.multiplicacioncomplex(m1[i//n][j//n_p], m2[i % n][j % n_p])
    return tensor

def distancia(v1,v2):

    dista = norma(restavectores(v1, v2))
    return dista


def norma(vector):
    solu = 0
    solu = producto_interno(vector, vector)
    final = (solu[0]+solu[1])**(1/2)
    return final


def producto_interno(v1, v2):
    """"C : V1 X V2 -> R"""
    solucion = (0, 0)
    for i,j in zip(v1, v2):
        solucion = ls.sumacomplejos(solucion, ls.multiplicacioncomplex(i, j))
    return solucion



def hermitania_verificador(m1):
    matriz = dagger(m1)
    if matriz == m1:
        return True


def trace(m1):
    operacion = (0, 0)
    for i in range(filas(m1)):
        operacion = ls.sumacomplejos(operacion, m1[i][i])
    return operacion


def dagger(x): #adjunta
    matrix = traspuestamtrx(x)
    matrix = conjugadamtrx(matrix)
    return matrix

def conjugada_vector(v):
    tama = len(v)
    conjugada = [(0, 0) for i in range(tama)]
    j = 0
    while j < tama:
        conjugada[j] = ls.conjugado(v[j])
        j += 1
    return conjugada


def conjugadamtrx(v):
    m = creador_matriz(filas(v), columnas(v))
    for i in range(filas(v)):
        for j in range(columnas(v)):
            m[i][j] = ls.conjugado(v[i][j])
    return m
def mtrxescalar(c, v):
    m = creador_matriz(filas(v),columnas(v))
    for i in range(filas(v)):
        for j in range(columnas(v)):
            m[i][j] = ls.multiplicacioncomplex(c , v[i][j])
    return m


def multplimtrx(v, w):
    if columnas(v) == filas(w):
        m = creador_matriz(filas(v), columnas(w))
        for i in range(filas(m)):
            for j in range(columnas(m)):
                for k in range(columnas(v)):
                    m[i][j] = ls.sumacomplejos(m[i][j], ls.multiplicacioncomplex(v[i][k], w[k][j]))
        return m

def invermtrx(v):
   return (mtrxescalar(((-1,0)), v))

def traspuestamtrx(x):
    m = filas(x)
    n = columnas(x)
    t = creador_matriz(m, n)
    for i in range(n):
        for j in range(m):
            t[i][j] = x[j][i]
    return t

def identidad(x):
    m = creador_matriz(x, x)
    for i in range(filas(m)):
        m[i][i] = (1, 0)
    return m


def creador_matriz(x, y):
    matriz = []
    for i in range(x):
        matriz.append([])
        for j in range(y):
            matriz[i].append((0, 0))
    return matriz


def filas(v):
    return len(v)


def columnas(v):
    return len(v[0])


def sumamatrx(v, w):
    if filas(v) == filas(w) and columnas(v) == columnas(w):
        c = creador_matriz(filas(v), columnas(v))
        for i in range(filas(v)):
            for j in range(columnas(v)):
                c[i][j] = ls.sumacomplejos(v[i][j], w[i][j])
        return c


def inversoaditiv(v):
    tama = len(v)
    inverso = [(0, 0) for i in range(tama)]
    j = 0
    while j < tama:
        inverso[j] = ls.multiplicacioncomplex((-1, 0), v[j])
        j += 1
    return inverso

def restavectores(v,w):
    tama = len(v)
    resta =[(0, 0) for i in range(tama)]
    j = 0
    while j < tama:
        resta[j] = ls.restacplx(v[j], w[j])
        j += 1
    return resta


def sumavectores(v, w):
    tama = len(v)
    suma = [(0, 0) for i in range(tama)]
    j = 0
    while j < tama:
        suma[j] = ls.sumacomplejos(v[j], w[j])
        j = j + 1
    return suma


def multescalar(c, v):
    tama = len(v)
    mult = [(0, 0) for i in range(tama)]
    j = 0
    while j < tama:
        mult[j] = ls.multiplicacioncomplex(c, v[j])
        j += 1
    return mult


if __name__ == '__main__':
    v = [(3, 7), (8, 9), (3.4, -7.8)]
    w = [(5, 6), (6, 8), (0, 0)]
    herni = [[(5, 0), (4, 5), (6, -16)], [(4, -5), (13, 0), (7, 0)], [(6, 16), (7, 0), (-2.1, 0)]]
    m1 = [[(2, 1), (3, 1)], [(2, 2), (2, 1)]]
    m2 = [[(1, 2), (1, 3)], [(2, 2), (1, 2)]]

    """Zonas de print"""

    if unitaria(m1):
        print('UNITARIA')
    else:
        print('NO UNITARIA')

    if hermitania_verificador(herni):
        print("HERMITANIA")
    else:
        print("NO HERMITANIA")
    print(product_tensor(m1,m2))
    print(distancia(v,w))
    print(norma(v))
    print(producto_interno([(3,0),(-1,0),(0,0)],[(2,0),(-2,0),(1,0)]))
    print(trace(m1))
    print(dagger(m1))
    print(conjugada_vector(v))
    print(conjugadamtrx(m1))
    print(invermtrx(m1))
    print(mtrxescalar((2,3), m1))
    print(multplimtrx(m1, m2))
    print(traspuestamtrx(m1))
    print(sumamatrx(m1, m2))
    print(inversoaditiv(v))
    print(sumavectores(v, w))
    print(multescalar((2, 3), w))
