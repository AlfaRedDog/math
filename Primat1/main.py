import math
#from Aalg import dichotomy
CONST_GOLDEN_RATIO = (1 + math.sqrt(5))/2

def dichotomy(a, b, absac):
    while((b - a) / 2 > absac):
        c = (a + b) / 2
        c1 = c - absac / 2
        c2 = c + absac / 2
        if(function(c1) > function(c2)):
            a = c1
        else:
            b = c2
    return (a + b) / 2
def golden_section(a, b, absac):
    while((b - a) / 2 > absac):
        x1 = b - (b - a) / CONST_GOLDEN_RATIO
        f_x1 = function(x1)
        x2 = a + (b - a) / CONST_GOLDEN_RATIO
        f_x2 = function(x2)
        if (f_x1 >= f_x2):
            a = x1
        else:
            b = x2
    return (a+b)/2
def parabola(a, b, absac):
    prev_x = a
    x1 = a
    x2 = (a+b) / 2
    x3 = b
    f_x1 = function(x1)
    f_x2 = function(x2)
    f_x3 = function(x3)
    while(True):
        if(x3 == x1 or x2 == x1 or x3 == x2):
            return x2
        a1 = (f_x2 - f_x1) / (x2 - x1)
        a2 = ((f_x3 - f_x1) / (x3 - x1) - (f_x2 - f_x1) / (x2 - x1)) / (x3 - x2)
        if(a1 == a2):
            return x2
        x = (x1 + x2 - (a1 / a2)) / 2
        f_x = function(x)
        if(abs(x - prev_x) <= absac):
            return x
        if(x < x2):
            if(f_x >= f_x2):
                x1 = x
                f_x1 = f_x
            else:
                x3 = x2
                f_x3 = f_x2
                x2 = x
                f_x2 = f_x
        else:
            if(f_x >= f_x2):
                x3 = x
                f_x3 = f_x
            else:
                x1 = x2
                f_x1 = f_x2
                x2 = x
                f_x2 = f_x
        prev_x = x
def fibonacci(a, b, absac):
    ch = []
    ch.append(1)
    ch.append(1)
    k = 1
    print(int((b-a)/absac))
    for n in range(1, int((b - a) / absac)):
        ch.append(ch[n] + ch[n-1])
        #print(ch[n])
        k = k + 1
    x1 = a + (ch[k-2] / ch[k]) * (b - a)
    f_x1 = function(x1)
    y1 = a + (ch[k-1] / ch[k]) * (b - a)
    f_y1 = function(y1)
    for i in range(0, k-2):
        if(f_x1 > f_y1):
            a = x1
            x1 = y1
            f_x1 = f_y1
            y1 = a + (ch[k - i - 2] / ch[k - i - 1]) * (b - a)
            f_y1 = function(y1)
        else:
            b = y1
            y1 = x1
            x1 = a + (ch[k - i - 3] / ch[k - i -1]) * (b - a)
            f_x1 = function(x1)
        y1 = x1 + absac
        if(f_x1 == f_y1):
            a = x1
        else:
            b = y1
        return (a + b) / 2


def brent1(a, b, absac):
    x = (a + b) / 2
    w = (a + b) / 2
    v = (a + b) / 2
    f_x = function(x)
    f_w = function(x)
    f_v = function(x)
    d = b - a
    e = b - a
    while (True):
        g = e
        u = -1
        e = d
        if(x != v and x != w and w != v and f_x != f_v and f_x != f_w and f_v != f_w):
            if(w > v):
                a1 = (f_x - f_v) / (x - v)
                a2 = ((f_w - f_v) / (w - v) - (f_x - f_v) / (x - v)) / (w - x)
                u = (v + x - (a1 / a2)) / 2
            else:
                a1 = (f_x - f_w) / (x - w)
                a2 = ((f_v - f_w) / (v - w) - (f_x - f_w) / (x - w)) / (v - x)
                u = (w + x - (a1 / a2)) / 2
        if(u  > a + absac and u < b - absac and abs(u - x) < g / 2):
            d = abs(u-x)
        else:
            if(x < (b - a) / 2):
                u = x + (b - x) / CONST_GOLDEN_RATIO
                d = b - x
            else:
                u = x - (x - a) / CONST_GOLDEN_RATIO
                d = x - a
        if(abs(u - x) < absac):
            return u
        f_u = function(u)
        if(f_u <= f_x):
            if(u >= x):
                a = x
            else:
                b = x
            v = w
            w = x
            x = u
            f_v = f_w
            f_w = f_x
            f_x = f_u
        else:
            if(u >= x):
                b = u
            else:
                a = u
            if(f_u <= f_w  or w == x):
                v = w
                w = u
                f_v = f_w
                f_w = f_u
            else:
                if(f_u <= f_v or v == x or v == w):
                    v = u
                    f_v = f_u






def function(x):
    return math.sin(x) * pow(x, 3)

absac = 10e-10
print(dichotomy(absac, math.pi * 2 - absac, absac))
print(golden_section(absac, math.pi*2 - absac, absac))
print(brent1(absac, math.pi * 2 - absac, absac))
print(parabola(absac, math.pi * 2 - absac, absac))
print(fibonacci(absac, math.pi * 2 - absac, absac))