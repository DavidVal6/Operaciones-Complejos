import libreriacomplex as ls

def dagger(x):
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
                    m[i][j] = ls.multiplicacioncomplex(v[i][k], w[k][j])
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


def creador_matriz(x, y):
    matriz = []
    for i in range(x):
        a = [0]*y
        matriz.append(a)
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
    m1 = [[(2, 1), (3, 1)], [(2, 2), (2, 1)]]
    m2 = [[(1, 2), (1, 3)], [(2, 2), (1, 2)]]
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
