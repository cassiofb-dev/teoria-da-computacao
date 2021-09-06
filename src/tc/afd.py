class AFD:
  """
  Classe que representa um Autômato Finito Determinado.

  ---

  Atributos:
  - estados: set
    - conjunto finito de estados
  - alfabeto: set
    - conjunto finito de símbolos de entrada (alfabeto)
  - transicao: set
    - função de transição
  - estado_inicial: string
    - estado inicial
  - estado_final: set
    - conjunto de estados finais
  - palavra: set
    - conjunto de ações a ser executadas pelo autômato (opcional)
  - estado_atual: string
    - começa igual ao estado inicial
  ---
  """
  def __init__(
    self,
    estados: set[str],
    alfabeto: set[str],
    transicao: dict[tuple[str, str], str],
    estado_inicial: str,
    estado_final: set[str],
    palavra: list[str] = None,
  ) -> None:
    """
    parametros:
    - estados: set
      - conjunto finito de estados
    - alfabeto: set
      - conjunto finito de símbolos de entrada (alfabeto)
    - transicao: set
      - função de transição
    - estado_inicial: string
      - estado inicial
    - estado_final: set
      -  conjunto de estados finais
    """
    self.estados = estados
    self.alfabeto = alfabeto
    self.transicao = transicao
    self.estado_inicial = estado_inicial
    self.estado_final = estado_final
    self.palavra = palavra
    self.estado_atual = estado_inicial

  def transita(self) -> None:
    """
    Realiza uma transição interativa
    """
    a = ''
    while True:
      print(f'Estado Atual: {self.estado_atual}')
      a = input('Entre com uma transição: ')
      if a == '$': break
      AFD.delta(self, self.estado_atual, a)


  @staticmethod
  def delta(automato: 'AFD', estado: str, simbolo: str) -> str:
    """
    Função que faz a transição de estado do autômato

    ---

    parametros:
    - automato: AFD
    - estado: str
    - simbolo: str
    """
    if estado in automato.estados:
      if simbolo in automato.alfabeto:
        automato.estado_atual = automato.transicao[(estado, simbolo)]
        return automato.estado_atual
      else:
        raise ValueError('simbolo invalido')
    else:
      raise ValueError('estado invalido')

  @staticmethod
  def delta_hat(automato: 'AFD', estado: str, palavra: list[str]) -> str:
    """
    Função que faz a transição estendida do autômato,
    retornando o estado final.

    ---

    parametros:
    - automato: AFD
    - estado: str
    - palavra: list
    """
    if len(palavra) == 0:
      return estado
    else:
      simbolo = palavra.pop()
      return AFD.delta(
        automato,
        AFD.delta_hat(automato, estado, palavra),
        simbolo
      )

  @staticmethod
  def aceita(automato: 'AFD', palavra: list[str]):
    """
    Função que realiza as transições e retorna True caso o estado de parada
    seja um estado final

    ---

    parametros:
    - automato: AFD
    - palavra: list
    """
    return AFD.delta_hat(automato, automato.estado_inicial, palavra) in automato.estado_final

  @staticmethod
  def computacao(automato: 'AFD', estado: str, palavra: list[str]) -> str:
    """
    Função que faz a computação de uma palavra.

    ---

    parametros:
    - automato: AFD
    - estado: str
    - palavra: list
    """
    if len(palavra) == 0:
      return "(" + estado + ", )"
    else:
      config = "(" + estado + ", " + "".join(str(s) for s in palavra) + ") |- "
      simbolo = palavra.pop(0)
      proximo = AFD.delta(automato, estado, simbolo)
      return config + AFD.computacao(automato, proximo, palavra)

  @staticmethod
  def testa(automato: 'AFD', fita: str) -> None:
    """
    Função que realiza testa uma fita em um autômato.

    ---

    parametros:
    - automato: AFD
    - fita: str
    """
    palavra = [letra for letra in fita]
    print(f'\nTeste: {"Aceito" if AFD.aceita(automato, palavra.copy()) else "Não Aceito"}')
    resultado = AFD.computacao(automato, automato.estado_inicial, palavra.copy())
    print(resultado)
