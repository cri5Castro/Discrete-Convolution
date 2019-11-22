import numpy as np
from collections import OrderedDict
def conv(X,Y):
    conv = OrderedDict()
    center=list(X.keys()).index(0)+list(Y.keys()).index(0)  
    size=len(X.values())+len(Y.values())-1
    for ck in range(-center,size-center):
        r = 0
        for xk,xv in X.items():
            diff = ck-xk
            if diff in Y:
                r += xv*Y[diff]
        conv[ck]=r
    return conv