# Cinema Seat Reservation System

Sistema REST de reserva de assentos de cinema utilizando o modelo Cliente-Servidor, desenvolvido para a disciplina de Sistemas Distribuídos 2026.1 do curso de Sistemas de Informação da UFF - Niterói.

## Tecnologias utilizadas

- HTML5
- CSS3
- JavaScript
- Python
- Biblioteca Flask
- Biblioteca JSON
- REST API

## Funcionalidades

- Visualização dos assentos disponíveis e reservados.
- Seleção de assentos pelo usuário.
- Cálculo automático do valor da reserva.
- Consulta de disponibilidade através de **API REST**.
- Reserva de assentos através de requisições **HTTP**.
- Armazenamento de dados utilizando arquivos **JSON**.
- Comunicação entre cliente e servidor utilizando **JSON**. (?)

## Arquitetura

O sistema segue uma arquitetura cliente-servidor, onde:

- O cliente web é responsável pela interface e interação com o usuário;
- O servidor Flask cuida do armazenamento e processamento, fornecendo os dados dos assentos e processando as reservas;
- A comunicação ocorre através de requisições HTTP seguindo os princípios REST.

## Créditos

Este projeto foi desenvolvido a partir do projeto open source **Cinema Seat Selector**, criado por Chatura Dissanayake.

Projeto original: https://github.com/chaturadissanayake/cinema-seat-selector

O sistema original forneceu a interface gráfica para seleção de assentos. 

## Checklist das alterações

Para atender aos requisitos da disciplina de Sistemas Distribuídos, foram realizadas adaptações e extensões, incluindo:

- [ ] Implementação de uma arquitetura cliente-servidor
    - [X] Lado do cliente: Separação do Frontend, UX e UI
    - [ ] Lado do servidor: Armazenamento de Dados e Processamento
- [ ] Desenvolvimento de uma API REST utilizando Python e Flask
    - [ ] Saída de dados em JSON
    - [ ] Recursos com identificadores uniformes e únicos
    - [ ] Stateless
    - [ ] Utilizar Hipermídia (HATEOAS)
- [ ] Integração entre cliente e servidor por meio de requisições HTTP;
    - [ ] Implementar requisição do tipo GET
    - [ ] Implementar requisição do tipo POST
    - [ ] Implementar requisição do tipo PUT
    - [ ] Implementar requisição do tipo DELETE
- [X] Implementação da funcionalidade de reserva de assentos;
- [ ] Gerenciamento centralizado da disponibilidade dos assentos.
