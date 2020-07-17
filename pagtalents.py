import random

numero = random.randint(0, 10000)

fibonacci = [0]

valorAnterior = 0
valorAtual = 1
while len(fibonacci) < 1000:
    fibonacci.append(valorAtual)
    valorAnterior, valorAtual = valorAtual, valorAtual + valorAnterior

if numero in fibonacci:
    print(numero, ' pertence a sequência de Fibonacci')
else:
    print(numero, ' não pertence a sequência de Fibonacci')  
