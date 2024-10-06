#Criando um dicionário fictício de exemplo

pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

print(f"Meu dicionario de exemplo: {pessoa}")

#Acessando valores por chave
print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa['idade']}")
print(f"Cidade: {pessoa['cidade']}")

pessoa["sobrenome"] = "Takara"
print(f"Sobrenome: {pessoa['sobrenome']}")

pessoa["idade"] = 31
print(f"Idade Atualizada: {pessoa['idade']}")

print(f"Meu dicionario de exemplo: {pessoa}")

#Removendo um par chave-valor
del pessoa["sobrenome"]
print(f"Meu dicionario de exemplo: {pessoa}")

#Métodos: keys(), values(), items()
chaves = list(pessoa.keys())
print(f"Chaves do dicionario: {chaves}")
print(f"Primeira chave: {chaves[0]}")

#Método values
valores = list(pessoa.values())
print(f"Valores do dicionario: {valores[0]}")

#Método items
itens = list(pessoa.items())
print(f"Pares chave-valor do dicionario: {itens}")
print(f"Primeiro item: chave:{itens[0][0]}, valor:{itens[0][1]}")
