class Persona:

    def init(self, nombre, edad):
        self.edad = edad
        self.nombre = nombre

    def lt(self, any):
        # To do!
        return super().lt(any)

    def str(self):
        return "\tNombre = {}\n\tEdad = {}\n".format(self.nombre, self.edad)

    def repr(self):
        return "Persona({}, {})".format(self.nombre, self.edad)

class Coleccion:

    def init(self, tam, alg):
        self.tam = tam
        self.can = 0
        self.vec = [None]*tam
        self.alg = alg

    def agrega(self, per):
       if self.can < self.tam: 
           self.vec[self.can] = per
           self.can += 1

    def str(self):
       s = "Personas: \n\n"
       for i in range(self.can):
           s += "{}".format(i + 1) + "- " + self.vec[i].str()
       return s

    def ordenar(self):
        alg = alg.ordenar(self.vec)
 
P = Persona("Carlos", 55)
P1 = Persona("Peter", 14)

c = Coleccion(10,0)

c.agrega(P)
c.agrega(P1)

print(c.str())