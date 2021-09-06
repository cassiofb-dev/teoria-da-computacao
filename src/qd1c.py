from tc.er import ER

# Exemplo de funcionamento.
# Testes reais dentro da pasta teste.

expressao_regular_1 = ('', ('*', 'a'), ('', 'b', ('*', 'c')))
expressao_regular_2 = ('+', ('*', 'a'), ('', ('+', 'b', 'd'), ('*', 'c')))
expressao_regular_3 = ('+', ('*', '1'), ('*', '0'))

automato_1 = ER.er2afn(expressao_regular_1)
ER.print(expressao_regular_1)
ER.testa(automato_1, 'aaaaaabcccccc')
ER.testa(automato_1, 'aaaaaacccccc')

automato_2 = ER.er2afn(expressao_regular_2)
ER.print(expressao_regular_2)
ER.testa(automato_2, 'bccccc')
ER.testa(automato_2, 'bdccccc')

automato_3 = ER.er2afn(expressao_regular_3)
ER.print(expressao_regular_3)
ER.testa(automato_3, '11111')
ER.testa(automato_3, '111110')