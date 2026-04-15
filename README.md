# Sistema de Avaliação com Controle de Duplicidade

## Descrição

Sistema web completo (full stack) desenvolvido em Python com Flask, com interface frontend para interação do usuário. O sistema serve para gerenciamento de avaliações de itens como filmes, produtos ou locais. Usuários podem se cadastrar, cadastrar itens categorizados e registrar avaliações com nota de 1 a 5 e comentário opcional. O sistema garante que um mesmo usuário não possa avaliar o mesmo item mais de uma vez, assegurando a integridade dos dados.

## Dupla

- Nome: GUSTAVO BARBOSA — RA: 22506610
- Nome: FRED GABRIEL — RA: 22511576

---

## Tecnologias utilizadas

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite
- python-dotenv
- HTML5
- CSS3
- JavaScript

---

## Estrutura do projeto

```
Sistema_Avaliacoes/
├── app/
│   ├── __init__.py              # Inicialização do app Flask e configurações
│   ├── models.py                # Definição das tabelas do banco de dados
│   ├── routes.py                # Rotas e lógica da aplicação
│   ├── templates/               # Páginas HTML (frontend)
│   │   ├── index.html
│   │   ├── usuarios.html
│   │   ├── categorias.html
│   │   ├── itens.html
│   │   └── avaliacoes.html
│   └── static/                  # Arquivos estáticos (CSS/JS)
│       ├── css/
│       └── js/
├── migrations/                  # Versionamento do banco de dados
├── instance/
│   └── avaliacoes.db            # Banco de dados SQLite (gerado automaticamente)
├── .env                         # Variáveis de ambiente (não versionado)
├── .gitignore                   # Arquivos ignorados pelo Git
├── requirements.txt             # Dependências do projeto
├── run.py                       # Ponto de entrada da aplicação
└── README.md
```

---

## Interface do sistema

O sistema possui uma interface web acessível pelo navegador, permitindo:

- Cadastro e gerenciamento de usuários
- Cadastro de categorias
- Cadastro de itens
- Registro de avaliações
- Navegação entre páginas via menu

As páginas são renderizadas pelo Flask utilizando templates HTML e interagem com o backend por meio de requisições HTTP (Fetch API).


## Banco de dados

O projeto possui 4 tabelas:

### `usuarios`
Armazena os usuários do sistema.

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | Integer | Chave primária |
| nome | String(100) | Nome do usuário |
| email | String(150) | E-mail único do usuário |

### `categorias`
Armazena os tipos de itens disponíveis para avaliação.

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | Integer | Chave primária |
| nome | String(100) | Nome da categoria (ex: Filmes, Produtos) |

### `itens`
Armazena os itens que podem ser avaliados.

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | Integer | Chave primária |
| nome | String(150) | Nome do item |
| categoria_id | Integer | Chave estrangeira para categorias |

### `avaliacoes`
Armazena as avaliações feitas pelos usuários.

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | Integer | Chave primária |
| nota | Integer | Nota de 1 a 5 |
| comentario | String(300) | Comentário opcional |
| usuario_id | Integer | Chave estrangeira para usuarios |
| item_id | Integer | Chave estrangeira para itens |

> A combinação de `usuario_id` e `item_id` é única — um usuário não pode avaliar o mesmo item duas vezes.

---

## Regras de negócio

1. **Controle de duplicidade:** um usuário não pode registrar mais de uma avaliação para o mesmo item. Caso tente, o sistema retorna erro `409 Conflict`.
2. **Validação de nota:** a nota deve ser um número inteiro entre 1 e 5. Notas fora desse intervalo retornam erro `400 Bad Request`.

---

## Rotas disponíveis

### Usuários

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/usuarios` | Lista todos os usuários |
| POST | `/usuarios` | Cria um novo usuário |
| PUT | `/usuarios/<id>` | Atualiza um usuário existente |
| DELETE | `/usuarios/<id>` | Remove um usuário |

### Categorias

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/categorias` | Lista todas as categorias |
| POST | `/categorias` | Cria uma nova categoria |
| PUT | `/categorias/<id>` | Atualiza uma categoria existente |
| DELETE | `/categorias/<id>` | Remove uma categoria |

### Itens

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/itens` | Lista todos os itens |
| POST | `/itens` | Cria um novo item |
| PUT | `/itens/<id>` | Atualiza um item existente |
| DELETE | `/itens/<id>` | Remove um item |

### Avaliações

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/avaliacoes` | Lista todas as avaliações |
| POST | `/avaliacoes` | Registra uma nova avaliação |
| PUT | `/avaliacoes/<id>` | Atualiza uma avaliação existente |
| DELETE | `/avaliacoes/<id>` | Remove uma avaliação |

---


## Como executar o projeto

1. Clone o repositório
2. Crie e ative o ambiente virtual:
   - python -m venv venv
   - venv\Scripts\activate (Windows)
3. Instale as dependências:
   - pip install -r requirements.txt
4. Crie o arquivo .env com:
   - DATABASE_URL=sqlite:///avaliacoes.db
   - SECRET_KEY=projeto_ceub_2026
5. Rode as migrations:
   - flask db upgrade
6. Inicie o servidor:
   - flask run

---

## Acesso ao sistema

Após iniciar o servidor, acesse no navegador:

http://127.0.0.1:5000/

Exemplos de páginas:

- /page/usuarios
- /page/categorias
- /page/itens
- /page/avaliacoes

> Importante: não abrir os arquivos HTML diretamente, sempre acessar via servidor Flask.

---


## Boas práticas adotadas

- Uso de ambiente virtual (`venv`) para isolamento de dependências
- Variáveis sensíveis armazenadas no arquivo `.env`
- Arquivo `.gitignore` configurado para não versionar `venv/` e `.env`
- Banco de dados criado e versionado via migrations com Flask-Migrate
- Código organizado em módulos separados por responsabilidade

---


## Screenshots

### Página de Início
<p align="center">
  <img src="https://i.pinimg.com/736x/1a/93/eb/1a93eb1ed50e422b0a929039f0dcdc4b.jpg" width="600"/>
</p>

### Página de Usuários
<p align="center">
  <img src="https://i.pinimg.com/736x/73/13/6e/73136ebd71cb1a10208aba8a00e2d87f.jpg" width="600"/>
</p>

### Página de Categorias
<p align="center">
  <img src="https://i.pinimg.com/736x/27/fd/3e/27fd3e1fd62f8e716d07ff4e14ae1448.jpg" width="600"/>
</p>

### Página de Itens
<p align="center">
  <img src="https://i.pinimg.com/736x/81/13/62/811362d143c3cab92a34a4912b4ff0e6.jpg" width="600"/>
</p>

### Página de Avaliações
<p align="center">
  <img src="https://i.pinimg.com/736x/73/cd/bd/73cdbd700073d75b2e5db8445fdf98a5.jpg" width="600"/>
</p>
