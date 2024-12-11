# 4. Imprimir los primeros 10 números pares

print("imprimir los primeros 10 numeros pares")
n = int(input("ingresa el numero desde donde empezar a buscar pares"))

contador = 0

while contador < 10:
    if n % 2 == 0:
        print(n)
        contador += 1
    n += 1
