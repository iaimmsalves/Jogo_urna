import random

def jogo():
    urna = list(range(1, 21))  # Lista de bolas na urna
    alvo = random.choice(urna)  # Escolha aleatória do alvo inicial
    soma_alvo = alvo
    limite_alvo = 100  # Limite para o alvo não ultrapassar

    while soma_alvo <= limite_alvo:
        palpite = int(input("Digite seu palpite (entre 1 e 20): "))
        
        if palpite == alvo:
            print("Parabéns! Você acertou o alvo:", alvo)
            return True
        else:
            print("Você errou! O alvo era:", alvo)
            urna.remove(palpite)  # Remove o palpite da urna
            nova_bola = random.choice(urna)  # Escolhe uma nova bola
            soma_alvo += nova_bola  # Soma a nova bola ao alvo
            alvo = soma_alvo
            print("Novo alvo:", alvo)
    
    print("Você ultrapassou o limite de", limite_alvo, "e perdeu o jogo!")
    return False

if __name__ == "__main__":
    jogo()
