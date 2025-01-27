<h1>Desafio 06</h1>

<p>A ideia desse desafio é criar uma API para um banco contendo operações para as tabelas de Pessoa Jurídica e Pessoa Física</p>

<p>Como tivemos um módulo completo, não vamos descrever detalhadamente rotas e propriedades dos registros a serem criadas, mas sim, as regras e requisitos que a API deve ter.</br>

O motivo disso é para vocês também exercitarem o desenvolvimento e a estruturação dessa parte. </p>

<p>Criação de um sistema bancário com clientes:</p>
<ul>
    <li>Pessoas Físicas</li>
    <li>Pessoas Jurídicas</li>
</ul>

<h2>Regras de Aplicação</h2>
<ul>
    <li>A aplicação deve estar conectada a um banco de dados <strong>QLite</strong></li>
    <li>O projeto deve conter uma interface <strong>Cliente</strong>, com métodos: Sacar dinheiro e Realizar extrato</li>
    <li>As controllers deve possuir testes unitários para garantir que estão funcionando conforme devem funcionar</li>
    <li>Deverá ser possível: <strong>Criar</strong> e <strong>listar</strong> usuários</li>
</ul>

<h2>Regras de Negócios</h2>
<ul>
    <li>O método <strong>"Sacar dinheiro"</strong> deve possuir um limite máximo menor em Pessoa Física do que para pessoa jurídica</li>
</ul>

<h2>Conceitos que pode praticar</h2>
<ul>
    <li>MVC</li>
    <li>Testes unitários (e quem sabe de integração 👀</li>
    <li>Criação e integração com banco de dados</li>
</ul>

<h2>Aviso!</h2>
<p>Regras para aplicação e regras de negócio são obrigatórias, porém a forma como vão ser implementadas ficam a cargo do desenvolvedor.</p>

<h2>Material Complementar</h2>
# Tabelas e Dados

As tabelas a seguir foram criadas para o projeto:

```sql
CREATE TABLE IF NOT EXISTS pessoa_fisica (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    renda_mensal REAL,
    idade INTEGER,
    nome_completo TEXT,
    celular TEXT,
    email TEXT,
    categoria TEXT,
    saldo REAL
);

CREATE TABLE IF NOT EXISTS pessoa_juridica (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    faturamento REAL,
    idade INTEGER,
    nome_fantasia TEXT,
    celular TEXT,
    email_corporativo TEXT,
    categoria TEXT,
    saldo REAL
);

INSERT INTO pessoa_fisica (renda_mensal, idade, nome_completo, celular, email, categoria, saldo)
VALUES
(5000.00, 35, 'João da Silva', '9999-8888', 'joao@example.com', 'Categoria A', 10000.00),
(4000.00, 45, 'Maria Oliveira', '7777-6666', 'maria@example.com', 'Categoria B', 15000.00),
(6000.00, 28, 'Pedro Santos', '5555-4444', 'pedro@example.com', 'Categoria C', 8000.00);

INSERT INTO pessoa_juridica (faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo)
VALUES
(100000.00, 10, 'Empresa XYZ', '1111-2222', 'contato@empresa.com', 'Categoria A', 50000.00),
(80000.00, 5, 'Empresa ABC', '3333-4444', 'contato@abc.com', 'Categoria B', 70000.00),
(120000.00, 8, 'Empresa 123', '5555-6666', 'contato@123.com', 'Categoria C', 90000.00);
