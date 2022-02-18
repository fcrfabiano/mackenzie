# A empresa local de abastecimento de água, a Saneamento Básico da Cidade (SBC), está promovendo uma campanha de conservação de água, distribuindo cartilhas e articulando ações que demonstrem a importância da água para a vida e para o meio ambiente. 
# Para incentivar mais ainda a economia de água, a SBC alterou os preços de seu fornecimento, de forma que, proporcionalmente, aqueles clientes que consumirem menos água paguem menos pelo metro cúbico.  
# Todo cliente paga mensalmente uma assinatura de R$ 7, que inclui uma franquia de 10m³ de água. Isto é, para qualquer consumo entre 0 e 10m³, o consumidor paga a mesma quantia de R$ 7 reais (note que o valor da assinatura deve ser pago mesmo que o consumidor não tenha consumido água).   
# Acima de 10m³, cada metro cúbico subsequente tem um valor diferente, dependendo da faixa de consumo. A SBC cobra apenas por quantidades inteiras de metros cúbicos consumidos. A tabela abaixo especifica o preço por metro cúbico para cada faixa de consumo:  

n = int  (input ("Consumo em metros cúbicos:")) 

if n <= 10: 

    conta = 7  

elif n>=11 and  n<=30: 

    conta = (n-10) * 1 + 7  

elif n>=31 and  n<=100: 

    conta = (n-30) * 2 + 27  

else: 

    conta = (n-100) * 5 + 167  

print(f'Valor  da conta = {conta}') 
