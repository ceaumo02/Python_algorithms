import random
import collections

PALOS = ['Espadas', 'Corazones', 'Diamantes', 'Treboles']
VALORES = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def crear_baraja():
    barajas = []
    for palo in PALOS:

        for valor in VALORES:
            barajas.append((palo, valor))
    
    return barajas


def obtener_mano(barajas, tamano_mano):
    return random.sample(barajas, tamano_mano)
 

def coincidencias(mano, tamano_coincidencia):
    num_coincidencias = 0
    valores = []
    for carta in mano:
        valores.append(carta[1])
    counter = dict(collections.Counter(valores))
    for i in counter.values():
        if i == tamano_coincidencia:
            num_coincidencias += 1
    return num_coincidencias


def escalera(mano):
    valores = []
    for carta in mano:
        valores.append(carta[1])
    for i, val in enumerate(valores):
        if val == 'As':
            valores[i] = 1
        elif val == 'J':
            valores[i] = 11
        elif val == 'Q':
            valores[i] = 12
        elif val == 'K':
            valores[i] = 13
        else:
            valores[i] = int(val)
    
    valores = sorted(valores)
    escalera = True
    for i in range(len(valores)-1):
        if i == 0:
            if valores[0]==1 and valores[len(valores)-1]==13:
                pass
        elif valores[i]+1 != valores[i+1]:
            escalera = False
            break

    return escalera


def color(mano):
    palos = []
    for carta in mano:
        palos.append(carta[0])
    coincidencia = True
    for i in range(len(palos)-1):
        if palos[i] != palos[i+1]:
            coincidencia = False

    return coincidencia
    

def probabilidad_pares(intentos, barajas, tamano_mano):
    contar = 0
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        if coincidencias(mano, 2):
            contar += 1
    return contar/intentos
        

def probabilidad_un_par(intentos, barajas, tamano_mano):
    contar = 0
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        if coincidencias(mano, 2)==1:
            contar += 1
    return contar/intentos


def probabilidad_dos_pares(intentos, barajas, tamano_mano):
    contar = 0
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        if coincidencias(mano, 2)==2:
            contar += 1
    return contar/intentos


def probabilidad_trio(intentos, barajas, tamano_mano):
    contar = 0
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        if coincidencias(mano, 3):
            contar += 1
    return contar/intentos

def probabilidad_escalera(intentos, barajas, tamano_mano):
    contar = 0
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        if escalera(mano):
            contar += 1
    return contar/intentos


def probabilidad_color(intentos, barajas, tamano_mano):
    contar = 0
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        if color(mano):
            contar += 1
    return contar/intentos


def probabilidad_full(intentos, barajas, tamano_mano):
    contar = 0
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        if coincidencias(mano, 2) and coincidencias(mano, 3):
            contar += 1
    return contar/intentos


def probabilidad_poker(intentos, barajas, tamano_mano):
    contar = 0
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        if coincidencias(mano, 4):
            contar += 1
    return contar/intentos


def probabilidad_escalera_color(intentos, barajas, tamano_mano):
    contar = 0
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        if escalera(mano) and color(mano):
            contar += 1
    return contar/intentos


def probabilidad_escalera_real(intentos, barajas, tamano_mano):
    contar = 0
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        real = False
        for i, j in mano:
            if j == 'A':
                real = True
        if escalera(mano) and color(mano) and real:
            contar += 1
    return contar/intentos


if __name__ == "__main__":
    barajas = crear_baraja()
    tamano_mano = int(input('Cuántas cartas quieres: '))
    intentos = int(input('Cuántas veces quieres simular: '))
    print(f'Probabilidad de Pares: {probabilidad_pares(intentos, barajas, tamano_mano)}')
    print(f'Probabilidad de Un Par: {probabilidad_un_par(intentos, barajas, tamano_mano)}')
    print(f'Probabilidad de Dos Pares: {probabilidad_dos_pares(intentos, barajas, tamano_mano)}')
    print(f'Probabilidad de Trio: {probabilidad_trio(intentos, barajas, tamano_mano)}')
    print(f'Probabilidad de Escalera: {probabilidad_escalera(intentos, barajas, tamano_mano)}')
    print(f'Probabilidad de Color: {probabilidad_color(intentos, barajas, tamano_mano)}')
    print(f'Probabilidad de Full House: {probabilidad_full(intentos, barajas, tamano_mano)}')
    print(f'Probabilidad de Poker: {probabilidad_poker(intentos, barajas, tamano_mano)}')
    print(f'Probabilidad de Escalera de Color: {probabilidad_escalera_color(intentos, barajas, tamano_mano)}')
    print(f'Probabilidad de Flor Imperial: {probabilidad_escalera_real(intentos, barajas, tamano_mano)}')