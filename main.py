"""Compilador incremental: Lexer -> Parser -> AST -> Semántica. Sin TAC ni VM."""
import argparse
from pathlib import Path
from lexer.lexer import Lexer
from parser.parser import Parser
from semantic.analizador import AnalizadorSemantico

BASE_DIR = Path(__file__).resolve().parent

def analizar_lexico(codigo):
    print('\n=== FASE 1 - ANALISIS LEXICO ===')
    tokens = Lexer(codigo).analizar()
    for token in tokens:
        print(' ', token)
    return tokens

def analizar_sintactico(tokens):
    print('\n=== FASE 2 - ANALISIS SINTACTICO ===')
    arbol = Parser(tokens).parsear()
    print('AST generado:')
    print(arbol)
    return arbol

def analizar_semantica(arbol):
    print('\n=== FASE 3 - ANALISIS SEMANTICO ===')
    semantico = AnalizadorSemantico()
    semantico.analizar(arbol)
    print('Analisis semantico correcto.')
    print('Tabla de simbolos:', semantico.tabla_simbolos)
    return semantico

def main():
    argumentos = argparse.ArgumentParser(description='Lexer + Parser + Semantica')
    argumentos.add_argument('archivo', nargs='?', default='pruebas/01_basico_valido.txt',
                            help='Programa fuente que se analizara.')
    argumentos.add_argument('--solo-lexer', action='store_true',
                            help='Ejecutar unicamente el analizador lexico.')
    argumentos.add_argument('--solo-parser', action='store_true',
                            help='Ejecutar lexer + parser, sin semantica.')
    opciones = argumentos.parse_args()
    ruta = Path(opciones.archivo)
    if not ruta.is_absolute() and not ruta.exists():
        ruta = BASE_DIR / ruta
    try:
        codigo = ruta.read_text(encoding='utf-8')
    except OSError as error:
        print(f'No se pudo abrir el archivo: {error}')
        return 1

    print('=== MI COMPILADOR: LEXER + PARSER + SEMANTICA ===')
    print('\nCODIGO FUENTE:')
    print(codigo)
    try:
        tokens = analizar_lexico(codigo)
        if opciones.solo_lexer:
            print('\nEjecucion detenida despues del lexer.')
            return 0
        arbol = analizar_sintactico(tokens)
        if opciones.solo_parser:
            print('\nEjecucion detenida despues del parser.')
            return 0
        analizar_semantica(arbol)
        print('\nLas tres fases finalizaron correctamente.')
        return 0
    except NotImplementedError as error:
        print(f'\n[IMPLEMENTACION PENDIENTE] {error}')
        return 2
    except (RuntimeError, SyntaxError, ValueError, NameError, TypeError) as error:
        print(f'\n{error}')
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
