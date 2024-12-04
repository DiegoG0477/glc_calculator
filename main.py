from flask import Flask, render_template, request, jsonify
from lark import Lark, Tree, Transformer
from graphviz import Digraph
import ply.yacc as yacc
from grammar import parse_expression, lexer
from tree import generate_tree

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/calcular", methods=["POST"])
# def calcular():
#     data = request.json
#     expression = data.get("expression")

#     try:
#         # Analiza la expresión para generar el árbol
#         tree = parse_expression(expression)

#         # Convierte el árbol en formato JSON
#         tree_json = generate_tree(tree)

#         return jsonify({
#             "valid": True,
#             "tree": tree_json
#         })
#     except Exception as e:
#         return jsonify({
#             "valid": False,
#             "error": str(e)
#         })

@app.route("/calcular", methods=["POST"])
def calcular():
    data = request.json
    expression = data.get("expression")

    print(expression)

    try:
        # Analiza la expresión para generar el árbol
        tree = parse_expression(expression)

        # Convierte el árbol en formato JSON
        tree_json = generate_tree(tree)

        # Genera tokens y frecuencias
        lexer.input(expression)
        token_values = []
        token_frequencies = {}

        for tok in lexer:
            token_values.append((tok.type, tok.value))
            token_frequencies[tok.type] = token_frequencies.get(tok.type, 0) + 1

        print(tree_json)

        return jsonify({
            "valid": True,
            "tree": tree_json,
            "token_values": token_values,
            "token_frequencies": token_frequencies
        })
    except Exception as e:
        return jsonify({
            "valid": False,
            "error": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True)