def add_methods(cls):
    
    def method_instance(self):
        print(f"Soy un método de instancia en {self}")

    
    @classmethod
    def method_class(cls):
        print(f"Soy un método de clase en {cls}")

    
    setattr(cls, 'method_instance', method_instance)
    setattr(cls, 'method_class', method_class)

    return cls


@add_methods
class Foo:
    pass


f = Foo()
f.method_instance()  # método de instancia
Foo.method_class()   # método de clase
f.method_class()     # también funciona desde la instancia
