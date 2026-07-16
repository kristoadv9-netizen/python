# Roadmap de Aprendizado de Python

Este roadmap foi criado para guiar seus estudos em Python, começando pelos fundamentos (como a sua primeira calculadora) até tópicos mais avançados. 
O código está organizado em 5 pastas, cada uma correspondendo a um nível de aprendizado contendo 10 tarefas. Marque as caixas conforme for progredindo!

## Nível 1: Fundamentos e Lógica (`01_Fundamentos_e_Logica`)
Nesta etapa, o foco é entender a sintaxe básica, variáveis, tipos de dados e estruturas de controle de fluxo.

- [x] **Task 01:** Calculadora de conversão de temperatura (Seu `primeiro teste.py`).
- [ ] **Task 02:** Calculadora básica (Soma, Subtração, Multiplicação, Divisão) recebendo input do usuário.
- [ ] **Task 03:** Programa que verifica se um número é par ou ímpar (Uso de `if/else` e operador módulo `%`).
- [ ] **Task 04:** Jogo de adivinhar o número (Uso de `while` e módulo `random`).
- [ ] **Task 05:** Tabuada de um número fornecido pelo usuário (Uso do laço `for`).
- [ ] **Task 06:** Calculadora de IMC (Índice de Massa Corporal) com categorias (Abaixo do peso, normal, etc.).
- [ ] **Task 07:** Contador de vogais em uma frase digitada pelo usuário.
- [ ] **Task 08:** Programa que calcula o fatorial de um número.
- [ ] **Task 09:** Verificador de palíndromos (checar se uma palavra é lida da mesma forma de trás pra frente).
- [ ] **Task 10:** Simulador de caixa eletrônico (Contagem de notas para um saque).

## Nível 2: Estruturas de Dados e Funções (`02_Estruturas_e_Funcoes`)
Aqui vamos organizar melhor nossos dados usando Listas, Dicionários, Tuplas e Sets, além de criar blocos de código reutilizáveis (Funções).

- [ ] **Task 11:** Criar uma função que recebe uma lista de números e retorna o maior e o menor valor.
- [ ] **Task 12:** Gerenciador de tarefas simples (To-Do List) usando uma lista para armazenar os itens (adicionar, remover, listar).
- [ ] **Task 13:** Dicionário de contatos (nome como chave, telefone como valor) com opções de buscar, adicionar e deletar.
- [ ] **Task 14:** Função que calcula a média de notas de alunos armazenadas em um dicionário.
- [ ] **Task 15:** Programa que remove elementos duplicados de uma lista usando `set`.
- [ ] **Task 16:** Gerador de senhas aleatórias (função que recebe o tamanho e caracteres permitidos).
- [ ] **Task 17:** Contador de frequência de palavras em um texto longo (usando dicionários).
- [ ] **Task 18:** Função recursiva para calcular a sequência de Fibonacci.
- [ ] **Task 19:** Jogo da forca estruturado (usando listas para letras tentadas e funções para a lógica).
- [ ] **Task 20:** Função que recebe n argumentos (`*args` e `**kwargs`) e imprime um relatório.

## Nível 3: Orientação a Objetos (`03_Orientacao_a_Objetos`)
Vamos introduzir o paradigma de Programação Orientada a Objetos (POO): Classes, Objetos, Herança e Polimorfismo.

- [ ] **Task 21:** Criar uma classe `Pessoa` com atributos (nome, idade) e métodos (apresentar).
- [ ] **Task 22:** Modelar uma classe `ContaBancaria` com saldo, métodos de depósito e saque (com validação de saldo).
- [ ] **Task 23:** Criar uma classe `Carro` com métodos para acelerar, frear e mostrar a velocidade atual.
- [ ] **Task 24:** Sistema de Herança: Criar uma classe base `Animal` e subclasses `Cachorro` e `Gato` com o método `emitir_som()`.
- [ ] **Task 25:** Loja virtual simples: Classes `Produto`, `CarrinhoDeCompras` e `Cliente`.
- [ ] **Task 26:** Gerenciador de biblioteca: Classes `Livro`, `Membro` e `Biblioteca` (emprestar, devolver).
- [ ] **Task 27:** Classe `Retangulo` com métodos para calcular área e perímetro (usando propriedades `@property`).
- [ ] **Task 28:** Jogo de RPG de texto simples: Classes `Personagem` (base), `Guerreiro` e `Mago` lutando contra `Inimigos`.
- [ ] **Task 29:** Implementar métodos mágicos/dunder (`__str__`, `__len__`, `__add__`) em uma classe de `Vetor2D`.
- [ ] **Task 30:** Criar uma classe `Agenda` que agrega objetos da classe `Contato`.

## Nível 4: Manipulação de Arquivos e Módulos (`04_Arquivos_e_Modulos`)
Aprendizado sobre como ler e escrever arquivos no computador, além de usar bibliotecas padrão do Python.

- [ ] **Task 31:** Criar um programa que escreve uma lista de compras em um arquivo `compras.txt`.
- [ ] **Task 32:** Ler o arquivo `compras.txt` e exibir no terminal com números nas linhas.
- [ ] **Task 33:** Contador de linhas e caracteres de um arquivo de texto qualquer.
- [ ] **Task 34:** Salvar o Dicionário de Contatos (da Task 13) em um arquivo `.json` (usando o módulo `json`).
- [ ] **Task 35:** Ler o arquivo `.json` de contatos e carregá-los de volta para o programa.
- [ ] **Task 36:** Programa que junta (concatena) o conteúdo de vários arquivos de texto em um só.
- [ ] **Task 37:** Script para renomear em massa todos os arquivos `.txt` de uma pasta (usando o módulo `os`).
- [ ] **Task 38:** Extrair dados de um arquivo `.csv` (como uma planilha de vendas) e calcular o total usando a biblioteca `csv`.
- [ ] **Task 39:** Script que mostra a data e hora atuais formatadas, e calcula quantos dias faltam para o fim do ano (módulo `datetime`).
- [ ] **Task 40:** Criar o seu próprio módulo (um arquivo `.py` com funções úteis) e importá-lo em outro script.

## Nível 5: Tópicos Avançados e APIs (`05_Avancado_e_APIs`)
Explorando recursos avançados do Python, tratamento de erros e integração com a web.

- [ ] **Task 41:** Implementar um bloco `try/except` robusto na Calculadora Básica para evitar erros de divisão por zero e letras no lugar de números.
- [ ] **Task 42:** Criar uma função geradora (`yield`) que produz números primos infinitamente.
- [ ] **Task 43:** Usar List Comprehension para criar uma lista de quadrados dos números pares de 1 a 100.
- [ ] **Task 44:** Criar um Decorator (`@meu_decorator`) que mede o tempo de execução de uma função.
- [ ] **Task 45:** Fazer uma requisição GET para uma API pública (ex: API do ViaCEP) usando a biblioteca `requests`.
- [ ] **Task 46:** Mostrar a previsão do tempo atual de uma cidade puxando os dados de uma API (ex: OpenWeatherMap).
- [ ] **Task 47:** Extrair os títulos das notícias da página principal de um site de notícias (Web Scraping simples com `BeautifulSoup`).
- [ ] **Task 48:** Enviar um e-mail automatizado pelo Python usando a biblioteca `smtplib`.
- [ ] **Task 49:** Interface Gráfica Simples (GUI): Fazer uma janela com um botão e um texto usando a biblioteca `tkinter`.
