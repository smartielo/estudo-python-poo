from abc import ABC, abstractmethod

class figuraGeometrica(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def calcular_area(self):
        pass

class Retangulo(figuraGeometrica):
    def __init__(self, nome, base, altura):
        super().__init__('Retângulo')
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class Quadrado(figuraGeometrica):
    def __init__(self, nome, base, altura):
        super().__init__('Quadrado')
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class Circulo(figuraGeometrica):
    def __init__(self, nome, raio):
        super().__init__('Círculo')
        self.raio = raio

    def calcular_area(self):
        return 3.14 * self.raio ** 2

class Triangulo(figuraGeometrica):
    def __init__(self, nome, base, altura):
        super().__init__('Triângulo')
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura    

figura = figuraGeometrica(
    nome='Retângulo'
)