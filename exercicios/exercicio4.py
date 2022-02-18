# Faça um programa em Python que receba o custo (valor em reais) de um espetáculo teatral e o preço do convite (valor em reais) desse espetáculo. Esse programa deve calcular e mostrar:  
# a) A quantidade de convites que devem ser vendidos para que, pelo menos, o custo do espetáculo seja alcançado.  
# b) A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%. 
# Observe que as quantidades calculadas devem ser um número inteiro, portanto, o resultado da quantidade de convites deve ser arredondada para cima, usando a função matemática apropriada em Python. 
import math

def calcConvites (precoEspetaculo, precoConvite):
    total = precoEspetaculo / precoConvite
    return math.ceil(total)

def calcLucro (precoEspetaculo, precoConvite):
    total = 1.23 * precoEspetaculo / precoConvite
    return math.ceil(total)

espetaculo = float(input('Preço do espetáculo:'))
convite = float(input('Preço do convite:'))
print('Custo do espetáculo: ', calcConvites(espetaculo, convite))
print('Lucro de 23%: ', calcLucro(espetaculo, convite))