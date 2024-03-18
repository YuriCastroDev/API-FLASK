from flask import Blueprint, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

docs_bp = Blueprint('docs', __name__)

@docs_bp.route('/swagger.json')
def swagger_json():
    swagger_spec = {
        "swagger": "2.0",
        "info": {
            "title": "API Flask",
            "description": "Documentação da API Flask",
            "version": "1.0.0"
        },
        "tags": [
            {
            "name": "Operações Matemáticas",
            "description": "Endpoints para operações matemáticas"
            },
            {
            "name": "Equação do Primeiro Grau",
            "description": "Endpoint responsável por calcular a equação do primeiro grau"  
            }
        ],
        "paths": {
            "/soma": {
                "post": {
                    "summary": "Realiza uma operação de soma",
                    "tags": ["Operações Matemáticas"],
                    "parameters": [
                        {
                            "name": "num1",
                            "in": "body",
                            "description": "Primeiro número da operação",
                            "required": True,
                            "schema": {"type": "number"}
                        },
                        {
                            "name": "num2",
                            "in": "body",
                            "description": "Segundo número da operação",
                            "required": True,
                            "schema": {"type": "number"}
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Operação realizada com sucesso",
                            "schema": {"type": "object", "properties": {"resultado": {"type": "number"}}}
                        },
                        "400": {"description": "Erro ao processar a operação"}
                    }
                }
            },
            "/subtracao": {
                "post": {
                    "summary": "Realiza uma operação de subtração",
                    "tags": ["Operações Matemáticas"],
                    "parameters": [
                        {
                            "name": "num1",
                            "in": "body",
                            "description": "Primeiro número da operação",
                            "required": True,
                            "schema": {"type": "number"}
                        },
                        {
                            "name": "num2",
                            "in": "body",
                            "description": "Segundo número da operação",
                            "required": True,
                            "schema": {"type": "number"}
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Operação realizada com sucesso",
                            "schema": {"type": "object", "properties": {"resultado": {"type": "number"}}}
                        },
                        "400": {"description": "Erro ao processar a operação"}
                    }
                }
            },
            "/multiplicacao": {
                "post": {
                    "summary": "Realiza uma operação de multiplicação",
                    "tags": ["Operações Matemáticas"],
                    "parameters": [
                        {
                            "name": "num1",
                            "in": "body",
                            "description": "Primeiro número da operação",
                            "required": True,
                            "schema": {"type": "number"}
                        },
                        {
                            "name": "num2",
                            "in": "body",
                            "description": "Segundo número da operação",
                            "required": True,
                            "schema": {"type": "number"}
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Operação realizada com sucesso",
                            "schema": {"type": "object", "properties": {"resultado": {"type": "number"}}}
                        },
                        "400": {"description": "Erro ao processar a operação"}
                    }
                }
            },
            "/divisao": {
                "post": {
                    "summary": "Realiza uma operação de divisão",
                    "tags": ["Operações Matemáticas"],
                    "parameters": [
                        {
                            "name": "num1",
                            "in": "body",
                            "description": "Primeiro número da operação",
                            "required": True,
                            "schema": {"type": "number"}
                        },
                        {
                            "name": "num2",
                            "in": "body",
                            "description": "Segundo número da operação",
                            "required": True,
                            "schema": {"type": "number"}
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Operação realizada com sucesso",
                            "schema": {"type": "object", "properties": {"resultado": {"type": "number"}}}
                        },
                        "400": {"description": "Erro ao processar a operação"}
                    }
                }
            },
            '/equacao/primeiro-grau': {
                'post': {
                    'summary': 'Resolve uma equação de primeiro grau',
                    'tags': ['Equação do Primeiro Grau'],
                    'parameters': [
                        {
                            'name': 'equacao',
                            'in': 'body',
                            'description': 'Equação de primeiro grau no formato "ax + b", onde "a" e "b" são números',
                            'required': True,
                            'schema': {'type': 'string'}
                        }
                    ],
                    'responses': {
                        '200': {
                            'description': 'Equação resolvida com sucesso',
                            'schema': {
                                'type': 'object',
                                'properties': {
                                    'raiz': {'type': 'object', 'properties': {'x': {'type': 'number'}, 'y': {'type': 'number'}}},
                                    'intersecao_com_eixo_y': {'type': 'object', 'properties': {'x': {'type': 'number'}, 'y': {'type': 'number'}}}
                                }
                            }
                        },
                        '400': {'description': 'Erro ao processar a equação'}
                    }
                }
            
    }
        }
    }
    return jsonify(swagger_spec)

# Configuração do Swagger UI
SWAGGER_URL = '/api/docs'
API_URL = '/swagger.json'

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API Flask",
    }
)

# Registrar o blueprint do Swagger UI
docs_bp.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)
