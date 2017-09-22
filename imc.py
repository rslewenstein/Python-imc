#coding: utf-8

print("Calculadora de IMC")
print()

peso = float(input("Qual o seu peso: "))
alt = float(input("Qual a sua altura (use o ponto . x.xx ): "))
print()

def calcImc(p, a):

        imc = p / (a * a)
       # return print (str("Seu IMC é: %.2f" % imc))
        print (str("Seu IMC é: %.2f" % imc))
        print()
        
        if (imc < 18.5):
                print("Você está abaixo do peso!")
        elif (imc >= 18.6) and (imc <= 24.9):
                print("Peso ideal!")
        elif (imc >= 25.0) and (imc <= 29.9):
                print("Levemente acima do peso!")
        elif (imc >= 30.0) and (imc <= 34.9):
                print("Obesidade grau I")
        elif (imc >= 35.0) and (imc <= 39.9):
                print("Obesidade grau II! (severa)")
        else:
                print("Obesidade III (mórbida)")

calcImc(peso ,alt)
