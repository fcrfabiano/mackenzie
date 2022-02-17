n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))

sum = n1+n2
sub = n1-n2
mult = n1*n2
div = n1/n2
divTrunc = n1//n2
rest = n1%n2
exp = n1**n2

print(f'Soma de {n1} + {n2} = {sum}')
print(f'Subtração de {n1} - {n2} = {sub}')
print(f'Multiplicação de {n1} x {n2} = {mult}')
print(f'Divisão de {n1} / {n2} = {div}')
print(f'Divisão Truncada de {n1} / {n2} = {divTrunc}')
print(f'Resto da divisão de {n1} % {n2} = {rest}')
print(f'Exponenciação de {n1} elevado por {n2} = {exp}')