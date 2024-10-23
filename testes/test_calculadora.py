from unittest import TestCase
import negocio.calculadora

class TestesDaCalculadora(TestCase):

    def test_calculo_guardado_6000_custo_1000_retorna_6_meses(self):
        valor_guardado = 6000
        custo_mensal = 1000
        qtd_de_meses_esperada = 6

        qtd_de_meses_calculada = negocio.calculadora.calcular(valor_guardado, custo_mensal)

        self.assertEqual(qtd_de_meses_calculada, qtd_de_meses_esperada)

    def test_calculo_guardado_10000_custo_2000_retorna_5_meses(self):
        valor_guardado = 10000
        custo_mensal = 2000
        qtd_de_meses_esperada = 5

        qtd_de_meses_calculada = negocio.calculadora.calcular(valor_guardado, custo_mensal)

        self.assertEqual(qtd_de_meses_calculada, qtd_de_meses_esperada)

    def test_calculo_guardado_50000_custo_5000_retorna_10_meses(self):
        valor_guardado = 50000
        custo_mensal = 5000
        qtd_de_meses_esperada = 10

        qtd_de_meses_calculada = negocio.calculadora.calcular(valor_guardado, custo_mensal)

        self.assertEqual(qtd_de_meses_calculada, qtd_de_meses_esperada)

    def test_calculo_guardado_27000_custo_3800_retorna7_meses(self):
        valor_guardado = 27000
        custo_mensal = 3800
        qtd_de_meses_esperada = 7

        qtd_de_meses_calculada = negocio.calculadora.calcular(valor_guardado, custo_mensal)

        self.assertEqual(qtd_de_meses_calculada, qtd_de_meses_esperada)

    def test_calculo_guardado_negativo_retorna_0(self):
        valor_guardado = -10000
        custo_mensal = 1000
        qtd_de_meses_esperada = 0

        qtd_de_meses_calculada = negocio.calculadora.calcular(valor_guardado, custo_mensal)

        self.assertEqual(qtd_de_meses_calculada, qtd_de_meses_esperada)

    def test_calculo_custo_negativo_retorna_0(self):
        valor_guardado = 10000
        custo_mensal = -1000
        qtd_de_meses_esperada = 0

        qtd_de_meses_calculada = negocio.calculadora.calcular(valor_guardado, custo_mensal)

        self.assertEqual(qtd_de_meses_calculada, qtd_de_meses_esperada)

    