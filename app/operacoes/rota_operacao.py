from flask import Blueprint, request, jsonify
from app.operacoes.operacao import Operacao

operacao_bp = Blueprint('operacao', __name__)

@operacao_bp.route('/soma', methods=['POST'])
def soma_route():
    return processar_operacao(Operacao.soma)

@operacao_bp.route('/subtracao', methods=['POST'])
def subtracao_route():
    return processar_operacao(Operacao.subtracao)

@operacao_bp.route('/multiplicacao', methods=['POST'])
def multiplicacao_route():
    return processar_operacao(Operacao.multiplicacao)

@operacao_bp.route('/divisao', methods=['POST'])
def divisao_route():
    return processar_operacao(Operacao.divisao)

def processar_operacao(operacao_func):
    if request.method == 'POST':
        data = request.json
        try:
            num1, num2 = Operacao.validar_numeros(data.get('num1'), data.get('num2'))
            resultado = operacao_func(num1, num2)
            return jsonify({'resultado': resultado})
        except ValueError as ve:
            return jsonify({'error': str(ve)}), 400
        except ZeroDivisionError:
            return jsonify({'error': 'Não é possível dividir por zero'}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    else:
        return jsonify({'error': 'Método não permitido'}), 405
