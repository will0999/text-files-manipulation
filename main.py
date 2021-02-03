import random

arq= open('results.txt', 'a')
p=0

def maior(digit, rand):
    global p, nome, arq
    if digit > 100 or digit < 1:
        nome=input('Digite seu nome: ')
        print(f'{nome}: {p} pontos')
        arq.write(f'{nome}: {p} pontos\n')
        quit()
    else:
        if digit>rand:
            p+=10
        elif digit == rand:
            p+=40
        elif digit<rand:
            p-=5
while True:
    n=int(input('Digite um numero entre 1 e 100: '))
    numero= random.randint(1,100)
    maior (n, numero)