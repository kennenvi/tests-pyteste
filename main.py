from src.bytebank import Funcionario


def teste_idade():
    funcionario_teste = Funcionario('Teste', '13/10/2000', 1350)
    print(funcionario_teste.idade())

teste_idade()