# Jokenpo AWS Lambda

Este projeto é uma implementação simples do jogo Jokenpo (Pedra, Papel, Tesoura) usando AWS Lambda e API Gateway.

## Funcionalidades

- O jogador faz uma escolha (pedra, papel ou tesoura) e a API seleciona uma escolha aleatória para a máquina.
- A API determina o vencedor com base nas escolhas do jogador e da máquina.

## Como testar no Postman

1. Abra o Postman ou uma ferramenta similar para fazer solicitações HTTP.
2. Crie uma solicitação POST.
3. Insira o URL da API: `https://hy0gp41bt1.execute-api.us-east-2.amazonaws.com/playJokenpo`.
4. No cabeçalho da solicitação, adicione um cabeçalho "Content-Type" com o valor "application/json".
5. No corpo da solicitação, selecione a opção "Raw" e escolha o tipo de dados como "JSON (application/json)".
6. Insira o seguinte JSON no corpo da solicitação, ou mude o valor do user_choice de acordo com sua escolha (pedra, papel ou tesoura):
   ```json
   {
     "user_choice": "pedra"
   }
