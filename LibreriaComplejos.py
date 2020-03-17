from sys import stdin

#---------------------------NUMEROS COMPLEJOS-----------------------------------#

def sumacomplex(z1,z2):
    a=z1[0]+z2[0]
    b=z1[1]+z2[1]
    c=a,b
    #print("("+str(c[0])+","+str(c[1])+"i"+")")
    return c
 
def restacomplex(z1,z2):
    a=z1[0]-z2[0]
    b=z1[1]-z2[1]
    c=a,b
    return c

def multicomplex(z1,z2):
    a=z1[0]*z2[0]-z1[1]*z2[1]
    b=z1[0]*z2[1]+z1[1]*z2[0]
    c=(round(a,3)),(round(b,3))
    return c

def divcomplex(z1,z2):
    a=(z1[0]*z2[0]+z1[1]*z2[1])/(z2[0]**2+z2[1]**2)
    b=(z1[1]*z2[0]-z1[0]*z2[1])/(z2[0]**2+z2[1]**2)
    c=a,b
    return c

def modcomplex(z1):
    c=(z1[0]**2+z1[1]**2)**(1/2)
    return c

def conjcomplex(z1):
    c=z1[0],z1[1]*(-1)
    return c

import math

def polarcomplex(z1):
    c=modcomplex(z1),math.atan2(z1[1]/z1[0],z1[1]/z1[0])
    return c


#---------------------------VECTORES COMPLEJOS-----------------------------------#

def sumavector(v1,v2):
    c=[]
    for i in range(len(v1)):
        a=sumacomplex(v1[i],v2[i])
        c.append(a)
    return c

def sumamatriz(v1,v2):
    c=[]
    for i in range(len(v1)):
        c.append([])
        for j in range(len(v1)):
            a=sumacomplex(v1[i][j],v2[i][j])
            c[i].append(a)
    return c

def inversovector(v1):
    c=[]
    for i in range(len(v1)):
        c.append((v1[i][0]*(-1),v1[i][1]*(-1)))
    return c

def multescalarvector(z1,v1):
    c=[]
    for i in range(len(v1)):
        c.append(multicomplex(z1,v1[i]))
    return c
##    c=m1
##    m2=multescalarmatrices((-1,0),m2)
##    c=adicionmatrices(m1,m2)
##    norma(c) #Toca hacer la multiplicacion de matrices

##def innervector(v1,v2):
##    s = multicomplex(v1[0],v2[0])
##    for i in range(1, len(v1)):
##        s  = sumacomplex(s,multicomplex(v1[i],v2[i]))
##    return s

def innervector(v1, v2):
    r = [0,0]
    v= conjugadavector(v1)
    for j in range(len(v2)):
        r = sumacomplex(r, multicomplex(v2[j], v[j]))

    return r


def conjugadavector(v1):
    c = []
    for i in range (len(v1)):
        c.append(conjcomplex(v1[i]))
    return c

def Vectorsproductotensor(m1,m2):
    c=[]
    for j in range(len(m1)):
        res=multescalarvector(m1[j],m2)
        for k in range(len(res)):
            c.append(res[k])
    return c      
    
##def distanciamatrices(m1,m2):
##    c=m1
##    m2=multescalarmatrices((-1,0),m2)
##    c=adicionmatrices(m1,m2)
##    norma(c) #Toca hacer la multiplicacion de matrices

#---------------------------MATRICES COMPLEJAS-----------------------------------#

def adicionmatrices(m1,m2):
    c=[]
    for i in range(len(m1)):
        c.append([])
        for j in range(len(m1[0])):
            a=sumacomplex(m1[i][j],m2[i][j])
            c[i].append(a)
    return c

def inversamatriz(m1):
    c=[]
    for i in range(len(m1)):
        c.append(inversovector(m1[i]))
    return c

def multescalarmatrices(z1,m1):
    c=[]
    for i in range(len(m1)):
        c.append(multescalarvector(z1,m1[i]))
    return c

def matriztranspuesta(m1):
    c=[]
    for i in range(len(m1)):
        c.append([])
        for j in range(len(m1[0])):
            c[i].append(m1[j][i])
    return c 

def conjmatriz(m1):
    c=[]
    for i in range(len(m1)):
        c.append([])
        for j in range(len(m1[0])):
            c[i].append(conjcomplex(m1[j][i]))
    return c

def adjmatriz(m1):
    return conjmatriz(matriztranspuesta(m1))
 
def innermatrix(m1,m2):
    inner = []
    trace = []
    
    inner.append
    for i in range(0, len(m1)):
       
        for j in range (0,len(m1)):
            
            inner.append(multicomplex(m1[i][j],m2[j][i]))
        trace.append(sumacompvector(inner))
    return sumacompvector(trace)

