# Compilador Entrega Lexer + Parser + Análisis semántico

**Esta es una continuación del mismo compilador incremental.** Ya están resueltos el lexer y el parser del lenguaje base; tu responsabilidad es desarrollar las reglas semánticas en la plantilla y adaptarlas a tu propio lenguaje.

## Qué entrega el catedrático

- `main.py`: conecta las tres fases y permite detenerse tras el lexer o el parser.
- `lexer/token.py` y `lexer/lexer.py`: lexer base completo **como referencia**, NO sustituye la versión personalizada que desarrollaste.
- `parser/parser.py`: parser descendente recursivo **completo para la gramática base**. NO sustituye tu parser personalizado.
- `arbol_ast/nodos.py`: clases AST de la versión base. Conservar los nodos nuevos o adaptados que agregaste.
- `semantic/analizador.py`: clase `AnalizadorSemantico` con **infraestructura resuelta** y 6 métodos `TODO`.
- `pruebas/`: casos correctos y errores léxicos, sintácticos y semánticos; pruebas automáticas para el lenguaje base.
- `GUIA_EXTENSIONES_PERSONALES.md`: orientación para validar semánticamente tus nuevos tokens y construcciones.

## Requisito: conservar el trabajo anterior

**NO reemplaces ni pierdas tu lexer, parser y AST ya desarrollados.** Integra la carpeta `semantic/` y la actualización de `main.py` a **tu repositorio**. Los módulos base incluidos son una referencia para comparar interfaces y comportamiento. Tu código previo debe mantener sus tokens y su sintaxis individual.

Interfaces mínimas: `Lexer(codigo).analizar() -> list[Token]` con EOF; `Parser(tokens).parsear() -> Programa` con nodos AST; `AnalizadorSemantico().analizar(ast)`.

## Los 6 métodos TODO que debes implementar

| Método | Qué valida |
|---|---|
| `visitar_Declaracion()` | Duplicados, tipos de inicialización y registro en tabla de símbolos. |
| `visitar_Asignacion()` | Variable declarada y compatibilidad de tipos. |
| `visitar_Identificador()` | Existencia de variable; devuelve su tipo. |
| `visitar_OpBinaria()` | Tipos de operandos y resultado según el operador. |
| `visitar_Si()` | Condición booleana y recorrido del bloque. |
| `visitar_Mientras()` | Condición booleana y recorrido del bloque. |

Ya resueltos: `__init__()`, `analizar()`, `error_generico()`, `visitar_Programa()`, `visitar_Numero()` y `visitar_Imprimir()`.

## Reglas semánticas del lenguaje base

- Solo hay **declaraciones de tipo `entero`**. Los números literales son `entero`.
- Una variable solo puede declararse una vez en la tabla global.
- No se puede asignar o utilizar una variable no declarada.
- Las expresiones aritméticas `+ - * /` requieren **dos enteros** y devuelven `entero`.
- Las comparaciones `== != < > <= >=` requieren **dos enteros** y devuelven `booleano`.
- Las declaraciones y asignaciones exigen que el tipo de la expresión coincida con el de la variable.
- Las condiciones de `si` y `mientras` deben ser booleanas.
- `imprimir` acepta una expresión semánticamente válida, sin ejecutarla.
- No hay ámbitos locales: se usa una **tabla global**, simplificación intencional de esta entrega.

## Ejecución

```bash
python main.py --solo-lexer
python main.py --solo-parser
python main.py
python main.py pruebas/08_error_variable_no_declarada.txt
python main.py pruebas/11_error_tipo_incompatible.txt
python main.py pruebas/13_valido_relacionales.txt
```

Con `python main.py`, el flujo es: **código → tokens → AST → análisis semántico → tabla de símbolos**.
No se ejecuta el código fuente. **Sin TAC ni máquina virtual.**

En la plantilla inicial, la semántica finaliza con `[IMPLEMENTACION PENDIENTE]` mientras quedan métodos `TODO`. No es un error del lexer ni del parser.

## Pruebas automáticas

```bash
python -m unittest pruebas.test_integracion -v
python -m unittest pruebas.test_semantica -v
python -m unittest discover -s pruebas -p "test_*.py" -v
```

Las primeras pruebas deben pasar con el lenguaje base; las semánticas fallarán parcialmente hasta completar los métodos. **No alteres las pruebas para ocultar fallos.**

## Tu extensión personal, obligatoria

Cada estudiante demostrará al menos **un caso correcto y un caso semánticamente incorrecto** en su propia sintaxis, considerando todos los tokens/construcciones añadidos anteriormente. Explica **qué cambia o por qué no hace falta cambiar** en la semántica. No todos los tokens implican una regla semántica nueva: un comentario descartado por el lexer, por ejemplo, no llega al AST.

Un token adicional en el lexer no implica automáticamente un nuevo `visitar_*`: observa **qué nodo AST produce tu parser**. Si agregaste el nodo `Booleano`, implementa `visitar_Booleano` y devuelve `booleano`; si reutilizaste `OpBinaria` para `%`, amplía `visitar_OpBinaria`.

## Entrega en Google Classroom

Enlace al repositorio de **GitHub**, con su lexer, parser, AST y semántica integrados. Incluye en el `README` cómo ejecutar, pruebas correctas/incorrectas, evidencia de tabla de símbolos y una explicación del tratamiento semántico de la extensión individual. No se requiere TAC, VM ni frontend.
