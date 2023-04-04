class Trie:
	root = None

class TrieNode:
  parent = None
  children = None   
  key = None
  isEndOfWord = False

''' insert(T,element) 
Descripción: insert un elemento en T, siendo T un Trie.
Entrada: El Trie sobre la cual se quiere agregar el elemento (Trie)  y el valor del elemento (palabra) a  agregar.
Salida:  No hay salida definida'''


'''search(T,element)
Descripción: Verifica que un elemento se encuentre dentro del Trie
Entrada: El Trie sobre la cual se quiere buscar el elemento (Trie)  y el valor del elemento (palabra)
Salida: Devuelve False o True  según se encuentre el elemento.
'''

'''delete(T,element)
	Descripción: Elimina un elemento se encuentre dentro del Trie
Entrada: El Trie sobre la cual se quiere eliminar el elemento (Trie)  y el valor del elemento (palabra) a  eliminar.
Salida: Devuelve False o True  según se haya eliminado el elemento.
'''

'''Ejercicio 4
Implementar un algoritmo que dado un árbol Trie T, un patrón p y un entero n, escriba todas las palabras del árbol que empiezan por p y sean de longitud n. 
'''

'''Ejercicio 5
Implementar un algoritmo que dado los Trie T1 y T2 devuelva True si estos pertenecen al mismo documento y False en caso contrario. Se considera que un 
Trie pertenecen al mismo documento cuando:

Ambos Trie sean iguales (esto se debe cumplir)

Si la implementación está basada en LinkedList, considerar el caso donde las palabras hayan sido insertadas en un orden diferente.
En otras palabras, analizar si todas las palabras de T1 se encuentran en T2. 
Analizar el costo computacional.

'''

'''Ejercicio 6
Implemente un algoritmo que dado el Trie T devuelva True si existen en el documento T dos cadenas invertidas. Dos cadenas son invertidas si se leen de izquierda a 
derecha y contiene los mismos caracteres que si se lee de derecha a izquierda, ej: abcd y dcba son cadenas invertidas, gfdsa y asdfg son cadenas invertidas, sin 
embargo abcd y dcka no son invertidas ya que difieren en un carácter.'''

'''Ejercicio 7:
Un corrector ortográfico interactivo utiliza un Trie para representar las palabras de su diccionario. Queremos añadir una función de auto-completar 
(al estilo de la tecla TAB en Linux): cuando estamos a medio escribir una palabra, si sólo existe una forma correcta de continuarla entonces debemos indicarlo. 
Implementar la función autoCompletar(Trie, cadena) dentro del módulo trie.py, que dado el árbol Trie T y la cadena “pal” devuelve la forma de auto-completar 
la palabra. Por ejemplo, para la llamada autoCompletar(T, ‘groen’) devolvería “land”, ya que podemos tener “groenlandia” o “groenlandés” 
(en este ejemplo la palabra groenlandia y groenlandés pertenecen al documento que representa el Trie). Si hay varias formas o ninguna, devolvería la cadena vacía. 
Por ejemplo, autoCompletar(T, ma’) devolvería “” si T presenta las cadenas “madera” y “mama”. 
'''
