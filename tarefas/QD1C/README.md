<h1 align="center">
  Questão Desafio 1C
</h1>

<p align="center">
  <a href="#instruções">Instruções</a> •
  <a href="#diagrama-de-sequência">Diagrama de Sequência</a> •
  <a href="#desenvolvimento">Desenvolvimento</a> •
  <a href="#código-python">Código Python</a> •
  <a href="#testes">Testes</a>
</p>

![cefet](https://i.imgur.com/K0E5iFC.jpg)

## Instruções

Implementar um algoritmo que receba uma Expressão Regular e uma palavra e indica
se a palavra é aceita ou não.
Com base na questão acima deverão ser entregues:

1. Um diagrama de sequência com os passos realizados pelo algoritmo para reconhecer (ou não) a palavra.
2. Um texto justificando seu raciocínio para a montagem do algoritmo.
3. A implementação em python do algoritmo conforme o modelo utilizado em aula.
4. Uma sequência de 20 testes, sendo 10 com palavras válidas e 10 com palavras inválidas. Deverão ser consideradas ao menos 3 ERs diferentes nos testes.

## Diagrama de Sequência

<p align="center">
  <img src="https://i.imgur.com/pYTP7Wm.png" alt="diagrama_qd1c">
</p>

## Desenvolvimento

Partindo do teorema que expressões regulares e autômatos finitos não determinísticos são equivalentes, podemos montar um esquema para solucionar o problema:

1. Entrar com uma expressão regular no formato apresentado em aula
2. Transformar essa expressão regular em um AFN
   - Função ```er2afn``` faz esse trabalho junto com algumas auxiliares:
     - ```er2afn_base```
     - ```er2afn_union```
     - ```er2afn_concat```
     - ```er2afn_kleene```
3. Verificar se uma palavra é aceita por esse AFN
   - Função ```testa``` faz esse trabalho junto com algumas auxiliares:
     - ```aceita```
     - ```delta_hat```
     - ```delta```
     - ```eclose```

## [Código Python](https://github.com/cassiofb-dev/teoria-da-computacao/blob/master/src/qd1c.py)

O código foi desenvolvido com base no [repositório do público do professor Joel dos Santos](https://github.com/joeldossantos/Teoria-da-Computacao). Para executar será preciso [python3](https://www.python.org/), [git](https://git-scm.com/) instalados.

No seu terminal:

```sh
git clone https://github.com/cassiofb-dev/teoria-da-computacao

py src/qd1c.py

```

A saída do código de exemplo pode ser observada no gif abaixo:
![exemplo_qd1c](https://i.imgur.com/zSwZRic.gif)

## Testes

No Código foram testadas as seguintes palavras e expressões regulares:

Para rodar os testes, em seu terminal:

```sh
pytest '.\src\testes\teste_er.py'
```

```py
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
```

A saída dos testes pode ser visualizada no gif abaixo:

![teste_qd1c](https://i.imgur.com/iU7jbqQ.gif)
