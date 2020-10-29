"""

В этом модуле хранятся вспомогательные функции и данные.

"""
import math

def sum(a,b): return a + b
def sub(a,b): return a - b
def mul(a,b): return a * b
def div(a,b):
	if b != 0: return a / b
	else: return None

def sqrt(a): return math.sqrt(a)
def sin(a): return math.sin(a)
def cos(a): return math.cos(a)
def tg(a): return math.tan(a)
def ctg(a): return math.atan(a)
def sqrt(a): return math.sqrt(a)

binary_operators = {
	'+' : sum,
	'-' : sub,
	'*' : mul,
	'/' : div,
}
actions_dict = {
	'#' : sin,
	'$' : cos,
	'@' : tg,
	'!' : ctg,
	'k' : sqrt,
	
}

def replacer(exp):
	"""
	Заменяет слова-обозначения функций на удобные в обращении символы

	input: str
	output: str

	cos(1) --> $(1)

	"""
	exp = exp.replace('pi', '3.141592653589793').replace('e', '2.718281828459045')
	for symbol, function in actions_dict.items():
		exp = exp.replace(f'{function.__name__}', f'{symbol}', )
		
	return exp



