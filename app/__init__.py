from flask import Flask
from app.rotas.rota import rotas_bp

def create_app():
    app = Flask(__name__)

    # Registrando o blueprint das rotas
    app.register_blueprint(rotas_bp)

    return app

# Executa a aplicação somente se este arquivo for executado diretamente
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
