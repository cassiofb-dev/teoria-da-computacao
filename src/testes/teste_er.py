from tc.er import ER

class TesteER:
  def teste_expressao_regular_1(self):
    expressao_regular_1 = ('', ('*', 'a'), ('', 'b', ('*', 'c')))
    automato_1 = ER.er2afn(expressao_regular_1)
    assert ER.testa(automato_1, 'b') == True
    assert ER.testa(automato_1, 'ab') == True
    assert ER.testa(automato_1, 'bc') == True
    assert ER.testa(automato_1, 'abc') == True
    assert ER.testa(automato_1, 'aabc') == True
    assert ER.testa(automato_1, 'abcc') == True
    assert ER.testa(automato_1, 'aabcc') == True
    assert ER.testa(automato_1, 'aaaaaaabccccccc') == True
    assert ER.testa(automato_1, '') == False
    assert ER.testa(automato_1, 'a') == False
    assert ER.testa(automato_1, 'c') == False
    assert ER.testa(automato_1, 'ac') == False

  def teste_expressao_regular_2(self):
    expressao_regular_2 = ('+', ('*', 'a'), ('', ('+', 'b', 'd'), ('*', 'c')))
    automato_2 = ER.er2afn(expressao_regular_2)
    assert ER.testa(automato_2, '') == True
    assert ER.testa(automato_2, 'a') == True
    assert ER.testa(automato_2, 'aa') == True
    assert ER.testa(automato_2, 'b') == True
    assert ER.testa(automato_2, 'd') == True
    assert ER.testa(automato_2, 'bccc') == True
    assert ER.testa(automato_2, 'dccc') == True
    assert ER.testa(automato_2, 'aabcc') == False
    assert ER.testa(automato_2, 'abdc') == False
    assert ER.testa(automato_2, 'bdc') == False
    assert ER.testa(automato_2, 'abd') == False
    assert ER.testa(automato_2, 'bd') == False
  
  def teste_expressao_regular_3(self):
    expressao_regular_3 = ('+', ('*', '1'), ('*', '0'))
    automato_3 = ER.er2afn(expressao_regular_3)
    assert ER.testa(automato_3, '') == True
    assert ER.testa(automato_3, '1') == True
    assert ER.testa(automato_3, '11') == True
    assert ER.testa(automato_3, '0') == True
    assert ER.testa(automato_3, '00') == True
    assert ER.testa(automato_3, '01') == False
    assert ER.testa(automato_3, '10') == False
    assert ER.testa(automato_3, '1110') == False
    assert ER.testa(automato_3, '0001') == False
    assert ER.testa(automato_3, '010') == False
    assert ER.testa(automato_3, '101') == False
    assert ER.testa(automato_3, '1010101010') == False