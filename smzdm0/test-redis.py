import redis

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

r.incrbyfloat('visit:12306:total', amount=0.1)

print(r.get('visit:12306:total'))

for i in range(10):
	r.incrby('visit:12306:total', amount=0.1)
	print(r.get('visit:12306:total'))

