"""Fase 3: analizador semántico (PLANTILLA PARA ESTUDIANTES).

El lexer y el parser ya funcionan. En esta fase se recorre el AST.
`analizar(nodo)` despacha al método `visitar_NombreDelNodo`.
Las expresiones devuelven su tipo ('entero' o 'booleano');
las sentencias normalmente devuelven None.

Tabla de símbolos: diccionario {nombre_variable: tipo}.
Ámbito simplificado de esta etapa: una única tabla GLOBAL.
No implementamos alcances locales, ejecución, TAC ni VM.
"""
from typing import Dict, Optional
from arbol_ast.nodos import (
    NodoAST, Programa, Declaracion, Asignacion, Numero, Identificador,
    OpBinaria, Imprimir, Si, Mientras,
)

class AnalizadorSemantico:
    def __init__(self):
        # YA IMPLEMENTADO. Ejemplo: {'edad': 'entero'}.
        self.tabla_simbolos: Dict[str, str] = {}

    def analizar(self, nodo: NodoAST) -> Optional[str]:
        # YA IMPLEMENTADO: patrón Visitor (recorrido del AST).
        metodo = f'visitar_{type(nodo).__name__}'
        visitante = getattr(self, metodo, self.error_generico)
        return visitante(nodo)

    def error_generico(self, nodo: NodoAST):
        # Es intencional: nuevas clases AST requieren un visitante propio.
        raise NotImplementedError(
            f'Falta soporte semantico para el nodo {type(nodo).__name__}. '
            'Si agregaste nodos AST por tus tokens propios, implementa su visitante.'
        )

    def visitar_Programa(self, nodo: Programa) -> None:
        # YA IMPLEMENTADO: analizar cada sentencia en orden.
        for sentencia in nodo.sentencias:
            self.analizar(sentencia)

    def visitar_Numero(self, nodo: Numero) -> str:
        # YA IMPLEMENTADO: en el lenguaje base, los NUMERO son enteros.
        return 'entero'

    def visitar_Imprimir(self, nodo: Imprimir) -> None:
        # YA IMPLEMENTADO: imprimir acepta expresiones válidas.
        # Debe analizar su expresión para descubrir identificadores inexistentes.
        self.analizar(nodo.expr)

    def visitar_Declaracion(self, nodo: Declaracion) -> None:
        # TODO 1: variable duplicada, analizar expresion, validar tipo,
        # finalmente registrar en tabla_simbolos. No registrar primero:
        # 'entero x = x + 1;' debe detectar que x aún no existe.
        raise NotImplementedError('TODO 1: visitar_Declaracion')

    def visitar_Asignacion(self, nodo: Asignacion) -> None:
        # TODO 2: verificar que el identificador exista y comparar
        # el tipo de la expresion con el tipo guardado de la variable.
        raise NotImplementedError('TODO 2: visitar_Asignacion')

    def visitar_Identificador(self, nodo: Identificador) -> str:
        # TODO 3: si el nombre no existe, lanzar NameError con linea.
        # Si existe, devolver su tipo desde tabla_simbolos.
        raise NotImplementedError('TODO 3: visitar_Identificador')

    def visitar_OpBinaria(self, nodo: OpBinaria) -> str:
        # TODO 4: analizar ambos operandos y comprobar compatibilidad.
        # + - * / -> requieren entero y devuelven entero.
        # == != < > <= >= -> requieren entero y devuelven booleano.
        # Para una operacion no conocida, lanzar error explicito.
        # Si el estudiante creo otros operadores debe extender esto.
        raise NotImplementedError('TODO 4: visitar_OpBinaria')

    def visitar_Si(self, nodo: Si) -> None:
        # TODO 5: la condicion debe ser 'booleano'. Luego visitar
        # cada sentencia del bloque verdadero.
        raise NotImplementedError('TODO 5: visitar_Si')

    def visitar_Mientras(self, nodo: Mientras) -> None:
        # TODO 6: la condicion debe ser 'booleano'. Luego visitar
        # cada sentencia del bloque (sin ejecutar el ciclo).
        raise NotImplementedError('TODO 6: visitar_Mientras')
