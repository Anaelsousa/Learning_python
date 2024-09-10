from random import randint

chanse = 5
n1 = randint(1, 10)

while chanse > 0:
    n2 = int(input(f"Tente adivinhar o número entre 1 e 10.\nVocê tem {chanse} tentativas."))
    chanse -=1
    if n2 > n1 and chanse > 0:
        print("Tente um número mais baixo.")
    elif n2 < n1 and chanse > 0:
        print("Tente um número mais alto.")
    elif n2 == n1:
        print("Parabens, você acertou.")
        break
 
if n2 != n1:
    print("Suas chanses acabaram.\nVocê perdeu.")