def matrizmult(m1, m2):
    
    f2 = len(m2)
    c1 = len(m1[0])
    
    if f2 == c1:
        f = len(m1)
        c = len(m2[0])
        m0 = [[(0, 0)] * c for x in range(f)]
        
        for i in range(0,f):
            for j in range(0,c):
                for k in range(0, len(m2)):
                    m = multicomplex(m1[i][k], m2[k][j])
                    n = m0[i][j]
                    m0[i][j] = (m[0]+n[0], m[1]+n[1])
    return m0

def matrizdis(m1,m2):
    res = 0
    for i in range (len(m1)):
        for j in range(len(m1[i])):
            v = restacomplex(m1[i][j],m2[i][j])
            res += v[0] **2 + v[1]**2
    c = res ** 0.5
    return c

def identidadmatriz(filas,columnas):
    c = [] # Matriz
    for i in range(filas):
        fila = []
        for j in range(columnas):
            val = 1 if i==j else 0
            fila.append(val)
        c.append(fila)
     
    return(c)
    
def isUnitaria(m1):
    
    f = len(m1)
    c = len(m1[0])
    
    if f == c:
        t = matriztranspuesta(m1)
        m1 = matrizmult(m1,t)
        iden = identidadmatriz(f,c)

        if m1 == iden:
            return True
        
        else:
            return False

        return False

def isHermitania(m1):
    if m1 == matriztranspuesta(adjmatriz(m1)):
        return True
    else:
        return False


#-----------------------ACCION DE UNA MATRIZ SOBRE UN VECTOR-----------------------------------#
       
def sumacompvector(v1):
    if len(v1) < 2 :
        return v1[0]
    elif len(v1) == 2:
        s = sumacomplex(v1[0],v1[1])
        return s
    else:
        s = sumacomplex(v1[0],v1[1])
        for i in range (2,len(v1)):
            s = sumacomplex(s,v1[i])
        return s
    
def accionmatrizvector(m1,v1):
    c = []
    d = []
    for i in range (len(m1)):
        c.append([])
        for j in range (len(m1)):
            c[i].append(multicomplex(m1[i][j],v1[j]))
    for i in range (len(c)):
        d.append(sumacompvector(c[i]))        
    return d

#-------------------------OPERACIONES MIXTAS-------------------------------------#
def norma(m1):
    a=innervector(m1,m1)
    return a[0]**0.5

def productotensor(m1,m2):
    res = []
    control = 0
    pj = 0
    for pi in range((len(m1)-1)*2):
        f1 = m1[pi]
        f2 = m2[pj]
        f = []        
        for i in f1:
            for j in f2:
                f.append(multicomplex(i,j))        
        pj += 1
        f2 = m2[pj]
        res.append(f)
        f = []        
        for i in f1:
            for j in f2:
                f.append(multicomplex(i,j))                
        pj -= 1
        res.append(f)
   
    return res

#-------------------------CIRCUITO SIMULACION-------------------------------------#
def simulacion_OO_HH_HX():
    H=[[(0.707,0),(0.707,0)],[(0.707,0),(-0.707,0)]]
    X=[[(0,0),(1,0)],[(0,0),(1,0)]]
    O=[(1,0),(0,0)]

    print("HH")
    HH=productotensor(H,H)
    for i in HH:
        print(i)
    print()
    print("HX")
    HX=productotensor(H,X)
    for i in HX:
        print(i)
    print()
    print("|O>*|O>")
    OO=Vectorsproductotensor(O,O)
    for i in OO:
        print(i)
    print()
    print("HX*HH")
    HHHX=matrizmult(HX,HH)
    for i in HHHX:
        print(i)
    print()
    print("|y>")
    Y=accionmatrizvector(HHHX,OO)
    for i in Y:
        print(i)

##def main():
##    m1=[[(1,0),(0,1)],[(0,-1),(1,0)]] 
##    print(isHermitania(m1))
####
##main()


##    m1=[[(3,2),(3,1)],[(0,2),(1,2)]]
##    for i in range(len(m1)):
##        print(m1[i])
##    print(".")
##    for j in range(len(m1)):
##        print(matriztranspuesta(m1)[j])
##    m1=[[(3,2),(3,1)],[(0,2),(1,2)]] m2=[[(1,3),(0,2)],[(1,1),(1,0)]]
##    print(adicionmatrices(m1,m2)) z1=(3,2)
##    v1=[(6,3),(0,0),(5,1),(4,0)]
##    print(multescalar(z1,v1))
##    v1=[(6,-4),(7,3),(4.2,-8.1),(0,-3)]
##    v2=[(16,2.3),(0,-7),(6,0),(0,-4)] print(sumavector(v1,v2))
##    z1=(0,-3) z2=(3,-10) pP("Suma",sumacomplex(z1,z2))
##    pP("Resta",restacomplex(z1,z2))
##    pP("Multiplicacion",multicomplex(z1,z2))
##    pP("Division",divcomplex(z1,z2)) print("Modulo
##    "+str(modcomplex(z1))) pP("Conjugada",conjcomplex(z1))
##    pP("Cartesiano a Polar",polarcomplex(z1))
