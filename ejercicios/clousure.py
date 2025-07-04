"""
    Cual es el estado de mi aplicacion?
    Quien son los metodos->sum,mult
"""
class Operaciones:
    def __init__(self,a):
        self._a=a
    def sum(self,b):
        return self._a+b
    def mult(self,b):
        return self._a*b

def OperationsClousure(a):
    def sum(b):
        return a+b
    def mult(b):
        return a*b
    def change_value(value):
        nonlocal a
        a=value

    return {
        "suma":sum,
        "multiplicacion":mult,
        "change":change_value
    }
    
operaciones = Operaciones(5)
operaciones._a = 8   #private y no debes de utilizarlo
print(operaciones.sum(10)) #15
print(operaciones.mult(10)) #50
print("fin")

instance = OperationsClousure(5)
#instance.a=8 encapsulacion
instance["change"](8)
print(instance["suma"](10)) #15
print(instance["multiplicacion"](10)) #50
print("fin clousure")


