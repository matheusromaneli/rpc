
import rpyc
import sys

def new_vector():
    size = int(input("Insira o tamanho do vetor:"))
    vector = []
    for i in range(size):
        vector.append(i)
    return vector

server = sys.argv[1]

c = rpyc.connect(server,18861)

client_vector = new_vector()
print(c.root.sum(client_vector))



