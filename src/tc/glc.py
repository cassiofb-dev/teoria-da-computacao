import random

class GLC:
  """
  Classe que representa uma gramática regular.

  ---

  atributos:
  - variaveis: set[str]
    - conjunto de variáveis
  - terminais: set[str]
    - conjunto de símbolos terminais
  - producoes: set[(str, tuple)]
    - conjunto de produções gramáticas
  - variavel_inicial: string
    - variável inicial
  - arvore: tuple
    - arvore de derivação
  ---
  """
  def __init__(
    self,
    variaveis: set[str],
    terminais: set[str],
    producoes: set[(str, tuple)],
    variavel_inicial: str
  ) -> 'None':
    """
    parametros:
    - variaveis: set[str]
      - conjunto de variáveis
    - terminais: set[str]
      - conjunto de símbolos terminais
    - producoes: set[(str, tuple)]
      - conjunto de produções gramáticas
    - variavel_inicial: string
      - variável inicial
    """
    self.variaveis = variaveis
    self.terminais = terminais
    self.producoes = producoes
    self.variavel_inicial = variavel_inicial
  
  @staticmethod
  def lmd(gramatica: 'GLC', palavra):
    palavra = str(palavra)
    palavra_aux = palavra
    producao_str = []
    inicial = gramatica.variavel_inicial
    saida = []
    saida.append(inicial)
    mensagem_saida = inicial
    mensagem = ''
    for producao in gramatica.producoes:
      if type(producao[1]) == tuple:
        prod = str(producao[1])
        prod = prod.replace("(","")
        prod = prod.replace(")","")
        prod = prod.replace("'","")
        prod = prod.replace(",","")
        prod = prod.replace(" ","")
        producao_str.append(prod)
      else:
        prod = str(producao[1])
        producao_str.append(prod)
    while mensagem_saida != palavra:
      if len(palavra) > len(mensagem_saida) and len(palavra_aux) != 0:
        for producao in producao_str:
          if len(producao) > 2 and palavra_aux != "":
            if palavra_aux[0] == producao[0] and palavra_aux[-1] == producao[2]:
              mensagem_saida = mensagem_saida.replace("S", producao)
              saida.append(mensagem_saida)
        palavra_aux = palavra_aux[1:]
        palavra_aux = palavra_aux[:-1]
      elif len(mensagem_saida) >= len(palavra):
        for producao in producao_str:
          if palavra_aux == producao:
            mensagem_saida = mensagem_saida.replace("S", producao)
            saida.append(mensagem_saida)
        palavra_aux = palavra_aux.replace(palavra_aux,"")
    for s in saida:
      if saida.index(s) == 0:
        producao = s[0]
        mensagem = producao
      else:
        producao = s
        mensagem += " => " + producao
    return mensagem
