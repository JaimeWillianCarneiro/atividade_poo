from classes import *

loja_1 = Loja("Botafogo")
print(loja_1)
funcionario_1 = Funcionario(nome_completo="Charli XCX",cpf= 00000000,salario=2400, cargo="Gerente")
print(funcionario_1)
funcionario_1.set_loja(loja_1)
print(funcionario_1)