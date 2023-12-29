# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self,nome):
        self.nome = nome 
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        return self._motor    
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor
    
    @property
    def fabricante(self):
        return self._fabricante    
    
    @fabricante.setter
    def fabricante(self,valor):
        self._fabricante = valor
        
    
class Motor:
    def __init__(self,motor):
        self.nome = motor
    
class Fabricante:
    def __init__(self,fabricante):
        self.nome = fabricante
    
fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
ford = Fabricante('Ford')
motor_2_0 = Motor('2.0')

print('#####P1########')
print(fusca.nome)
print(volkswagen.nome)
print(motor_1_0.nome)
print('#####P1########')

fusca.fabricante = volkswagen
fusca.motor = motor_1_0

print('#####CARRO 1########')
print(f'Carro: {fusca.nome}, Fabricante:{fusca.fabricante.nome}, Motor:{fusca.motor.nome}')

gol = Carro('Gol')
gol.fabricante = volkswagen
gol.motor = motor_1_0

print('#####CARRO 2########')
print(f'Carro: {gol.nome}, Fabricante:{gol.fabricante.nome}, Motor:{gol.motor.nome}')

focus = Carro('Focus Titanium')
focus.fabricante = ford
focus.motor = motor_2_0

print('#####CARRO 3########')
print(f'Carro: {focus.nome}, Fabricante:{focus.fabricante.nome}, Motor:{focus.motor.nome}')
