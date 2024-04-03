sql
-- Criação do banco de dados
CREATE DATABASE Biblioteca;

-- Utilização do banco de dados
USE Biblioteca;

-- Criação da tabela Livros
CREATE TABLE Livros (
    ID INT PRIMARY KEY,
    Titulo VARCHAR(100),
    Autor VARCHAR(100),
    AnoPublicacao INT,
    Genero VARCHAR(50)
);

-- Inserção de registros na tabela Livros
INSERT INTO Livros (ID, Titulo, Autor, AnoPublicacao, Genero)
VALUES
    (1, 'Dom Quixote', 'Miguel de Cervantes', 1605, 'Romance'),
    (2, '1984', 'George Orwell', 1949, 'Ficção Distópica'),
    (3, 'O Senhor dos Anéis', 'J.R.R. Tolkien', 1954, 'Fantasia'),
    (4, 'Crime e Castigo', 'Fiódor Dostoiévski', 1866, 'Romance'),
    (5, 'Orgulho e Preconceito', 'Jane Austen', 1813, 'Romance');

-- Criação da tabela Autores
CREATE TABLE Autores (
    ID INT PRIMARY KEY,
    Nome VARCHAR(100),
    Nacionalidade VARCHAR(50),
    DataNascimento DATE
);

-- Inserção de registros na tabela Autores
INSERT INTO Autores (ID, Nome, Nacionalidade, DataNascimento)
VALUES
    (1, 'Miguel de Cervantes', 'Espanha', '1547-09-29'),
    (2, 'George Orwell', 'Inglaterra', '1903-06-25'),
    (3, 'J.R.R. Tolkien', 'Inglaterra', '1892-01-03'),
    (4, 'Fiódor Dostoiévski', 'Rússia', '1821-11-11'),
    (5, 'Jane Austen', 'Inglaterra', '1775-12-16');
