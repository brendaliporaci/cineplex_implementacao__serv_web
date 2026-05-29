# Cinema Seat Reservation System

Sistema distribuído de reserva de assentos de cinema desenvolvido para a disciplina de Sistemas Distribuídos.

## Tecnologias utilizadas

- HTML5
- CSS3
- JavaScript
- Python
- Flask
- REST API

## Funcionalidades

- Visualização dos assentos disponíveis e reservados;
- Seleção de assentos pelo usuário;
- Cálculo automático do valor da reserva;
- Consulta de disponibilidade através de API REST;
- Reserva de assentos através de requisições HTTP;
- Comunicação entre cliente e servidor utilizando JSON.

## Arquitetura

O sistema segue uma arquitetura cliente-servidor, onde:

- O cliente web é responsável pela interface e interação com o usuário;
- O servidor Flask fornece os dados dos assentos e processa as reservas;
- A comunicação ocorre através de requisições HTTP seguindo princípios REST.

## Créditos

Este projeto foi desenvolvido a partir do projeto open source **Cinema Seat Selector**, criado por Chatura Dissanayake.

Projeto original: https://github.com/chaturadissanayake/cinema-seat-selector

O sistema original forneceu a interface gráfica para seleção de assentos. Para atender aos requisitos da disciplina de Sistemas Distribuídos, foram realizadas adaptações e extensões, incluindo:

- Implementação de uma arquitetura cliente-servidor;
- Desenvolvimento de uma API REST utilizando Python e Flask;
- Integração entre cliente e servidor por meio de requisições HTTP;
- Implementação da funcionalidade de reserva de assentos;
- Gerenciamento centralizado da disponibilidade dos assentos.
