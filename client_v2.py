import rpyc
import sys
from random import randint
import time


def new_vector():
    size = int(input("Tamanho do vetor: "))
    vector = []
    for i in range(size):
        vector.append(i)
    return vector

server = sys.argv[1]


start = time.time()
c = rpyc.connect(server,18861)
c._config['sync_request_timeout'] = None

client_vector = new_vector()
# print(client_vector)
result, server_time = c.root.sum(client_vector)

end = time.time()
client_time = end - start

rtt_time = client_time - server_time
fraction = round(rtt_time / client_time, 4)

print(f"tempo total cliente: {client_time}")
print(f"tempo total servidor: {server_time}")
print(f"tempo total transporte na rede: {rtt_time}")
print(f"contribuição tempo de transporte para tempo do cliente: {fraction}")
