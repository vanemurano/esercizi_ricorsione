#funzione binomiale: ( n ) = ( n-1 ) + ( n-1 )
#                    ( m )   ( m-1 )   (  m  )
#  ( n ) = 1
#  ( n )

def binomial(n,m):
    #condizione terminale
    if m==0 or m==n:
        return 1
    #condizione non terminale
    else:
        return (binomial(n-1,m-1)+binomial(n-1,m))
    #lascio che sia l'algoritmo a risolvere

if __name__=="__main__":
    n=6
    m=3
    print(binomial(n,m))

