'''
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.

Exemplo de Entrada
6
-5

Exemplo de Saída
5
'''


x = int(input())
y = int(input())
soma = 0
for i in range(min (x, y)+1, max (x, y)):
    if i % 2 == 1:
        soma += i
print (soma)
    
