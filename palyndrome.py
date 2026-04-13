#controllo se una parola è palindroma

#metodo ricorsivo
def palyndrome(word):
    if len(word)<=1:
        return True
    else:
        return (word[0] == word[-1] and #controllo se la prima e l'ultima lettera della parola sono uguali
                palyndrome(word[1:-1])) #ritorna il palindromo della parola privata di prima e ultima lettera

#metodo non ricorsivo
def palyndrome_banale(word):
    return word[::-1]==word #controlla se la parola al contrario rimane uguale

if __name__=="__main__":
    print(palyndrome("casa"))
    print(palyndrome("civic"))

    print(palyndrome_banale("casa"))
    print(palyndrome_banale("civic"))