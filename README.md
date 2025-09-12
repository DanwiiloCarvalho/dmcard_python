# Teste DMCard Python

A DMCard está em busca de pessoas incríveis que integrem nosso time para
criarmos produtos digitais incríveis, e gostaríamos de ter você aqui conosco.
Para iniciar o processo, pedimos um teste que não vai tomar muito do seu tempo e
nos dará uma perspectiva da sua forma de trabalhar.

## Requisitos do desafio

Deve se criar uma aplicação que permitirá a solicitação de um cartão de crédito,
onde o usuário irá inserir suas informações básicas e o sistema irá fazer uma
análise da liberação do cartão.
Deve ser feito uma API Restful, que permitirá:

- Cartão
<ul style="padding-left: 5rem">
    <li style="list-style-type: circle"><span style="font-weight: bold">GET</span>: Listar todas as solicitações de cartões no sistema ordenadas por data
de solicitação.</li>

<li style="list-style-type: circle"><span style="font-weight: bold">POST</span>: Deve inserir uma nova solicitação de cartão.</li>

<li style="list-style-type: circle"><span style="font-weight: bold">DELETE</span>: Remove uma solicitação.</li>
</ul>

Quando o usuário solicitar um cartão, deve ter uma aprovação automática do
sistema.
Deverá ser criada uma rotina que verificará a pontuação de crédito do usuário que
será uma rotina que devolva uma pontuação aleatória entre 1 a 999, para ser
utilizada como score de credito.
Por exemplo:

```code
import random
random.randint(1,999)
```

Sendo que, dependendo do score retornado a solicitação é aprovada ou não,
também alterando o seu limite de crédito, que deverá seguir a seguinte lógica:

| Score     | Crédito                                        |
| --------- | ---------------------------------------------- |
| 1 a 299   | Reprovado                                      |
| 300 a 599 | R$ 1000,00                                     |
| 600 a 799 | 50% da renda informada, valor mínimo R$1000,00 |
| 800 a 950 | 200% da renda informada                        |
| 951 a 999 | Sem limites, considerar R$ 1.000.000           |

O Back-End deverá ser feito em Python, utilizando um framework de sua escolha.
Qualquer dúvida sobre os requisitos, você pode enviar um e-mail
para jailson.dias@dmcard.com.br

## Critérios de avaliação

Tudo que for feito no desafio vai ser considerado, abaixo tem algumas das coisas
que vão ser consideradas no momento da avaliação, mas pode ser avaliado outras
coisa também.

<ol>
    <li>Organização do código (Classes, Métodos etc)</li>

<li>Estrutura de pastas e arquivos do projeto</li>

<li>Testes</li>

<li>Documentação</li>

<li>Nomes de variáveis, classes etc</li>
</ol>

## Como fazer?

Sugerimos um prazo de 7 dias para a entrega. Caso precise de mais nos avise e
Justifique.
Sobre a entrega:

<ul>
    <li style="font-weight: bold">Pedimos que você nos envie um e-mail, para sinalizar seu início no
desenvolvimento do desafio.</li>

<li>Seu código deve estar disponível em um repositório no Github.</li>

<li>Você pode utilizar plataformas como Heroku ou AWS para nos mostrar a
aplicação funcionando em produção.</li>

<li>Quando estiver pronto nos envie o link do repositório.</li>
</ul>

Boa Sorte!
