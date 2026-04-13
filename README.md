# Sistema de Avaliação com Controle de Duplicidade

## Descrição

Sistema backend desenvolvido em Python com Flask para gerenciamento de avaliações de itens como filmes, produtos ou locais. Usuários podem se cadastrar, cadastrar itens categorizados e registrar avaliações com nota de 1 a 5 e comentário opcional. O sistema garante que um mesmo usuário não possa avaliar o mesmo item mais de uma vez, assegurando a integridade dos dados.

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

---

## Estrutura do projeto

```
Sistema_Avaliacoes/
├── app/
│   ├── __init__.py       # Inicialização do app Flask e configurações
│   ├── models.py         # Definição das tabelas do banco de dados
│   └── routes.py         # Rotas e lógica da aplicação
├── migrations/           # Versionamento do banco de dados
├── instance/
│   └── avaliacoes.db     # Banco de dados SQLite (gerado automaticamente)
├── .env                  # Variáveis de ambiente (não versionado)
├── .gitignore            # Arquivos ignorados pelo Git
├── requirements.txt      # Dependências do projeto
├── run.py                # Ponto de entrada da aplicação
└── README.md
```

---

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

## Boas práticas adotadas

- Uso de ambiente virtual (`venv`) para isolamento de dependências
- Variáveis sensíveis armazenadas no arquivo `.env`
- Arquivo `.gitignore` configurado para não versionar `venv/` e `.env`
- Banco de dados criado e versionado via migrations com Flask-Migrate
- Código organizado em módulos separados por responsabilidade
