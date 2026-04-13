-- Sistema de Avaliação com Controle de Duplicidade
-- Script de criação do banco de dados

CREATE TABLE usuarios (
    id      INTEGER     PRIMARY KEY AUTOINCREMENT,
    nome    VARCHAR(100) NOT NULL,
    email   VARCHAR(150) NOT NULL UNIQUE
);

CREATE TABLE categorias (
    id      INTEGER      PRIMARY KEY AUTOINCREMENT,
    nome    VARCHAR(100) NOT NULL
);

CREATE TABLE itens (
    id           INTEGER      PRIMARY KEY AUTOINCREMENT,
    nome         VARCHAR(150) NOT NULL,
    categoria_id INTEGER      NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);

CREATE TABLE avaliacoes (
    id         INTEGER      PRIMARY KEY AUTOINCREMENT,
    nota       INTEGER      NOT NULL,
    comentario VARCHAR(300),
    usuario_id INTEGER      NOT NULL,
    item_id    INTEGER      NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (item_id)    REFERENCES itens(id),
    UNIQUE (usuario_id, item_id)
);