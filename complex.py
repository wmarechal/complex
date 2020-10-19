import numpy as np

class complexe:
    """
    complex numbers with class
    """

    def __init__(self, r=0.0, i=0.0, module=0.0, phase=0.0):
        if float(r) != 0.0:
            self.real = float(r)
            self.imag = float(i)
            self.module = np.sqrt(self.real**2+self.imag**2)
            self.phase = np.arccos(self.real/self.module)
        if float(module) != 0.0:
            self.module = float(module)
            self.phase = float(phase)
            self.real = module * np.cos(phase)
            self.imag = module * np.sin(phase)

    def __add__(self, other):
        add = complexe(self.real + other.real, self.imag + other.imag)
        return add

    def __sub__(self, other):
        sub = complexe(self.real - other.real, self.imag - other.imag)
        return sub

    def __mul__(self, other):
        if other.__class__ is complexe:
            return complexe(self.real * other.real - self.imag * other.imag,
                            self.imag * other.real + self.real * other.imag)
        elif other.__class__ is float or other.__class__ is int:
            return complexe(self.real * other, self.imag * other)

    def conj(self):
        return complexe(self.real, -self.imag)
    
    def module2(self):
        return (self * self.conj()).real
