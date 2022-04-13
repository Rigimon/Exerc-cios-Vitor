#Exercício Par
print ("Identificar números ímpares")
n1 = int(input("Digite um número\n"))
if (n1%2 == 1):
    print ("Impar")
else:
    print ("Par")

#Exercício Salario
print ("Digite seu Salario")
cont = 0
while (cont < 5):
    sal = float(input())
    if (sal <= 1500):
        sal = sal-(sal*0.05)
    elif (sal <= 2000):
        sal = sal-(sal*0.1)
    elif (sal <= 2500):
        sal = sal-(sal*0.15)
    else:
        sal = sal-(sal*0.2)
    print (sal)
    cont = cont + 1
print ("Fim")

#Exercício teste
print ("Digite um Número")
num = int(input())
if (num > 10):
    for num in range(num,0-1,-1):
        print (num)
elif (num < 10):
    for num in range(num,11):
        print (num)
