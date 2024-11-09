"""  
Arquivo com as classes a serem construidas
"""
from enum import Enum

class Loja:
    def __init__(self, localizacao):
        
        self.localizacao = localizacao
        self.funcionarios = [] # A loja agrega os funcionarios
        self.estoque = [] # A loga agrega o estoque
    
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
    
    def adicionar_instrumento(self, instrumento):
        self.estoque.append(instrumento)
    
    def consultar_funcionarios(self):
        return self.funcionarios

class Funcionario:
    def __init__(self, nome_completo, cpf, salario, cargo):
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.salario = salario
        self.loja_atual = None
        self.cargo = cargo # Ver a hierarquia depois 

class Instrumento:
    
    
        