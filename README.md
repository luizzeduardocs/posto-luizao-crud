# Sistema Posto Luizão - CRUD em Python e PostgreSQL

Trabalho prático desenvolvido para a disciplina do Centro Universitário Santo Agostinho (UNIFA)[cite: 1, 2]. O sistema consiste em uma aplicação de terminal para gerenciamento de um posto de combustíveis[cite: 1, 2].

## 🚀 Tecnologias Utilizadas
* **Python** (Linguagem de programação)[cite: 2]
* **PostgreSQL** (Banco de dados relacional)[cite: 1]
* **Biblioteca Psycopg2** (Conexão entre Python e PostgreSQL)

## 📋 Funcionalidades (CRUD Completo)
* **Login de Usuário:** Acesso restrito ao sistema[cite: 1, 2].
* **Create (Cadastrar):** Registro de novos abastecimentos com cálculo automático do valor total[cite: 1, 2].
* **Read (Consultar):** Listagem de todos os abastecimentos cadastrados[cite: 1, 2].
* **Update (Atualizar):** Modificação de dados de abastecimento ou marcação de pagamento[cite: 1, 2].
* **Delete (Excluir):** Remoção de registros por ID[cite: 1, 2].
* **Filtros SQL:** Consulta filtrada por tipo de combustível[cite: 1, 2].

## ⚙️ Configuração do Banco de Dados
1. Abra o **pgAdmin** e crie um banco de dados chamado `posto_luizao`[cite: 2].
2. Execute o script contido no arquivo `banco.sql` na ferramenta de consulta (Query Tool) para criar as tabelas e o usuário administrador[cite: 2].

## 🔑 Credenciais para Teste
* **E-mail:** `admin@posto.com`[cite: 2]
* **Senha:** `123`[cite: 2]

## ▶️ Instruções para Execução
1. Certifique-se de ter o Python e a biblioteca `psycopg2` instalados.
2. No arquivo `conexao.py`, configure a senha do seu PostgreSQL.
3. Abra o terminal (CMD) na pasta do projeto e execute[cite: 2]:
   ```bash
   python main.py