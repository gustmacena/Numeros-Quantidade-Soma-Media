# programa que leia números inteiros do teclado.
# O programa deve ler os números até que o usuário digite 0 (zero).
# No final da execução, exiba a quantidade de números digitados não
# levando em consideração o zero, assim como a soma e a média aritmética.
s = 0
q = 0
while True:
    n = int(input("Digite um número inteiro:"))
    if n == 0:
        break
    s = s + n
    q = q + 1
print(f"Quantidade de números digitados: {q}")
print(f"Soma: {s}")
print(f"Média: {s / q:.2f}")
