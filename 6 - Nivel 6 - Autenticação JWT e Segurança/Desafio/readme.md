<h1>Desafio 07</h1>

<h2>Objetivo</h2>

<p>Vamos desenvolver uma API de pedidos com JWT: Desenvolva uma API que utilize JWT para autenticação e autorização. A API deve ter diferentes endpoints que só podem ser acessados por usuários que tenham autenticação via token</p>

<h2>Sobre o token JWT</h2>
<p>Ao fazer login, o usuário recebe um token JWT que contém as seguintes informações:</p>
<ul>
    <li><strong>ID do Usuário: </strong>Identificador único do usuário na base de dados</li>
    <li><strong>Nome de Usuário: </strong>Nome do usuário para exibição.</li>
    <li><strong>Token JWT: </strong>Token necessário para ser colocado na requisição</li>
</ul>

<h2>Sobre os endpoints</h2>
<p>Deve ser possível listar os pedidos do usuário autenticado e adicionar um novo pedido. Um usuário só pode ter acesso aos seus pedidos e não de outros.

Como pode imaginar, você deverá utilizar seus conhecimentos sobre HTTP para poder pensar na lógica e em qual método irá suprir a implementação necessária.</p>

<h2>Sobre as tabelas no banco</h2>
<p>Os usuários devem possuir um id, o username e a senha que deverá ser armazenada.

Os pedidos por sua vez, deve ter uma relação com os usuários, descrição, id e a data na qual o pedido foi criado no banco.</p>