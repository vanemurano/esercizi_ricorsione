#piccolo programma che realizza un countdown in loop

from time import sleep #fa una pausa di () secondi

#metodo iterativo
def countdown (n):
    while n>=0:
        print(n)
        sleep(1)
        n-=1

#metodo ricorsivo
#se non finisce mai, risulta un RecursiveError dopo un tot di iterazioni
def countdown_recursive(n):
    #condizione terminale
    if n==0:
        print("Stop")
    #condizione non terminale
    else:
        print(n)
        sleep(1)
        countdown_recursive(n-1)

#nel main eseguo il countdown partendo da 10
#ALL'ESAME devo fare i controlli sul numero
if __name__=="__main__":
    N=4
    countdown_recursive(N)
