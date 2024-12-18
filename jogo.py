from Personagens import Heroi, Vilao
import random

def menu():
    personagens = []
    while True:
        print("""\n===Dugeons & Dragons===\n
                1. Criar personagens\n
                2. Mostrar personagens\n
                3. Iniciar duelo\n
                4. Realizar torneio\n
                5. Alimentar personagem\n
                6. Interagir\n
                7. Sair""")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            criar_personagem(personagens)
        elif opcao == "2":
            mostrar_personagens(personagens)
        elif opcao == "3":
            iniciar_duelo(personagens)
        elif opcao == "4":
            realizar_torneio(personagens)
        elif opcao == "5":
            alimentar_personagem(personagens)
        elif opcao == "6":
            interagir(personagens)
        elif opcao == "7":
            print("Saindo do jogo. Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.")

def criar_personagem(personagens):
    lado = input("Criar Herói ou Vilão? (H/V): ").strip().upper()
    name = input("Digite o nome do personagem: ").strip()
    if lado == "H":
        personagens.append(Heroi(name))
        print(f"Herói '{name}' criado com sucesso!")
    elif lado == "V":
        personagens.append(Vilao(name))
        print(f"Vilão '{name}' criado com sucesso!")
    else:
        print("Tipo inválido. Escolha 'H' ou 'V'.")

def mostrar_personagens(personagens):
    if not personagens:
        print("Nenhum personagem criado ainda.")
        return
    for i, personagem in enumerate(personagens):
        print(f"{i + 1}. Nome: {personagem.name}, Energia: {personagem.energy}, Histórico: {personagem.historico_batalhas}")

def iniciar_duelo(personagens):
    if len(personagens) < 2:
        print("É necessário pelo menos dois personagens para um duelo.")
        return

    mostrar_personagens(personagens)
    try:
        index1 = int(input("Escolha o número do primeiro personagem: ")) - 1
        index2 = int(input("Escolha o número do segundo personagem: ")) - 1

        p1 = personagens[index1]
        p2 = personagens[index2]

        if p1 == p2:
            print("Você não pode escolher o mesmo personagem duas vezes.")
            return

        p1.lutar(p2)
    except (ValueError, IndexError):
        print("Entrada inválida. Tente novamente.")

def realizar_torneio(personagens):
    if len(personagens) < 2:
        print("É necessário pelo menos dois personagens para um torneio.")
        return

    participantes = personagens[:]

    while len(participantes) > 1:
        p1 = random.choice(participantes)
        p2 = random.choice(participantes)

        if p1 != p2:
            print(f"Duelo entre {p1.name} e {p2.name}!")
            p1.lutar(p2)
            if p1.energy == 0:
                participantes.remove(p1)
            if p2.energy == 0:
                participantes.remove(p2)

    vencedor = participantes[0]
    print(f"O vencedor do torneio é {vencedor.name} com {vencedor.energy} de energia!")
    print("Histórico de batalhas do vencedor:")
    print(vencedor.historico_batalhas)

def alimentar_personagem(personagens):
    mostrar_personagens(personagens)
    try:
        index = int(input("Escolha o número do personagem para alimentar: ")) - 1
        personagem = personagens[index]

        if personagem.energy == 0:
            print(f"{personagem.name} está morto e não pode ser alimentado.")
            return

        if isinstance(personagem, Heroi):
            personagem.incremento(2)
        elif isinstance(personagem, Vilao):
            personagem.incremento(3)

        print(f"{personagem.name} foi alimentado e agora tem {personagem.energy} de energia.")
    except (ValueError, IndexError):
        print("Entrada inválida. Tente novamente.")

def interagir(personagens):
    mostrar_personagens(personagens)
    try:
        index1 = int(input("Escolha o número do personagem que iniciará a interação: ")) - 1
        index2 = int(input("Escolha o número do personagem alvo da interação: ")) - 1

        p1 = personagens[index1]
        p2 = personagens[index2]

        if p1 == p2:
            print("Um personagem não pode interagir consigo mesmo.")
            return

        p1.interagir(p2)
    except (ValueError, IndexError):
        print("Entrada inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
