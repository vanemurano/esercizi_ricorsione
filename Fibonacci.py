#la sequenza di Fibonacci è una sequenza di numeri in cui ognuno è la somma dei due precedenti
from functools import lru_cache
from time import time


class Fibonacci:
    def __init__(self):
        self.cache={0:0, 1:1} #cache per memorizzare il risultato per ogni n

    #funzione ricorsiva
    #il tempo aumenta esponenzialmente all'aumentare di n, perché eseguo tante volte la stessa funzione
    def calcola_elemento(self, n):
        #casi terminali
        if n==0:
            return 0
        elif n==1:
            return 1
        #caso non terminale
        else:
            return (self.calcola_elemento(n-1)+
                    self.calcola_elemento(n-2))

    #utilizzo una memoria volatile per velocizzare i calcoli
    #tecnica MEMOIZATION: memorizzo i risultati parziali dei sottoproblemi
    def calcola_elemento_cache(self, n):
        #se ho già la soluzione per questo n la prendo dalla cache
        if self.cache.get(n) is not None:
            return self.cache[n]
        #altrimenti vado avanti con la ricorsione
        else:
            self.cache[n] = (self.calcola_elemento_cache(n-1) +
            self.calcola_elemento_cache(n-2))
        return self.cache[n]

    @lru_cache(maxsize=None) #decoratore che implementa automaticamente la cache con maxsize specificata
    def calcola_elemento_lru(self, n):
        #casi terminali
        if n==0:
            return 0
        elif n==1:
            return 1
        #caso non terminale
        else:
            return (self.calcola_elemento_lru(n-1)+
                    self.calcola_elemento_lru(n-2))


if __name__=="__main__":
    N=40
    fib=Fibonacci()
    #check tempo
    start_time=time()
    print(fib.calcola_elemento(N))
    end_time=time()
    print(f"Elapsed time - recursion: {end_time-start_time}")
    start_time = time()
    print(fib.calcola_elemento_cache(N))
    end_time = time()
    print(f"Elapsed time - cache: {end_time-start_time}")
    print(fib.calcola_elemento_lru(N))
    end_time = time()
    print(f"Elapsed time - cache: {end_time-start_time}")