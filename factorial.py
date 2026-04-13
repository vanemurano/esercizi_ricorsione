#fattoriale di un numero (n!)

def factorial (n):
    #condizionae terminale
    if n==0 or n==1:
        return 1
    #condizione non terminale
    else:
        return n*factorial(n-1)

#growing call-stack: chiamare un metodo (che rimane aperto) a ogni iterazione
#unwinding call-stack: chiudere i metodi rimasti aperti, partendo dall'ultimo chiamato

if __name__=="__main__":
    N=5
    print(factorial(N))