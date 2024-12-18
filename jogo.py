from Personagens import Heroi, Vilao

def menu():
    personagens=[]
    while True:
        print("""\n===Dugeons & Dragons===\n
                1. Criar personagens\n
                2. Mostrar personagens\n
                3. Iniciar duelo\n
                4. Realizar torneio\n
                5. Alimentar personagem\n
                6. Interagir\n
                7. Sair""")
        opcao=input("Escolha uma opção: ")
        if opcao=="1":
            criar_personagem(personagens)
        elif opcao=="2":
            mostrar_personagens(personagens)
        elif opcao=="3":
            iniciar_duelo(personagens)
        elif opcao=="4":
            realizar_torneio(personagens)
        elif opcao=="5":
            alimentar_personagem(personagens)
        elif opcao=="6":
            interagir(personagens)
        elif opcao=="7":
            print("Saindo do jogo. Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.")

def criar_personagem(personagens):
    lado=input("Criar Herói ou Vilão? (M/V): ").strip().upper()
    name=input("Digite o nome do personagem: ").strip()
    if lado == "M":
        personagens.append(Heroi(name))
        print(f"Herói '{name}' criado com sucesso!")
    elif lado == "V":
        personagens.append(Vilao(name))
        print(f"Vilão '{name}' criado com sucesso!")
    else:
        print("Tipo inválido. Escolha 'M' ou 'V'.")

def mostrar_personagens(personagens):
    if not personagens:
        print("Nenhum personagem criado ainda.")
        return
    for personagem in personagens:
        print(f"Nome: {personagem.name}, Energia: {personagem.energy}, Histórico: {personagem.historico_batalhas}")

def iniciar_duelo(personagens):
    if len(personagens) < 2:
        print("É necessário pelo menos dois personagens para um duelo.")
        return
    name1=input("Digite o nome do primeiro personagem: ").strip()
    name2=input("Digite o nome do segundo personagem: ").strip()
    p1=next((p for p in personagens if p.name==name1), None)
    p2=next((p for p in personagens if p.name==name2), None)
    if not p1 or not p2:
        print("Um ou ambos os personagens não foram encontrados.")
        return
    p1.lutar(p2)

def realizar_torneio(personagens):
    if len(personagens)<2:
        print("É necessário pelo menos dois personagens para um torneio.")
        return
    while len(personagens)>1:
        p1=random.choice(personagens)
        p2=random.choice(personagens)
        if p1!=p2:
            print(f"Duelo entre {p1.name} e {p2.name}!")
            p1.lutar(p2)
            if p1.energy==0:
                personagens.remove(p1)
            if p2.energy==0:
                personagens.remove(p2)
    vencedor=personagens[0]
    print(f"O vencedor do torneio é {vencedor.name} com {vencedor.energy} de energia!")
    print("Histórico de batalhas do vencedor:")
    print(vencedor.historico_batalhas)

def alimentar_personagem(personagens):
    name=input("Digite o nome do personagem para alimentar: ").strip()
    personagem=next((p for p in personagens if p.name==name), None)
    if not personagem:
        print("Personagem não encontrado.")
        return
    if personagem.energy==0:
        print(f"{personagem.name} está morto e não pode ser alimentado.")
        return
    if isinstance(personagem, Heroi):
        personagem.incremento(2)
    elif isinstance(personagem, Vilao):
        personagem.incremento(3)
    print(f"{personagem.name} foi alimentado e agora tem {personagem.energy} de energia.")

def interagir(personagens):
    name1=input("Digite o nome do personagem que iniciará a interação: ").strip()
    name2=input("Digite o nome do personagem alvo da interação: ").strip()
    p1=next((p for p in personagens if p.name==name1), None)
    p2=next((p for p in personagens if p.name==name2), None)
    if not p1 or not p2:
        print("Um ou ambos os personagens não foram encontrados.")
        return
    p1.interagir(p2)

if __name__=="__main__":
    menu()
