"""  
Arquivo com as classes a serem construidas
"""
from enum import Enum

"""  
* Há uma relação de AGREGAÇÃO entre Funcionario e Loja e Funcinario , 
pois pode existir um funcionario independente da sua loja 
* Há uma relação de COMPOSIÇÂO entre LOJA e INSTRUMENTO, um instrumento
só existe se estiver associado a uma loja
* Utilizei Herança entre Instrumento e as classes filhas Baixo, Violão e Guitarra 
"""
class TipoInstrumento(Enum):
    GUITARRA = "guitarra"
    BAIXO = "baixo"
    VIOLAO = "violão"


class Loja:
    def __init__(self, localizacao: str):
        
        self.localizacao = localizacao
        self.funcionarios = [] # A loja agrega os funcionarios
        self.estoque = [] 
        self.loja_mais_perto = None
    
    def __str__(self):
        if self.loja_mais_perto:
            return f"Localização da Loja: {self.localizacao} \nNúmero de funcionários: {len(self.funcionarios)}\nLoja mais perto: {self.loja_mais_perto}\n"
        else:
            return f"Localização da Loja: {self.localizacao} \nNúmero de funcionários: {len(self.funcionarios)}\n"
    
    def __repr__(self):
        return f"{self.localizacao}"
    
    def adicionar_funcionario(self, funcionario) -> None:
        self.funcionarios.append(funcionario)
    
    def remover_funcionario(self)-> None:
        #  removendo o último funcionário adicionado
        self.funcionarios.pop(-1)
    
    def adicionar_instrumento(self, tipo_instrumento,  **kwargs)-> None:
        
        instrumento = None
        if tipo_instrumento == TipoInstrumento.GUITARRA:
            instrumento = Guitarra(**kwargs)
        elif tipo_instrumento == TipoInstrumento.BAIXO:
            instrumento = Baixo( **kwargs)
        elif tipo_instrumento == TipoInstrumento.VIOLAO:
            instrumento = Violao(**kwargs )
        
        if instrumento:
            self.estoque.append(instrumento)
    
    
    def remover_instrumento(self)-> None:
        #  removendo o ultimo funcionario
        self.estoque.pop(-1)
    
    def get_estoque(self) -> list:
        return self.estoque
    
    def consultar_estoque(self)-> str:
        estoque_str = "Lista de Instrumentos:\n--------------\n"
        
        for instrumento in self.get_estoque():
            estoque_str += f"{instrumento}\n"
        return estoque_str
     
    def get_funcionarios(self)-> list:
        return self.funcionarios
    
    def consultar_funcionarios(self)-> str:
        funcionarios_str = "Lista de funcionários:\n--------------\n"
        for funcionario in self.get_funcionarios():
            funcionarios_str += f"{funcionario}\n"
        
        return funcionarios_str
    
    def set_loja_mais_proxima(self, loja_mais_proxima)-> None:
        self.loja_mais_perto = loja_mais_proxima.localizacao

class Cargo(Enum):
    ESTAGIARIO = "Estagiário"
    JUNIOR = "Júnior"
    PLENO = "Pleno"
    SENIOR = "Sênior"
    GERENTE = "Gerente"
    DIRETOR = "Diretor"
    
class Funcionario:
    def __init__(self, nome_completo:str, cpf:str, salario:float, cargo: Cargo):
        self.nome_completo = nome_completo
        self._cpf = cpf #atributo privado
        self.salario = salario
        self.loja_atual = None
        self.cargo = cargo 
    
    def __str__(self):
        if self.loja_atual:
            return f"Nome completo: {self.nome_completo}, Cargo: {self.cargo.value}, Loja atual: {self.loja_atual.localizacao}"
        else:
            return f"Nome completo: {self.nome_completo}, Cargo: {self.cargo.value}"
    def __repr__(self):
        if self.loja_atual:
            return f"Nome completo: {self.nome_completo}, Cargo: {self.cargo.value}, Loja atual: {self.loja_atual.localizacao}"
        else:
            return f"Nome completo: {self.nome_completo}, Cargo: {self.cargo.value}"
    
    def set_loja(self, loja)-> None:
        self.loja_atual= loja
    
        

class Instrumento:
    
    def __init__(self, marca, modelo, preco, numero_cordas ):
        self.marca = marca
        self.preco = preco
        self.numero_cordas = numero_cordas
        self.modelo = modelo
    
    def __str__(self):
        return f"Marca: {self.marca}, Número de Cordas: {self.numero_cordas} "
        
class Guitarra(Instrumento):
    
    def __init__(self, marca, modelo, preco, numero_cordas, tem_ponte_floyd_rose):
        super().__init__(marca, modelo, preco, numero_cordas)
        self.tem_ponte_floyd_rose = tem_ponte_floyd_rose

    def __str__(self):
        if self.tem_ponte_floyd_rose:
            return f"Guitarra: {super().__str__()}, Tem Ponte Floyd Rose: SIM"
        else:
            return f"Guitarra: {super().__str__()}, Tem Ponte Floyd Rose: NÃO"
        
    def fazer_solo(self)-> str:
        # Minha criatividade se limita a isso aqui
       
        return f"Executando o solo...\nSolos de guitarra não vão me conquistar..."
    
    
class Violao(Instrumento):
    
    def __init__(self, marca, modelo, preco, numero_cordas, tipo_madeira):
        super().__init__(marca, modelo, preco, numero_cordas)
        self.afinado = False
        self.tipo_madeira = tipo_madeira
    
    def __str__(self):
        return f"Violão: {super().__str__()}, Afinado: {"SIM" if self.afinado else "NÃO"},Tipo de Madeira:  {self.tipo_madeira}"
    
    def afinar(self)->None:
        self.afinado = True
        print("Afinando violão")
    
class Baixo(Instrumento):
    def __init__(self, marca, modelo, preco, numero_cordas, tipo_captacao):
        super().__init__(marca, modelo, preco, numero_cordas)
        self.tipo_captacao = tipo_captacao
        
    def __str__(self):
        return f"Baixo: {super().__str__()},Tipo de Captação: {self.tipo_captacao}"