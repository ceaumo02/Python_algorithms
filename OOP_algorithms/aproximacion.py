import time

objetivo = int(input('Escoge un número: '))
epsilon = 0.0001
paso = epsilon**2
respuesta = 0.0
# num = 0

start = time.time()

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    # print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso
    # num += 1

# end = time.time()
# tiempo = round((end - start), 2)

#print(f'Para encontrár la respuesta con margen de error de {epsilon*100}%, hizo {num} iteraciones y duró {tiempo} segundos')

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontró la raíz cuadrada de {objetivo}')
else:
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')
