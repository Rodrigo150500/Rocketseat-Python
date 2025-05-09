import redis

redis_conn = redis.Redis(host="localhost", port=6379, db=0)

#insert and update
redis_conn.set("minha_chave", "meu_valor")

#select
meu_valor = redis_conn.get("minha_chave").decode("utf-8")
#transformando de bytes -> string
print(meu_valor)

#delete
redis_conn.delete("minha_chave")


###Exemplo de dicionario para hash
meu_hash = { #chave
    "nome": "joao", #field: values
    "idade": 18,
    "cidade": "sao paulo"
}

#insert e update
redis_conn.hset("meu_hash", "nome", "joao")
redis_conn.hset("meu_hash", "idade", "18")
redis_conn.hset("meu_hash", "cidade", "macapa")

#get data
valor_1 = redis_conn.hget("meu_hash", "nome").decode("utf-8")

#delete hash
redis_conn.hdel("meu_hash", "nome")

#busca por dados se existem
minha_chave =redis_conn.exists("minha_chave")
print(minha_chave)

minha_chave_2 = redis_conn.hexists("meu_hash", "cidade")
print(minha_chave_2)

#### Set data with TTL
# TTL is Time to Live - Significa o quanto tempo em segundos o dados ficarão no banco antes de serem deletados

redis_conn.set("chave_del", "dados para serem deletados", 12)
redis_conn.expire("meu_hash", 20)