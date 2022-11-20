numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'terze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    usuario = int(input("Digite um numero de 0 a 20: "))
    if 0<= usuario <= 20:
        break
    else:
        print('Tente novamente')

    
print(numeros[usuario])