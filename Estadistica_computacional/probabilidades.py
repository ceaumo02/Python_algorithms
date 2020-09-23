import random

def tirar_dados(numero_de_tiros, numero_de_dados):
    secuencia_de_tiros = []
    if numero_de_dados <= 0:
        numero_de_dados = 1

    for _ in range(numero_de_tiros):
        tiro = 0
        for _ in range(numero_de_dados):
            tiro += random.choice([1,2,3,4,5,6])
        secuencia_de_tiros.append(tiro)

    return secuencia_de_tiros   

def probabilidad_existir(tiros, numero_de_intentos,valor_del_dado_buscado):
    

    tiros_con_valor_buscado = 0
    for tiro in tiros:
        if valor_buscado in tiro:
            tiros_con_valor_buscado += 1

    probabiblidad_de_tiros_con_1 = tiros_con_valor_buscado / numero_de_intentos
    print(f'Cual es la probabiblidad de obtener por lo menos un {valor_buscado} en {numero_de__tiros} = {probabiblidad_de_tiros_con_1}')
    

def main(numero_de_tiros, numero_de_intentos, numero_de_dados, valor_buscado):
    tiros = []
    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dados(numero_de_tiros, numero_de_dados)
        tiros.append(secuencia_de_tiros)


    probabilidad_existir(tiros, numero_de_intentos, valor_buscado)

    

if __name__ == "__main__":
    numero_de__tiros = int(input('Cuantos tiros del dado: '))
    numero_de_intentos = int(input('Cuantas veces correra la simulacion: '))
    numero_de_dados = int(input('Numero de dados: '))
    valor_buscado = int(input('Cual es el valor buscado: '))

    main(numero_de__tiros, numero_de_intentos, numero_de_dados, valor_buscado)