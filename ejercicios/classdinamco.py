class Foo:
    pass

def method_instance(self):
    print(f"Soy un método de instancia en {self}")

def method_class(cls):
    print(f"Soy un método de clase en {cls}")


Foo.method_instance = method_instance
Foo.method_class = classmethod(method_class)


f = Foo()
f.method_instance()  # Soy un método de instancia en <__main__.Foo object at ...>
Foo.method_class()   # Soy un método de clase en <class '__main__.Foo'>
