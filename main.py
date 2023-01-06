

class Vehículos:
    Color = "rojo"
    Ruedas = 4
    Puertas = 3

class Coche(Vehículos):
    Velocidad = "300 K/H"
    Cilindrada = "V8"


p = Coche
p.Ruedas
p.Color
p.Puertas
p.Velocidad
p.Cilindrada

print("puertas:",p.Ruedas)
print("Color:",p.Color,)
print("Puertas:",p.Puertas)
print("Velocidad:", p.Velocidad)
print("Cilindrada:", p.Cilindrada)