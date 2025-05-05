<h1>Projeto</h1>

<h2>API para venda de produtos</h2>
--> Uso em cache

<h2> Funcionalidades</h2>

- Registrar um produto em banco SQL e em Cache
- Buscar um produto salvando-o em Cache

- A API fará conexão com dois banco de dados, redis e SQL.

<h3>Na requisição de busca funcionará da seguinte forma:</h3>
- Haverá uma busca primeiro no redis
- Caso não encontre ele passa a buscar no SQL
- Assim que achado ele escreve no redis para que caso seja necessários já faça a busca direto no redis

<h3>Inserção de dados</h3>
- A inserção ocorre primeiro no SQL
- Depois no redis