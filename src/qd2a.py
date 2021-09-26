import random

from tc.glc import GLC

# Implementação da definição formal da gramática

V = {'S'}
T = {'o','v'}
P = {
  ('S', ()),
  ('S', ('o')),
  ('S', ('v')),
  ('S', ('o','S','o')),
  ('S', ('v','S','v')),
}

gramatica = GLC(V, T, P, 'S')

# INICIO DO ESTUDO

# PEGANDO UMA LETRA ALEATÓRIOA
def letra_aleatoria(gramatica: 'GLC'):
  """
  Função que pega uma letra aleatória de uma gramática
  """
  terminais = list(gramatica.terminais)
  letra = random.choice(terminais)
  return letra


# PEGANDO UM PALINDROMO ALEATÓRIO
def palindromo_aleatorio(gramatica: 'GLC', tamanho: int):
  """
  Função que pega um palíndromo aleatórios de uma gramática
  """
  palindromo = ''
  for i in range(tamanho):
    palindromo += letra_aleatoria(gramatica)
  palindromo += palindromo[::-1]
  return palindromo


# PEGANDO VÁRIOS PALÍNDROMOS ALEATÓRIOS
def palindromos_aleatorios(gramatica: 'GLC', numero_palindromos: int, tamanho: int):
  """
  Função que gera palíndromos aleatórios
  """
  palindromos = [
    palindromo_aleatorio(gramatica, tamanho) for i in range(numero_palindromos)
  ]
  return palindromos


# ESTUDO EMPÍRICO
palindromos = palindromos_aleatorios(gramatica, 40, 10)


for i in range(len(palindromos)):
  mensagem = mensagem = GLC.lmd(gramatica, palindromos[i])
  print(f'\n\n{(i+1):02d}:\t{mensagem}')