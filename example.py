"""Arquivos com exemplo de uso das classes criadas"""
from classes import *

loja_1 = Loja("Botafogo")
print(loja_1)
funcionario_1 = Funcionario(nome_completo="Charli XCX",cpf= '00000000',salario=2400, cargo=Cargo.GERENTE)
funcionario_2 = Funcionario(nome_completo="Chappel Roan",cpf='00000001' ,salario= 2300, cargo=Cargo.DIRETOR)
print()
print("Novos funcionários:")
print(funcionario_1)
print(funcionario_2)
print()
print("Atualizando loja que os funcionário trabalham")
loja_1.adicionar_funcionario(funcionario_1)
loja_1.adicionar_funcionario(funcionario_2)

funcionario_1.set_loja(loja_1)
funcionario_2.set_loja(loja_1)
print()
print(funcionario_1)
print(funcionario_2)

print()
print("Consultando funcionários da loja 1")
print()
print(loja_1.consultar_funcionarios())

print("Criando duas novas lojas")
loja_2 = Loja("Flamengo")
loja_3 = Loja("Catete")

#  Adicionando as loja mais perto de cada respectiva loja
loja_1.set_loja_mais_proxima(loja_2)
loja_2.set_loja_mais_proxima(loja_3) #Aqui eu vi que o conceito de loja mais perto não é uma bijeção
loja_3.set_loja_mais_proxima(loja_2)

print()
print("Lojas existentes:")
print()
print(loja_1)
print(loja_2)
print(loja_3)

print()
print("Adiconando novos instrumentos na Loja 1: ")
loja_1.adicionar_instrumento(TipoInstrumento.GUITARRA, marca =  "Fender", modelo="Stratocaster",preco= 500,numero_cordas= 6, tem_ponte_floyd_rose = True)
loja_1.adicionar_instrumento(TipoInstrumento.BAIXO, marca= "Ibanez",modelo= "GSR200", numero_cordas = 4, preco = 800.0, tipo_captacao="Ativo")
loja_1.adicionar_instrumento(TipoInstrumento.VIOLAO, marca = "Yamaha",modelo=  "F310",numero_cordas=6, preco =  300.0, tipo_madeira="Madeira Nobre")
print()
print("Consultando o estoque da loja 1")
print(loja_1.consultar_estoque())

print()
print("Removendo último instrumento adicionado")
loja_1.remover_instrumento()

print()
print("Consultando novamente o estoque da loja 1")
print(loja_1.consultar_estoque())
