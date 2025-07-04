"""
si no pasas el message por argumento incumples
la D de solid https://es.wikipedia.org/wiki/SOLID
"""
def motor(message):
    def arrancar():
        print(message)
    return {
        "arrancar":arrancar
    }
def coche(motor):
    return {
        "arrancar":motor["arrancar"]
    }
motor_instance = motor("Coche arranco")
coche_instance = coche(motor_instance)
coche_instance["arrancar"]()
