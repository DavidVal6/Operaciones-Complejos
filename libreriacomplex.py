import math



def cartesianas(c1):
    r = modulo(c1)
    real = r*math.cos(fase(c1))
    imaginaria = r*math.sin(fase(c1))
    return real, imaginaria


def fase(c1):
    angulo = math.atan(c1[1]/c1[0])  # Este resulatado sera en radianes
    return angulo


def restacplx(c1, c2):
    return c1[0]-c2[0], c1[1]-c2[1]


def conjugado(c1):
    return c1[0], -c1[1]


def modulo(c1):
    modulo_c = ((c1[0]**2)+(c1[1]**2))**(1/2)
    return modulo_c


def divisioncplx(c1, c2):
    p_real = ((c1[0]*c2[0])+(c1[1]*c2[1]))/((c2[0]**2)+(c2[1]**2))
    p_imaginaria = ((c2[0]*c1[1])-(c1[0]*c2[1]))//((c2[0]**2)+(c2[1]**2))
    return p_real, p_imaginaria


def multiplicacioncomplex(c1, c2):
    parte_real = ((c1[0]*c2[0])-(c1[1]*c2[1]))
    parte_imaginaria = (c1[0]*c2[1])+(c1[1]*c2[0])
    return parte_real, parte_imaginaria

def restacomplejos(c1, c2):
    return c1[0] - c2[0], c1[1] - c2[1]

def sumacomplejos(c1, c2):
    return c1[0]+c2[0], c1[1]+c2[1]


if __name__ == '__main__':
    print(sumacomplejos((3, 2), (4, 8)))  # el resultado de esta operacion debe de ser : 7 + 10i
    print(multiplicacioncomplex((3, 4), (5, 2)))  # el resultado de etsa operacion debe de ser  :
    print(divisioncplx((-2, 1), (1, 2)))  # el resultaod de la operacion es : i
    print(modulo((2, 1)))  # el resultado de la operacion es : sqrt(5)
    print(conjugado((2, 1)))  # el resultado es : 2 - i
    print(restacplx((3, 1), (2, -1)))
    print(math.degrees(fase((1, 2))))
    print( cartesianas((1, 2)))
#
