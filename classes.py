"""  
Arquivo com as classes a serem construidas
"""
from enum import Enum

#  TODO
#  Usar as Hierar
"""  
* Há uma relação de AGREGAÇÃO entre Funcionario e Loja e Funcinario , 
poois pode existir um funcionario independente da sua loja 
"""
class Loja:
    def __init__(self, localizacao):
        
        self.localizacao = localizacao
        self.funcionarios = [] # A loja agrega os funcionarios
        self.estoque = [] 
        self.loja_mais_perto = None
    
    def __str__(self):
        return f"Localização da Loja: {self.localizacao} \nNúmero de funcionários: {len(self.funcionarios)}\n"
    def __repr__(self):
        return f"{self.localizacao}"
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
    
    def remover_funcionario(self):
        #  removendo o último funcionário adicionado
        self.funcionarios.remove(self.consultar_funcionarios[-1])
    
    def adicionar_instrumento(self,  marca, modelo, preco, numero_cordas):
        self.estoque.append(Instrumento(marca, modelo, preco, numero_cordas))
    
    def consultar_funcionarios(self):
        return self.funcionarios
    
    def set_loja_mais_proxima(self, loja_mais_proxima):
        self.loja_mais_perto = loja_mais_proxima.localizacao
        
class Funcionario:
    def __init__(self, nome_completo, cpf, salario, cargo):
        self.nome_completo = nome_completo
        self._cpf = cpf #atributo privado
        self.salario = salario
        self.loja_atual = None
        self.cargo = cargo # Ver a hierarquia depois 
    
    def __str__(self):
        if self.loja_atual:
            return f"Nome completo: {self.nome_completo}, Cargo: {self.cargo}, Loja atual: {self.loja_atual.localizacao}"
        else:
            return f"Nome completo: {self.nome_completo}, Cargo: {self.cargo}"
    def set_loja(self, loja):
        self.loja_atual= loja
    
        

def TipoInstrumento(Enum):
    GUITARRA = "guitarra"
    BAIXO = "baixo"
    VIOLAO = "violão"

class Instrumento:
    # opcoes_instrumentos = list(TipoInstrumento)
    
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
