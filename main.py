from flask import Flask, render_template, request, jsonify
from lark import Lark, Tree, Transformer
from graphviz import Digraph
import ply.yacc as yacc
from grammar import parse_expression, lexer
from tree import generate_tree
import simpleeval 
import math

app = Flask(__name__)

SPECIAL_OPERATORS = {'!', '%', 'log', 'π', 'e'}

def evaluate_expression(expression):
    """
    Decide si usar simple_eval o parse_expression en función de la presencia de operadores especiales.
    """
    # Verifica si hay algún operador especial en la expresión
    if any(op in expression for op in SPECIAL_OPERATORS):
        print("Usando parse_expression para analizar la expresión.")
        return evaluate_special_expression(expression)
    else:
        print("Usando simpleeval para analizar la expresión.")
        return simpleeval.simple_eval(expression)
    
def evaluate_special_expression(expression):
    """
    Evalúa expresiones con funciones especiales como factorial, logaritmos, etc.
    
    Args:
        expression (str): Expresión matemática con funciones especiales
    
    Returns:
        float: Resultado de la operación
    """
    # Funciones especiales soportadas
    special_functions = {
        'factorial': math.factorial,
        'log': math.log,
        'log10': math.log10,
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'sqrt': math.sqrt,
        'exp': math.exp,
        'abs': abs
    }
    
    # Limpiar espacios
    expression = expression.strip()

    # Caso para el operador factorial "!"
    if '!' in expression:
        # Buscar el número antes del operador '!'
        num_str = expression[:-1].strip()  # Eliminamos el '!' al final
        try:
            num = int(num_str)
            return math.factorial(num)
        except ValueError:
            print(f"Error: Argumento inválido para factorial en '{expression}'")
            return None
    
    # Caso para el operador de módulo "%"
    if '%' in expression:
        # Separar los dos números por el operador '%'
        parts = expression.split('%')
        if len(parts) == 2:
            try:
                num1 = float(parts[0].strip())
                num2 = float(parts[1].strip())
                return num1 % num2
            except ValueError:
                print(f"Error: Argumento inválido para módulo en '{expression}'")
                return None

    # Caso para la constante 'e'
    if 'e' in expression:
        # Reemplazar 'e' por math.e
        expression = expression.replace('e', str(math.e))
    
    # Caso para logaritmos
    for func_name, func in special_functions.items():
        if expression.startswith(func_name + '(') and expression.endswith(')'):
            # Extraer el argumento dentro de los paréntesis
            arg = expression[len(func_name)+1:-1].strip()
            
            try:
                # Convertir el argumento a número
                numeric_arg = float(arg)
                
                # Calcular y devolver el resultado
                return func(numeric_arg)
            except ValueError:
                print(f"Error: Argumento inválido para {func_name}")
                return None
    
    # Si no se encuentra ninguna función especial
    print("No se reconoce la función especial")
    return None


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    data = request.json
    expression = data.get("expression")

    print(expression)

    try:
        result = evaluate_expression(expression)

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
            "result": result,
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