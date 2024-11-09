"""  
Arquivo com as classes a serem construidas
"""
from enum import Enum

"""  
* Há uma relação de AGREGAÇÃO entre Funcionario e Loja e Funcinario , 
poois pode existir um funcionario independente da sua loja 
"""
class Loja:
    def __init__(self, localizacao):
        
        self.localizacao = localizacao
        self.funcionarios = [] # A loja agrega os funcionarios
        self.estoque = [] 
    
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
    
    def adicionar_instrumento(self,  marca, modelo, preco, numero_cordas):
        self.estoque.append(Instrumento(marca, modelo, preco, numero_cordas))
    
    def consultar_funcionarios(self):
        return self.funcionarios

class Funcionario:
    def __init__(self, nome_completo, cpf, salario, cargo):
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.salario = salario
        self.loja_atual = None
        self.cargo = cargo # Ver a hierarquia depois 


def TipoInstrumento(Enum):
    GUITARRA = "guitarra"
    BAIXO = "baixo"
    VIOLAO = "violão"

class Instrumento:
    opcoes_instrumentos = list(TipoInstrumento)
    
    def __init__(self, marca, modelo, preco, numero_cordas ):
        self.marca
        self.preco
        self.numero_cordas
        self.modelo
        
class Guitarra(Instrumento):
    
    def __init__(self, marca, modelo, preco, numero_cordas):
        super().__init__(marca, modelo, preco, numero_cordas)

    def fazer_solo(self):
        print("Executando o solo...")
        print("Solos de guitarra não vão me conquistar...")
    
    
class Violao(Instrumento):
    
    def __init__(self, marca, modelo, preco, numero_cordas):
        super().__init__(marca, modelo, preco, numero_cordas)
        self.afinado = False
    
    def afinar(self):
        self.afinado = True
        print("Afinando violão")
    
class Baixo(Instrumento):
    def __init__(self, marca, modelo, preco, numero_cordas):
        super().__init__(marca, modelo, preco, numero_cordas)
    


info_violao = ['marca': ]
violao_1 = Instrumento()