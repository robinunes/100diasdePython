#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print ("Bem vindo a calculadora de gorgeta")
total_conta = input ("Qual foi o valor total da conta?")
porcentagem = input ("Qual a porcentagem da gorgeta? 10%, 12% ou 15% ")
pessoas = input ("A gorgeta será dividida entre quantas pessoas?")

total = float (total_conta)
percentual = int (porcentagem)
num_pessoas = int (pessoas)

conta_gorgeta = total * percentual/100
resultado_final = conta_gorgeta / num_pessoas
fim = round (resultado_final, 2)
print (f"Cada pessoa deverá pagar: R${fim}" )