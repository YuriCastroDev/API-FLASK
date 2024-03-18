from flask import Blueprint, request, jsonify
from app.equacoes.equacao_primeiro_grau import EquacaoPrimeiroGrau

primeiro_grau_bp = Blueprint('primeiro_grau', __name__)

@primeiro_grau_bp.route('/equacao/primeiro-grau', methods=['POST'])
def resolver_primeiro_grau():
    equacao = request.json.get('equacao')
    resultado = EquacaoPrimeiroGrau.resolver(equacao)
    return jsonify(resultado)

