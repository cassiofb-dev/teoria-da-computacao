<h1 align="center">
  Questão Desafio 2B
</h1>

<p align="center">
  <a href="#instruções">Instruções</a> •
  <a href="#definição-formal">Definição Formal</a> •
  <a href="#explicação">Explicação</a> •
  <a href="#palavras-aceitas">Palavras Aceitas</a>
</p>

![cefet](https://i.imgur.com/K0E5iFC.jpg)

## Instruções

Um prédio de três andares (1,2,3) comprou um elevador mais moderno que funciona como segue:

- O novo elevador continua iniciando seu funcionamento no andar 1, com a porta aberta;
- O painel do elevador agora possui botões com a numeração de cada andar (1,2,3);
- Uma vez parado em um andar com a porta aberta, o elevador aceita que sejam pressionados os botões dos andares e só volta a fechar a porta quando o botão de fechar porta f é pressionado;
- Os botões dos andares podem ser pressionados em qualquer ordem, mas o elevador deverá parar em cada andar conforme a ordem dos andares;
- Se o elevador está subindo e entra alguém para descer, ele continua subindo antes de descer;
- O elevador abre a porta automaticamente quando para em um andar, sem precisar de um comando específico para tal;
- O elevador pode subir mais de um andar por vez, baseado apenas na numeração do andar escolhido.

Considerando o alfabeto Σ = {1, 2, 3, f }, faça um Autômato com Pilha que controla o funcionamento do elevador.
Com base na questão cima deverão ser entregues:

1. A especificação forma do autômato.
2. Um texto justificando seu raciocínio para a montagem do autômato.
3. Exemplos de palavras válidas para o elevador, dependendo dos andares escolhidos e de onde o elevador está (ex.: alguém está no andar 1 e quer ir para o 3).

## Definição Formal

Observação: A palavra vazia é representada por 'e'

<p align="center">
  <img src="https://i.imgur.com/smdrK0M.png" alt="qd2b">
</p>

## Explicação

O autômato deverá guardar 3 estados para os andares sendo que cada um pode se encontrar em um estado aberto ou fechado, logo deveremos ter 3 * 2 = 6 estados.

Apesar de ser uma limitação, para simplifacação do código o elevador só irá abrir a porta caso a pilha estiver vazia.

Para transitar de um andar para o outro o autômato deverá ter ser comportar da seguinte maneira:

1. Pilha vazia e andar adjacente
   - Transita para o andar sem alterar a pilha
2. Pilha não vazia e andar adjacente
   - Transita para o andar da pilha e coloca o adjacente no topo
3. Pilha vazia e andar não adjacente
   - Coloca o andar na pilha e transita em sua direção
4. Pilha não vazia e andar não adjacente
   - Coloca o andar na pilha abaixo do topo e transita na direção do topo
5. Pilha vazia e palavra vazia
   - Abre a porta

Para simplificar o diagrama as trânsições de 'f' não foram explícitadas pois abrir e fechar a porta não altera a pilha, uma vez que ela tem apenas como objetivo guardar a informação e ordem dos andares que se deseja alcançar.

Vale lembrar também que todos os estados são considerados finais pela definição de pilha vazia, pois em todos os estados podemos ter uma pilha vazia.

## Palavras Aceitas

Lembrando que o elevador começa do estado ```1A``` podemos realizar as seguintes ações:

1. Ir direto para o terceiro andar: ```f3```
2. Ir direto para o terceiro e depois direto para o primeiro: ```f3f1```
3. Visitar todos os andares (abrindo a porta): ```f1f2f3```
