def run():
    LIMITE = 1000000

    contador = 2 
    potencia_2 = 2**contador
    
    while potencia_2 < LIMITE:
        print('2 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2)) 
        contador = contador + 1
        potencia_2 = 2**contador

if __name__ == '__main__':
    run()