# Projeto de avaliação técnica
Projeto de avaliação técnica para o processo seletivo da IGS Software.

## Endpoints
Foram criados dois endpoints:

- **/admin** - Rota de acesso a página de login do Admin do django.

- **/employees** - o endpoint recebe requisições GET, POST, PUT e DELETE, além de receber requisições 'GET by ID'.

  - Query params:
    
    - **name** - Filtrando colaboradores por nome;
    - **email** - Filtrando colaborador por e-mail;
    - **departament** - Filtrando colaboradores de um departamento específico;

- **/departaments** - endpoint para consulta da lista de departamentos;

  - Query params:

    - **name** - Filtrando departamentos por nome; 
## Execução do projeto

- Criar uma virtual env. 
      
     `python -m venv venv`


- Instalar os pacotes listados no pacote requirements.txt executando o comando abaixo na raiz do projeto.
      
  `pip install -r requirements.txt`


- Executar o projeto executando o comando abaixo na raiz do projeto.

    `python manage.py runserver`


Obs.: O projeto está utilizando o sqlite3 como base de dados, e foi disponibilizado no git junto com o projeto.
