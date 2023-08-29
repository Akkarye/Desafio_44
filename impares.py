valor_inserido = int(input("Digite um número inteiro: "))

print(f"Números ímpares de 1 até {valor_inserido}:")
for num in range(1, valor_inserido + 1, 2):
    print(num)
