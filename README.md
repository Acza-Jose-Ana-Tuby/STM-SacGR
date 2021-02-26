# STM-SacGR
Repositório para armazenamento do código fonte do Sistema de Agendamento de Consultas para Grupos de Risco, como requisito de avaliação para a disciplina de Laboratório de Engenheria de Software, Professor Cleidson Ronald Botelho de Souuza, Faculdade de Computação, UFPA

#Preparando o ambiente:
Para executar o projeto, tenha certeza de ter instalados:
Wamp (Windows) ou Lamp (Linux). Recomenda-se entretanto, instalar o Xampp (Multiplataforma);
IDE com suporte para Python e JS (Recomenda-se Visual Studio Code);
Python3;
Pip3;
Node.js 10.21.0;
npm 6.14.9;

#Preparando os servidores em máquina local:
BackEnd:  Abra o terminal (Linux) ou prompt (Windows) e navegue para pasta do back-end, a seguir:
1. Crie um ambiente virtual para alocar as dependências: [virtualenv venv]
2. Ative o ambiente: [. venv/bin/activate]
3. Instale as dependências do projeto: [pip install -r requirements.txt]
4. Enfim, execute o comando: [python3 run.py]

FrontEnd: Abra o terminal (Linux) ou prompt (Windows) e navegue para pasta do front-end, a seguir use o comando [npm install] para instalar as dependências necessárias. Caso haja uma mensegem de erro, re-execute o comando com privilégios de administrador. Depois da instalação, abra o servidor web em modo de desenvolvimento digitando o comando [npm run serve] e aguarde o servidor ser carregado.

Executando a aplicação:
Abra o navegador de internet (Chrome, Firefox, etc) e certifique-se de que o javascript esteja habilitado. Acesse a aplicação digitando na barra de endereço localhost:8081/.
