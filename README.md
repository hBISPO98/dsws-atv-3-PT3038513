# Formulário ​📑​

Esta aplicação consiste em um formulário web interativo desenvolvido em Flask, utilizando a extensão Flask-WTF para a criação e validação dos campos, o Flask-Bootstrap para a estruturação visual e responsiva da interface, e a arquitetura PRG (Post-Redirect-Get) para gerenciar o fluxo de requisições de forma segura através de sessões e cookies.

## Método PRG (Post-Redirect-Get)
1. Usuário faz POST: O usuário preenche o formulário e o navegador envia o payload de dados para o servidor.

2. Validação e Armazenamento: O servidor recebe os dados, executa a validação e os armazena temporariamente na session.

3. Criptografia e Cookies: O Flask criptografa as informações da sessão e as armazena de forma segura nos cookies do navegador.

4. Redirecionamento (Status 303): O servidor envia uma resposta com código de status de redirecionamento junto com o cookie, solicitando que o navegador faça um GET.

5. Requisição GET e Exibição: O navegador muda a rota da URL e a página é renderizada exibindo os valores que foram armazenados na session, limpando o histórico de reenvio do formulário.

## Demonstração
| Interface Inicial - Home |
| :---: |
| <img src="https://github.com/user-attachments/assets/0da5f893-0199-4c8f-bf77-44a54aa67213" /> |


| Incluindo Nome |
| :---: |
| <img src="https://github.com/user-attachments/assets/48da2f39-7409-4d9d-b4d7-8acc9ddacf5c" /> |


| Alterando Nome |
| :---: |
| <img src="https://github.com/user-attachments/assets/af79dc9b-7536-4def-8489-54c6e2be2e7d" /> |
