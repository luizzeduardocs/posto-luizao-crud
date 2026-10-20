-- Criação da tabela de usuários
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(100) NOT NULL
);

-- Criação da tabela de abastecimentos (relacionada com usuários via chave estrangeira)
CREATE TABLE abastecimentos (
    id SERIAL PRIMARY KEY,
    cliente VARCHAR(100) NOT NULL,
    combustivel VARCHAR(50) NOT NULL,
    litros NUMERIC(10, 2) NOT NULL,
    valor_litro NUMERIC(10, 2) NOT NULL,
    total NUMERIC(10, 2) NOT NULL,
    pago BOOLEAN DEFAULT FALSE,
    usuario_id INT REFERENCES usuarios(id)
);

-- Inserção de usuário administrador padrão para testes
INSERT INTO usuarios (nome, email, senha) VALUES ('Administrador', 'admin@posto.com', '123');

-- Exemplo de consulta com filtro (utilizada no sistema)
-- SELECT * FROM abastecimentos WHERE combustivel = 'gasolina';