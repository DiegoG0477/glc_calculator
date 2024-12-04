import ply.lex as lex
import ply.yacc as yacc

# Tokens
tokens = (
    'DECIMAL',
    'ENTERO',
    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'PAREN_IZQ',
    'PAREN_DER',
)

# Expresiones regulares para tokens
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_PAREN_IZQ = r'\('
t_PAREN_DER = r'\)'

# Manejo de números decimales
def t_DECIMAL(t):
    r'\d*\.\d+'
    t.value = float(t.value)
    return t

# Manejo de enteros
def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios y tabs
t_ignore = ' \t'

# Manejo de errores léxicos
def t_error(t):
    print(f"Caracter ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Construcción del analizador léxico
lexer = lex.lex()

def p_S(p):
    '''S : E'''
    # S apunta a E
    #p[0] = {"S": p[1]}
    p[0] = p[1]

def p_E_plus(p):
    '''E : E SUMA T'''
    # Nodo E con hijos E, SUMA y T
    p[0] = {"E": [p[1], "+", p[3]]}

def p_E_minus(p):
    '''E : E RESTA T'''
    # Nodo E con hijos E, RESTA y T
    p[0] = {"E": [p[1], "-", p[3]]}

def p_E_term(p):
    '''E : T'''
    # Nodo E apuntando a T
    p[0] = {"E": p[1]}

def p_T_mul(p):
    '''T : T MULT F'''
    # Nodo T con hijos T, MULT y F
    p[0] = {"T": [p[1], "*", p[3]]}

def p_T_div(p):
    '''T : T DIV F'''
    # Nodo T con hijos T, DIV y F
    p[0] = {"T": [p[1], "/", p[3]]}

def p_T_factor(p):
    '''T : F'''
    # Nodo T apuntando a F
    p[0] = {"T": p[1]}

def p_F_group(p):
    '''F : PAREN_IZQ E PAREN_DER'''
    # Nodo F con hijos (, E, )
    p[0] = {"F": ["(", p[2], ")"]}

def p_F_number(p):
    '''F : N'''
    # Nodo F apuntando a N
    p[0] = {"F": p[1]}

def p_N_decimal(p):
    '''N : DECIMAL'''
    # Nodo N apuntando al número decimal
    p[0] = {"N": str(p[1])}

def p_N_integer(p):
    '''N : ENTERO'''
    # Nodo N apuntando al número entero
    p[0] = {"N": str(p[1])}

def p_error(p):
    print(f"Error de sintaxis en '{p.value}'" if p else "Error de sintaxis")

# Construcción del analizador sintáctico
parser = yacc.yacc()

# Función para analizar expresiones
def parse_expression(expression):
    return parser.parse(expression, lexer=lexer)
