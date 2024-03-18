class Operacao:
    @staticmethod
    def soma(num1, num2):
        return num1 + num2

    @staticmethod
    def subtracao(num1, num2):
        return num1 - num2

    @staticmethod
    def multiplicacao(num1, num2):
        return num1 * num2

    @staticmethod
    def divisao(num1, num2):
        if num2 == 0:
            raise ValueError("Não é possível dividir por zero")
        return num1 / num2

    @staticmethod
    def validar_numeros(num1, num2):
        try:
            num1 = float(num1)
            num2 = float(num2)
            if num1 is None or num2 is None:
                raise ValueError('Por favor, forneça dois números')
            return num1, num2
        except ValueError:
            raise ValueError('Os números fornecidos são inválidos')
