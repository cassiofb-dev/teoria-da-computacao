class ER:
  """
  Classe que representa uma expressão regular.

  ---

  atributos:
  - count_i: int
    - necessario para nao repetir o nome dos estados
  """

  count_i = 0

  @staticmethod
  def er2afn_base(simbolo: str):
    """
    Função do caso base de uma expressão regular para autômato.

    ---

    parametros:
    - simbolo: str
    """
    ER.count_i += 1
    if simbolo == None:
      QSet = {f'i{ER.count_i}', f'f{ER.count_i}'}
      Sigma = {}
      Delta = {}
      FSet = {f'f{ER.count_i}'}
      return (QSet, Sigma, Delta, f'i{ER.count_i}', FSet)

    elif simbolo == '':
      QSet = {f'i{ER.count_i}', f'f{ER.count_i}'}
      Sigma = {}
      Delta = { (f'i{ER.count_i}', ''):{f'f{ER.count_i}'} }
      FSet = {f'f{ER.count_i}'}
      return (QSet, Sigma, Delta, f'i{ER.count_i}', FSet)
    else:
      QSet = {f'i{ER.count_i}', f'f{ER.count_i}'}
      Sigma = {simbolo}
      Delta = {(f'i{ER.count_i}', simbolo):{f'f{ER.count_i}'}}
      FSet = {f'f{ER.count_i}'}
    return (QSet, Sigma, Delta, f'i{ER.count_i}', FSet)

  @staticmethod
  def er2afn_union(R, S):
    """
    Função que faz a união de dois AFNs regulares, famoso 'ou'.

    ---

    parametro:
    - R: AFN
    - S: AFN
    """
    ER.count_i += 1
    new_i = f'i{ER.count_i}'
    new_f = f'f{ER.count_i}'

    newQSet = R[0].union(S[0]).union({new_i, new_f})
    newSigma = R[1].union(S[1])

    end_R = next(iter(R[4]))
    end_S = next(iter(S[4]))

    newDelta = {
      (new_i, ''):{R[3], S[3]},
      (end_R, ''):{new_f},
      (end_S, ''):{new_f},
      **R[2],
      **S[2]
    }
    newFSet = {new_f}
    return (newQSet, newSigma, newDelta, new_i, newFSet)

  @staticmethod
  def er2afn_concat(R, S):
    """
    Função que faz a concatenação de dois AFNs regulares.

    ---

    parametro:
    - R: AFN
    - S: AFN
    """
    newQSet = R[0].union(S[0])
    newSigma = R[1].union(S[1])

    end_R = next(iter(R[4]))

    newDelta = {
      **R[2],
      (end_R, ''): {S[3]},
      **S[2]
    }
    newFSet = S[4]
    return (newQSet, newSigma, newDelta, R[3], newFSet)

  @staticmethod
  def er2afn_kleene(R):
    """
    Função que faz a operação '*', fazendo um loop não obrigatório.

    ---

    parametro:
    - R: AFN
    """
    ER.count_i += 1
    new_i = f'i{ER.count_i}'
    new_f = f'f{ER.count_i}'

    newQSet = R[0].union({new_i, new_f})
    newSigma = R[1]

    end_R = next(iter(R[4]))

    newDelta = {
      (new_i, ''):{R[3], new_f},
      (end_R, ''):{new_f, R[3]},
      **R[2]
    }
    newFSet = {new_f}

    return (newQSet, newSigma, newDelta, new_i, newFSet)

  @staticmethod
  def er2afn(expreg: tuple):
    """
    Função que faz a união de dois AFNs regulares, famoso 'ou'.

    ---

    parametro:
    - expreg: tuple
    """
    operador = expreg[0]

    operando_1 = expreg[1]

    if type(operando_1) is tuple:
      operando_1 = ER.er2afn(operando_1)
    else:
      operando_1 = ER.er2afn_base(operando_1)

    if len(expreg) > 2:
      operando_2 = expreg[2]
      if type(operando_2) is tuple:
        operando_2 = ER.er2afn(operando_2)
      else:
        operando_2 = ER.er2afn_base(operando_2)
    if operador == '+':
      return ER.er2afn_union(operando_1, operando_2)
    elif operador == '':
      return ER.er2afn_concat(operando_1, operando_2)
    elif operador == '*':
      return ER.er2afn_kleene(operando_1)

  @staticmethod
  def delta(automato, estado, simbolo):
    """
    Função que faz a transição de estado do autômato

    ---

    parametros:
    - automato: AFN
    - estado: str
    - simbolo: str
    """
    try:
      return automato[2][(estado, simbolo)]
    except:
      return {None}

  @staticmethod
  def eclose(automato,estados):
    """
    Função que faz a operação eclose de um AFN

    ---

    parametros:
    - automato: AFN
    - estados: set[str]
    """
    if estados == {None}:
      return {}

    simbolo = ''
    eclosure = set()

    for estado in estados:
      eclosure = eclosure.union({estado})
      if(ER.delta(automato,estado,simbolo) != {None}):
        eclosure = eclosure.union(ER.delta(automato, estado, simbolo))
        eclosure = eclosure.union(ER.eclose(automato, ER.delta(automato, estado, simbolo)))
    return eclosure

  @staticmethod
  def delta_hat(automato, estado, palavra):
    """
    Função que faz a transição estendida do autômato.

    ---

    parametros:
    - automato: AFN
    - estado: str
    - palavra: list[str]
    """
    if palavra == []:
      return estado
    else:
      palavra_copy = palavra.copy()
      simbolo = palavra_copy.pop()
      fe = ER.eclose(automato, estado)
      fn = set()
      for e in fe:
        estados = ER.delta_hat(automato, {e}, palavra_copy)
        deltas = [ER.delta(automato, estado, simbolo) for estado in estados]
        fn = fn.union(*deltas)
      fn_copy = fn.copy()

      for f in fn_copy:
        if f is not None:
          fn = fn.union(ER.eclose(automato, {f}))
      return fn

  @staticmethod
  def aceita(automato, palavra):
    """
    Função que verifica se uma palavra é aceita em um AFN.

    ---

    parametros:
    - automato: AFN
    - palavra: list[str]
    """
    estados_finais = ER.delta_hat(automato, {automato[3]}, palavra)
    for estado in estados_finais:
      if estado in automato[4]:
        return True
    return False

  @staticmethod
  def er2str(expressao_regular: tuple):
    """
    Função que printa uma expressão regular

    ---

    parametros:
    - expressao_regular: tuple
    """
    operator = expressao_regular[0]

    if len(expressao_regular) == 3:
      if type(expressao_regular[-2]) is tuple and type(expressao_regular[-1]) is tuple:
        x1 = ER.er2str(expressao_regular[-2])
        x2 = ER.er2str(expressao_regular[-1])
        return "".join(f'({str(x1)})' + str(operator) + f'({str(x2)})')

      if type(expressao_regular[-2]) is tuple:
        x1 = ER.er2str(expressao_regular[-2])
        return "".join(f'({str(x1)})' + str(operator) + str(expressao_regular[-1]))

      if type(expressao_regular[-1]) is tuple:
        x2 = ER.er2str(expressao_regular[-1])
        return "".join(str(expressao_regular[-2]) + str(operator) + f'({str(x2)})')

      else:
        return "".join(str(expressao_regular[-2]) + str(operator) + str(expressao_regular[-1]))

    if len(expressao_regular) == 2:
      if type(expressao_regular[-1]) is tuple:
        x2 = ER.er2str(expressao_regular[-1])
        return "".join(f'({str(x2)})' + str(operator))

      else:
        return "".join(str(expressao_regular[-1]) + str(operator))

  @staticmethod
  def print(expressao_regular: tuple):
    """
    Função que printa uma expressão regular

    ---

    parametros:
    - expressao_regular: tuple
    """
    print(f'\nExpressão Regular: {ER.er2str(expressao_regular)}')

  @staticmethod
  def testa(automato, fita: str) -> None:
    """
    Função que realiza testa uma fita em um autômato.

    ---

    parametros:
    - automato: AFN
    - fita: str
    """
    palavra = [letra for letra in fita]
    if len(palavra) == 0: palavra.append('')
    aceito = ER.aceita(automato, palavra.copy())

    print(f'\tEntrada: "{fita}"\n\tSaida: {"Aceita" if aceito  else "Não Aceita"}\n')

    return aceito