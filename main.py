import os
import random
import time
import sys
import event

hpmax = 0
hp = 0
atk = 0
shld = 0
while True:
    turno=1
    print()
    os.system('cls' if os.name=='nt' else 'clear')
    print("jogar ou sair? [J/s]")
    jogarousair=str(input(">_ "))
    if jogarousair == "" or jogarousair == "j" or jogarousair == "J":
        print("escolha seu nome.")
        escolhanome=input(">_ ")
        print("agora escolha uma classe.")
        print("""
    # *humano [1]               #
    #                           #
    # *vida max. 100            #
    # *vida 80                  #
    # *ataque 10                #
    # *defesa 5                 #
    #                           #

    #                           #
        """)
        hpmax=100
        hp=80
        atk=10
        shld=5
        escolhaclasse=input("[1] >_ ")
        print("escolha um extra.")
        print("""
    # *extra 1                  ## *extra 2                  ## *extra 3                  #
    #                           ##                           ##                           #
    # *vida max +50             ## *vida max -50             ## *vida max +100            #
    # *vida +30                 ## *vida -30                 ## *vida +90                 #
    # *ataque -4                ## *ataque +6                ## *ataque -5                #
    # *defesa +2                ## *defesa -1                ## *defesa +4                #
    #                           ##                           ##                           #

    #                           ##                           ##                           #
        """)
        escolhaextra=input("[1/2/3] >_ ")
        if escolhaextra == "1":
            classe="extra 1"
            hpmax+=50
            hp+=30
            atk-=4
            shld+=2
        elif escolhaextra == "2":
            classe="extra 2"
            hpmax-=50
            hp-=30
            atk+=6
            shld-=1
        elif escolhaextra == "3":
            classe="extra 3"
            hpmax+=100
            hp+=90
            atk-=5
            shld+=4
        else:
            print("escolha invalida")
            continue
        inventario=[]
        while hp > 0 and hpmax > 0:
            if hp > hpmax:
                hp = hpmax
            os.system('cls' if os.name=='nt' else 'clear')
            print(f"=====================")
            print(f"$ nome = {escolhanome}")
            print(f"$ classe = {escolhaextra}")
            print(f"$ turno = {turno}")
            print(f"$ vida = ({hp}/{hpmax})")
            print(f"$ ataque = {atk}")
            print(f"$ defesa = {shld}")
            print(f"$ inventario = {inventario}")
            print(f"=====================")
            print()
            print("ir para esquerda [e] ou direita [d]?")
            eventos=["evento_1", "evento_2", "evento_3", "evento_4", "evento_5", "evento_6", "evento_7", "evento_8", "evento_9", "evento_10", "evento_1", "evento_2", "evento_3", "evento_4", "evento_5", "evento_6", "evento_7", "evento_8", "evento_9", "evento_10", "evento_11", "evento_12", "evento_13", "evento_14", "evento_15", "evento_16"]
            esquerda=random.choice(eventos)
            direita=random.choice(eventos)
            ladocontinuar = input("[e/d] >_ ").strip().lower()
            if ladocontinuar == "e":
                evatual=esquerda
            elif ladocontinuar == "d":
                evatual=direita
            else:
                continue
            print()
            hp_antes = hp
            hp, atk, shld, hpmax, inventario = event.eventos_map[evatual](hp, atk, shld, hpmax, turno, inventario)
            if escolhaextra == "2" and hp <= 0 and hp_antes > 1:
                hp = 1
                print("\nvocê sobrevive por pouco!")
            input("\npressione enter para continuar...")
            turno += 1
        if hp <= 0:
            print(r"""
               ('-.     _   .-')       ('-.                           (`-.      ('-.  _  .-')   
              ( OO ).-.( '.( OO )_   _(  OO)                        _(OO  )_  _(  OO)( \( -O )  
  ,----.      / . --. / ,--.   ,--.)(,------.       .-'),-----. ,--(_/   ,. \(,------.,------.  
 '  .-./-')   | \-.  \  |   `.'   |  |  .---'      ( OO'  .-.  '\   \   /(__/ |  .---'|   /`. ' 
 |  |_( O- ).-'-'  |  | |         |  |  |          /   |  | |  | \   \ /   /  |  |    |  /  | | 
 |  | .--, \ \| |_.'  | |  |'.'|  | (|  '--.       \_) |  |\|  |  \   '   /, (|  '--. |  |_.' | 
(|  | '. (_/  |  .-.  | |  |   |  |  |  .--'         \ |  | |  |   \     /__) |  .--' |  .  '.' 
 |  '--'  |   |  | |  | |  |   |  |  |  `---.         `'  '-'  '    \   /     |  `---.|  |\  \  
  `------'    `--' `--' `--'   `--'  `------'           `-----'      `-'      `------'`--' '--' 
            """)
            print(f"\nvocê morreu no turno {turno}.")
            input("pressione enter para continuar...")
    else:
        sys.exit("ok")
    time.sleep(5)
