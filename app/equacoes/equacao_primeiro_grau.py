from flask import abort
from sympy import sympify, symbols

class EquacaoPrimeiroGrau:
    @staticmethod
    def resolver(equacao):
        try:
            expr = sympify(equacao.replace('x', '*x'))
            coeficiente_angular, termo_independente = EquacaoPrimeiroGrau.obter_coeficiente_e_termo(expr)
            raiz = EquacaoPrimeiroGrau.calcular_raiz(coeficiente_angular, termo_independente)
            intersecao_y = EquacaoPrimeiroGrau.calcular_intersecao_y(termo_independente)
            return EquacaoPrimeiroGrau.formatar_resultado(raiz, intersecao_y)
        except ValueError:
            abort(400, "Por favor, certifique-se de que a variável é denotada como 'x'.")


    @staticmethod
    def obter_coeficiente_e_termo(expr):
        x = symbols('x')
        coeficiente_angular = expr.coeff(x)
        termo_independente = expr - coeficiente_angular * x
        return coeficiente_angular, termo_independente

    @staticmethod
    def calcular_raiz(coeficiente_angular, termo_independente):
        return -termo_independente / coeficiente_angular

    @staticmethod
    def calcular_intersecao_y(termo_independente):
        return termo_independente

    @staticmethod
    def formatar_resultado(raiz, intersecao_y):
        return {
            'raiz': {'x': float(raiz), 'y': 0},
            'intersecao_com_eixo_y': {'x': 0, 'y': float(intersecao_y)}
        }