<h1 align="center">
  Questão Desafio 3
</h1>

<p align="center">
  <a href="#instruções">Instruções</a> •
  <a href="#pcp">PCP</a> •
  <a href="#explicação">Explicação</a> •
  <a href="#algoritmo">Algoritmo</a>
</p>

![cefet](https://i.imgur.com/K0E5iFC.jpg)

## Instruções

Mostre que o Problema da Correspondência de Post é decidível sobre o alfabeto unário Σ = {1}.

## PCP

> A entrada do problema consiste em duas listas finitas de palavras sobre algum alfabeto tendo pelo menos 2 símbolos. Uma solução para esse problema é uma sequência de palavras tal que sejam formadas pelos mesmo índices nas duas listas. O problema de decisão é, então, decidir se tal solução existe ou não.

## Explicação

Podemos pensar em tal problema como uma lista de dominós, nosso objetivo seria achar uma lista de dominós de maneira que a parte superior e inferior quando lidas na horizontal sejam exatamente iguais. Como no exemplo:

```txt
|-----|-----|
|  1  |  11 |
|-----|-----|
| 11  |  1  |
|-----|-----|
```

Nesse caso a primeira lista seria: ``['1', '11']``<br>
E a segunda lista seria: ``['11', '1']``

## Algoritmo

Agora com o problema simplificado, podemos focar no algoritmo:

Considere uma sequencida de dominós como entrada:

1. Se um dominó tem o mesmo tamanho na parte inferior e superior, aceite.
2. Se todos os dominós possuem tamanho diferente na parte inferior e superior, rejeite.
3. Procure um dominó com um tamanho superior maior, e outro com um tamanho inferior menor, se quando juntos o tamanho superior e inferior sejam iguais, aceite.
