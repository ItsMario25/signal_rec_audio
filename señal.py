import math    

def umbrales(x):
    M = len(x)
    E = []
    v = int(M/16)
    e1 = 0
    e2 = 0 
    e3 = 0 
    e4 = 0
    e5 = 0
    e6 = 0
    e7 = 0
    e8 = 0
    e9 = 0
    e10 = 0
    e11 = 0
    e12 = 0 
    e13 = 0 
    e14 = 0
    e15 = 0
    e16 = 0
    for i in range (v):
        e1 = e1 + x[i]**2
        e2 = e2 + x[i+v]**2
        e3 = e3 + x[i+2*v]**2
        e4 = e4 + x[i+3*v]**2
        e5 = e5 + x[i+4*v]**2
        e6 = e6 + x[i+5*v]**2
        e7 = e7 + x[i+6*v]**2
        e8 = e8 + x[i+7*v]**2
        e9 = e9 + x[i+8*v]**2
        e10 = e10 + x[i+9*v]**2
        e11 = e11 + x[i+10*v]**2
        e12 = e12 + x[i+11*v]**2
        e13 = e13 + x[i+12*v]**2
        e14 = e14 + x[i+13*v]**2
        e15 = e15 + x[i+14*v]**2
        e16 = e16 + x[i+15*v]**2


    e1 = int(e1/M)
    e2 = int(e2/M)
    e3 = int(e3/M)
    e4 = int(e4/M)
    e5 = int(e5/M)
    e6 = int(e6/M)
    e7 = int(e7/M)
    e8 = int(e8/M)
    e9 = int(e9/M)
    e10 = int(e10/M)
    e11 = int(e11/M)
    e12 = int(e12/M)
    e13 = int(e13/M)
    e14 = int(e14/M)
    e15 = int(e15/M)
    e16 = int(e16/M)
    E.append(e1)
    E.append(e2)
    E.append(e3)
    E.append(e4)
    E.append(e5)
    E.append(e6)
    E.append(e7)
    E.append(e8)
    E.append(e9)
    E.append(e10)
    E.append(e11)
    E.append(e12)
    E.append(e13)
    E.append(e14)
    E.append(e15)
    E.append(e16)
    return E


def fft(X):
    tam = len(X)
    if tam == 2:
        temp1 = X[0] + X[1]
        temp2 = X[0] - X[1]
        X[0] = temp1
        X[1] = temp2
        return X
    else :
        f = []
        g = []
        for i in range(tam):
            if (i+1)%2 == 0:
                f.append(X[i])
            else :
                g.append(X[i])
        g = fft(g)
        f = fft(f)
        k = 0
        for n in range(tam):
            w =  math.cos((2*math.pi*n)/tam) - 1j*math.sin((2*math.pi*n)/tam)
            X[n] = g[k] + f[k] * w
            if k == (tam/2)-1:
                k = 0
            else :
                k = k + 1
        return X
