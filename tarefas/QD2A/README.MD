<h1 align="center">
  Questão Desafio 2A
</h1>

<p align="center">
  <a href="#instruções">Instruções</a> •
  <a href="#definição-formal">Definição Formal</a> •
  <a href="#implementação-em-python">Implementação em Python</a> •
  <a href="#código-do-estudo-empírico">Código do Estudo Empírico</a> •
  <a href="#resultado-do-estudo-empírico">Resultado do Estudo Empírico</a> •
  <a href="#função-de-derivação">Função de Derivação</a>
</p>

![cefet](https://i.imgur.com/K0E5iFC.jpg)

## Instruções

Para uma linguagem Livre do Contexto a sua escolha faça o que se pede.

1. Apresente a definição forma de uma gramática que a reconhece.
2. Apresente a implementação em python dessa gramática. O código python deve seguir a estrutura utilizada em aula.
3. Apresente um estudo empírico, com ao menos 40 palavras, do comprimento da derivação mais a direita na gramática que você escolheu para diferentes palavras. Como resultado desse estudo você deve apresentar uma função que relacione o tamanho de uma palavra com o comprimento da derivação mais a direita que reconhece essa palavra.
4. Com base na experiência obtida solucionando essa questão, indique a(s) dificuldades para implementar uma função que apresenta a derivação de uma palavra w em uma gramática G. Aproveite para indicar qual estratégia seria mais aconselhada para implementar esta função para w e G quaisquer.

## Definição Formal

<p align="center">
  <img src="https://i.imgur.com/hFIiIY4.png" alt="glc">
</p>

## Implementação em Python

```py
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
```

## [Código do Estudo Empírico](https://github.com/cassiofb-dev/teoria-da-computacao/blob/master/src/qd2a.py)

O código foi desenvolvido com base no [repositório do público do professor Joel dos Santos](https://github.com/joeldossantos/Teoria-da-Computacao). Para executar será preciso [python3](https://www.python.org/) e [git](https://git-scm.com/) instalados.

No seu terminal:

```sh
git clone https://github.com/cassiofb-dev/teoria-da-computacao

py src/qd2a.py

```

### Código Principal

```py
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
```

## Resultado do Estudo Empírico

A saída pode ser visualizada no gif abaixo:

![resultado](https://i.imgur.com/tHttET3.gif)

## Função de Derivação

No caso do palíndromo onde tudo é simétrico, a lmd e a rmd são similares. E o tamanho da derivação será divido em dois casos (ímpar e par):

Em ambos os casos seram acrecentado o símbolo 'S' no topo da árvore de derivação, sendo a sutileza:

- Caso Par:
  - Será acrecentado a letra vazia na parte inferior da árvore dando o resultado do tamanho da derivação
    - n/2 + 2, onde n é o tamanho da palavra
- Caso Ímpar:
  - Não será acrecentada a letra vazia como no caso par, logo seu tamanho será:
    - (n - 1) + 2, onde n é o tamanho da palavra
