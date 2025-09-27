Sistema de Gerenciamento de EPIs

Este projeto é um sistema de controle de empréstimo e fornecimento de Equipamentos de Proteção Individual (EPIs) para empresas de construção civil.
Foi desenvolvido em Python (Django) com SQLite3 como banco de dados, visando simplicidade e facilidade de uso.


Funcionalidades:

Dashboard com visão geral de colaboradores, equipamentos e movimentações.

Cadastro de Colaboradores (inserir, editar, excluir, listar, pesquisar).

Cadastro de Equipamentos (inserir, editar, excluir, listar, pesquisar).


Controle de EPIs:

Registrar entrega de equipamento a colaborador.

Informar data prevista de devolução (obrigatoriamente futura).

Atualizar status: Emprestado, Em Uso, Fornecido, Devolvido, Danificado, Perdido.

Campos extras para devolução (observações e data efetiva).

Relatórios por colaborador com histórico de empréstimos.

Interface Web responsiva feita com Bootstrap 5.


Estrutura do Projeto:

epi_manager_full_ready/
├── manage.py
├── requirements.txt
├── epi_manager/        # Configurações do projeto Django
├── core/               # App principal com models, views, forms, urls e templates
│   ├── migrations/
│   └── templates/core/ # Telas HTML
└── db.sqlite3          # Banco de dados (gerado após as migrações)


Instale as dependências:

pip install -r requirements.txt

Aplique as migrações:

python manage.py makemigrations
python manage.py migrate

Rode o servidor:

python manage.py runserver


Uso:

Abra o navegador em:

http://127.0.0.1:8000/

Dashboard: /

Colaboradores: /colaboradores/

Equipamentos: /equipamentos/

Controle de EPIs: /epi/

Relatórios: /relatorios/


Tecnologias Utilizadas:

Python 3.12+

Django 5

SQLite3

Bootstrap 5


Observações:

A data prevista de devolução deve ser posterior à data atual, caso contrário o cadastro não será aceito.

Status Devolvido, Danificado e Perdido só podem ser selecionados na edição de um registro.

O sistema não possui autenticação (login/logout), apenas exibe usuário fictício no menu lateral.


Licença:

Projeto acadêmico/educacional — uso livre para estudos e melhorias.