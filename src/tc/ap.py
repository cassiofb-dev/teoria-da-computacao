class AP:
  """
  Classe que representa um Autômato com Pilha.

  ---

  Atributos:
  - estados: set
    - conjunto finito de estados
  - alfabeto_automato: set
    - conjunto finito de símbolos de entrada (alfabeto_automato)
  - alfabeto_pilha: set
    - conjunto finito de símbolos de entrada (alfabeto_pilha)
  - transicao: set
    - função de transição
  - estado_inicial_automato: string
    - estado inicial do automato
  - estado_inicial_pilha: string
    - estado inicial da pilha
  - estados_finais: set
    - conjunto de estados finais
  - fita: set
    - conjunto de ações a ser executadas pelo autômato (opcional)
  - estado_atual: string
    - começa igual ao estado inicial
  ---
  """
  def __init__(
    self,
    estados: set[str],
    alfabeto_automato: set[str],
    alfabeto_pilha: set[str],
    transicoes: dict[tuple[str, str], (str, [str])],
    estado_inicial_automato: str,
    estado_inicial_pilha: str,
    estados_finais: set[str],
    fita: str = None,
  ) -> None:
    """
    parametros:
    - estados: set
      - conjunto finito de estados
    - alfabeto_automato: set
      - conjunto finito de símbolos de entrada (alfabeto_automato)
    - alfabeto_pilha: set
      - conjunto finito de símbolos de entrada (alfabeto_pilha)
    - transicoes: set
      - função de transição
    - estado_inicial_automato: string
      - estado inicial do automato
    - estado_inicial_pilha: string
      - estado inicial da pilha
    - estados_finais: set
      -  conjunto de estados finais
    """
    self.estados = estados
    self.alfabeto_automato = alfabeto_automato
    self.alfabeto_pilha = alfabeto_pilha
    self.transicoes = transicoes
    self.estado_inicial_automato = estado_inicial_automato
    self.estado_inicial_pilha = estado_inicial_pilha
    self.estados_finais = estados_finais
    self.pilha = [estado_inicial_pilha]
    self.fita = fita
    self.estado_atual = estado_inicial_automato

  def transita(self, simbolo: str):
    if simbolo in self.alfabeto_automato:
      self.estado_atual, entradas_pilha = self.transicoes[(
        self.estado_atual,
        simbolo,
        self.pilha[-1] if len(self.pilha) > 0 else None,
      )]

      self.pilha.pop() if len(self.pilha) > 0 else None

      for entrada_pilha in entradas_pilha:
        self.pilha.append(entrada_pilha)

      topo = self.pilha[-1] if len(self.pilha) > 0 else None
      return (self.estado_atual, topo)
    else:
      raise ValueError('Símbolo não reconhecido pela linguagem!')

  def computa(self, fita: str = None):
    entrada = fita if fita else self.fita

    if entrada is None:
      return
    
    for simbolo in entrada:
      q = self.estado_atual
      a = simbolo
      X = self.pilha[-1] if len(self.pilha) > 0 else None
      p, y = self.transita(simbolo)
      print(f'f{(q, a, X)}\t= {(p, y)}\tpilha: {self.pilha}')

    if self.estado_atual in self.estados_finais or len(self.pilha) == 0:
      print('Aceito pelo automato!')
    else:
      print('Não aceito pelo automato!')
