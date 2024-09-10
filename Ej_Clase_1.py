print("Introduccion a clases")
class animal: 
    edad=23
    raza="chihuahua"
    comida="croquetas"
    def come(self):
        print(f"el perro come " +self.comida)
print(animal)
print("Creando el objeto de la clase animal")
perro = animal()

print(f"Edad del perro: {perro.edad}")
print(f"Raza del perro: {perro.raza}")
perro.come()

