<h1 align="center">
  Questão Desafio 1A
</h1>

<p align="center">
  <a href="#instruções">Instruções</a> •
  <a href="#especificação-formal">Especificação Formal</a> •
  <a href="#desenvolvimento">Desenvolvimento</a> •
  <a href="#código-python">Código Python</a> •
  <a href="#teste">Testes</a>
</p>

![cefet](https://i.imgur.com/K0E5iFC.jpg)

## Instruções

Considere um prédio de cinco andares (1, 2, 3, 4, 5) contendo um elevador. O elevador
do prédio funciona como segue:

- Quando inicia seu funcionamento, o elevador está no andar 1, com a porta aberta;
- O painel do elevador possui botões de fechar a porta f, abrir a porta a, subir s ou
descer d;
- O elevador não possui painel externo de chamar o elevador;
- O elevador sobe um andar por vez, mantendo sua porta fechada, a menos que o
botão de abrir porta seja pressionado.
- Ao final do dia um funcionário leva o elevador de volta para o primeiro andar

Considerando o alfabeto Σ = {a, f, s, d}, faça um Autômato Finito que controla o
funcionamento do elevador. O autômato deverá aceitar as palavras que simbolizam um
conjunto de movimentos válidos para o elevador ao longo de um dia de funcionamento.

Com base na questão acima deverão ser entregues:

<style type="text/css">
    ol { list-style-type: upper-alpha; }
</style>

1. A especificação formal do autômato (grafo, tabela ou função de transição).
2. Um texto justificando seu raciocínio para a montagem do autômato.
3. A implementação do autômato em python conforme o modelo utilizado em aula.
4. Uma sequência de 20 testes, sendo 10 com palavras válidas e 10 com palavras inválidas.

## Especificação Formal

![qd1a](https://i.imgur.com/8fOSBqx.png)

## Desenvolvimento

Partindo de que um elevador pode subir e descer ao prescionar os botões de subir e descer, podemos
fazer facilmente um autômato que só represente esse modelo e depois podemos expandir ele nas laterais
para acrescentar um estado aberto e fechado com relações as portas com suas ações de abrir e fechar.

Considerei durante o desenvolvimento que a porta do elevador deverá sempre terminar aberta pois a
pessoa não conseguirá entrar no elevador no dia seguinte.

## Código Python

O código foi desenvolvido com base no [repositório do público do professor Joel dos Santos](https://github.com/joeldossantos/Teoria-da-Computacao). Para executar será preciso [python3](https://www.python.org/) e [git](https://git-scm.com/) instalados.

No seu terminal:

```sh
git clone https://github.com/cassiofb-dev/teoria-da-computacao

py src/qd1a.py

```

## Testes

No Código foram testadas as seguintes palavras:

```py
# TESTES VALIDOS

AFD.testa(automato, "aaaaaaaaaa") #1
AFD.testa(automato, "fafafafafa") #2
AFD.testa(automato, "fssddffafa") #3
AFD.testa(automato, "fssssdddda") #4
AFD.testa(automato, "fsafsddfaa") #5
AFD.testa(automato, "fssasfddaa") #6
AFD.testa(automato, "affssddaaa") #7
AFD.testa(automato, "fsssffddda") #8
AFD.testa(automato, "ffssddsdfa") #9
AFD.testa(automato, "fsssfdddaa") #10

# TESTES INVALIDOS

AFD.testa(automato, "fsssssssss") #1
AFD.testa(automato, "fssasafsaf") #2
AFD.testa(automato, "fsssafafad") #3
AFD.testa(automato, "fsafasfasf") #4
AFD.testa(automato, "fasfasfasf") #5
AFD.testa(automato, "fsfsfsfsfs") #6
AFD.testa(automato, "fsafsafsaf") #7
AFD.testa(automato, "fffafsssss") #8
AFD.testa(automato, "aaaffsafas") #9
AFD.testa(automato, "ffsafasfas") #10
```

A saída pode ser visualizada no gif abaixo:

![teste](https://i.imgur.com/U0juMy7.gif)
