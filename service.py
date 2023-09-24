import rpyc
import time
class MyService(rpyc.Service):
    def on_connect(self, conn):
    # código que é executado quando uma conexão é iniciada, casoseja necessário
        pass
    def on_disconnect(self, conn):
    # código que é executado quando uma conexão é finalizada,caso seja necessário
        pass

    def exposed_sum(self, vector):
        start = time.time()
        total = sum(vector)
        end = time.time()
        total_time = end-start
        
        print(f"resultado: {total}")
        print(f"tempo de processamento: {total_time}")
        
        return total, total_time

    def exposed_get_answer(self): # este é um método exposto
        return 42
    exposed_the_real_answer_though = 43 # este é um atributo exposto
        
    def get_question(self): # este método não é exposto
        return "Qual é a cor do cavalo branco de Napoleão?"
    #Para iniciar o servidor
if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()