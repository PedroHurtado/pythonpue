"""
Quiero sumar dos numeros con dos invocaciones a funciones, es decir
para obtener el 8 tengo que ejecutar sum(5)(3).
Escribir el código con una función tradicional de python y con lambdas
"""
def sum(a):
    return lambda b:a+b

print(sum(5)(3))
print(sum(5)(100))

result = sum(5)
print(result(3)) #8
print(result(100)) #105

sumlamda = lambda a:lambda b:a+b
print(sumlamda(5)(3))