from scipy.optimize import root
from math import sqrt, log

def calcula_fator_friccao(eps, Dh, Re):
    def y(f):
        return (1/(sqrt(f))) + 2 * log((eps / (3.7 * Dh)) + (2.51 / (Re * sqrt(f))), 10)
    return root(y, 0.0002).x[0]

def converter_para_metro(valor):
    return valor/1000
