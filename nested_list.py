#lista annidata (alcuni elementi sono liste)

def count_leaf_nodes(input_list):
    #condizione terminale
    if len(input_list) == 0: #esempio banale
        return 0
    #condizione non terminale
    else:
        counter = 0
        for element in input_list:
            #controllo se element è una lista
            if type(element) == list:
                counter+=count_leaf_nodes(element)
                #richiama il metodo sulla lista trovata nella lista originaria
            else:
                counter+=1 #se non è una lista, aggiungo un elemento ai nodi
    return counter

if __name__ == '__main__':
    names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
    print(count_leaf_nodes(names)) #ce ne aspettiamo 10