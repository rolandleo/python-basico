menu = """
Bienvenido al conversor de monedas

1 - soles peruanos
2 - pesos mexicanos
3 - pesos argentinos

"""
opcion = input(menu)

if opcion == 1:
    soles = input("¿cuantos soloes peruanos tienes?: ")
    soles = float(soles)
    valor_dolar = 3.70
    dolares = soles / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + "dòlares")
elif opcion == 2:
    pesos = input("¿cuantos pesos mexixanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3.85
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + "dòlares")
elif opcion == 3:
    pesos = input("¿cuantos pesos argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3.90
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + "dòlares")
else:
    print('Ingresa una opciòn correcta por favor')


