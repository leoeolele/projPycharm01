import time
import numpy
import pygame


# -- AULA 1

# start_time = time.time()
# lista = [0] * 100
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f'{elapsed_time} seconds')

# -- AULA 2

# CLASSES

# class Dog: # Classe Dog
#     family = 'Canadae' # Atributo da classe
#
#     def __init__(self, age: int): # define função __init__ (construtor), é invocado automaticamente, self para atributos do objeto
#         self._age: int = age # Atributo do objeto, pode explicitar o tipo (Não necessário) para melhor identificação,
#         self.__peso = 0 #_ para sinalizar privado, __ não deve ser acessado fora da classe (solução: get e set)
#
#     def get_age(self) -> int: # pode se definir o dado de retorno
#         return self._age
#
#     def get_peso(self) -> int:
#         return self.__peso
#
#     def set_peso(self, peso: int): # pode se definir o dado de entrada
#         self.__peso = peso

# ----main
# rex = Dog(10) # Instanciar objeto da classe Dog, chamando construtor da classe Dog
# rex.set_peso(45)
# caramelo = Dog(20)
# caramelo.set_peso(30)
# print(f'A idade do rex é: {rex.get_age()} e pertence a familia: {rex.family}')
# print(f'A idade do caramelo é: {caramelo.get_age()}, peso: {caramelo.get_peso()} e pertence a familia: {caramelo.family}')
# print(f'A que familia pertence todos os cachorros: {Dog.family}')
# print(f'Rex é um objeto de qual classe? R: {rex.__class__.__name__}')

# HERANÇA - evita desperdício de código

# class Animal:
#     def __init__(self, age: int, height: int, weight: int, position: tuple):
#         self.age = age
#         self.height = height
#         self.weight = weight
#         self.position: tuple = position  # position [position_x, position_y, position_z], tuplas: vários elementos dentro de uma estrutura que não pode ser alterada
#
#     def move_x(self):
#         self.position[0] += 1
#
#     def move_y(self):
#         self.position[1] += 1
#
#     def move_z(self):
#         self.position[2] += 1
#
#
# class Dog(Animal):  # herda de Animal
#     def __init__(self, age: int, height: int, weight: int, position: tuple):
#         Animal.__init__(self, age, height, weight, position)  # super() = chama classe pai, construtor, e atributos. ou deixe explícito o nome ex: Animal
#
#     def move_z(self):  # Dog pula mais alto, + 2
#         self.position[2] += 2
#
#
# caramelo = Dog(10, 40, 30, (0, 0, 0))
# print(caramelo.age)
