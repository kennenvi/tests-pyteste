from src.bytebank import Funcionario
import pytest
from pytest import mark


# Testes metodologia Given-When-Then (Contexto-Ação-Desfecho)
class TestClass:
    @pytest.fixture
    def funcionario(self):
        return Funcionario('Teste', '13/03/2000', 1000)

    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self, funcionario):
        entrada = '13/03/2000' # Given-contexto
        esperado = 22

        funcionario.data_nascimento = entrada
        resultado = funcionario.idade() # When-ação

        assert resultado == esperado # Then-desfecho
    
    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self, funcionario):
        entrada = ' Lucas Carvalho ' # given
        esperado = 'Carvalho'

        funcionario.nome = entrada
        resultado = funcionario.sobrenome() # when

        assert esperado == resultado # then
    
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self, funcionario):
        entrada_salario = 100000 # given
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario.nome = entrada_nome
        funcionario.salario = entrada_salario
        funcionario.decrescimo_salario() # when
        resultado = funcionario.salario

        assert esperado == resultado # then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self, funcionario):
        entrada = 1000 # given
        esperado = 100

        funcionario.salario = entrada
        resultado = funcionario.calcular_bonus() # when

        assert esperado == resultado # then

    
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self, funcionario):
        with pytest.raises(Exception):
            entrada = 100000000 # given

            funcionario.salario = entrada
            resultado = funcionario.calcular_bonus() # when

            assert resultado # then