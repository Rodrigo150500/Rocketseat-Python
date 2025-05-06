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