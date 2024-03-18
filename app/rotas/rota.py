from flask import Blueprint
from app.operacoes.rota_operacao import operacao_bp
from app.docs.docs import docs_bp
from app.equacoes.rota_primeiro_grau import primeiro_grau_bp

rotas_bp = Blueprint('rotas', __name__)

rotas_bp.register_blueprint(operacao_bp)

rotas_bp.register_blueprint(docs_bp)

rotas_bp.register_blueprint(primeiro_grau_bp)

