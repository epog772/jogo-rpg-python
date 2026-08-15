import random

def sorte(sorte):
    if random.random() < 0.10:
        print("--> uma reviravolta inesperada acontececeu.")
        return -sorte
    return sorte


def escalar(dano, turno):
    return max(1, int(dano * (1 + turno * 0.08)))


def reduzir_por_atk(dano, atk):
    return max(0, int(dano * max(0.2, 1 - atk * 0.02)))


def punicao_fuga(hp, atk, shld, hpmax, turno, inventario, chance=0.4):
    if random.random() < chance:
        tipo = random.choice(["vida", "ataque", "defesa"])
        if tipo == "vida":
            dano = escalar(random.randint(15, 35), turno)
            hp -= dano
            print(f"fugir não saiu barato... {-dano:+} de vida.")
        elif tipo == "ataque":
            perda = random.randint(3, 8)
            atk -= perda
            print(f"você perde confiança e força nos golpes. {-perda:+} de ataque.")
        else:
            perda = random.randint(2, 5)
            shld -= perda
            print(f"sua guarda fica comprometida. {-perda:+} de defesa.")
    else:
        print("você escapa ileso, dessa vez.")
    atk = max(1, atk)
    return hp, atk, shld, hpmax, inventario


def evento_1(hp, atk, shld, hpmax, turno, inventario):
    print("você encontra uma fonte brilhante no meio do caminho.")
    print("[1] beber da fonte")
    print("[2] ignorar e seguir em frente")
    escolha = input(">_ ").strip()
    if escolha == "1":
        cura = sorte(random.randint(10, 25))
        hp += cura
        print(f"você se sente {'revigorado' if cura >= 0 else 'enfraquecido'}. {cura:+} de vida.")
    else:
        print("você segue seu caminho sem se arriscar.")
        hp, atk, shld, hpmax, inventario = punicao_fuga(hp, atk, shld, hpmax, turno, inventario)
    atk = max(1, atk)
    return hp, atk, shld, hpmax, inventario


def evento_2(hp, atk, shld, hpmax, turno, inventario):
    print("um bandido salta das sombras!")
    print("[1] lutar")
    print("[2] fugir")
    escolha = input(">_ ").strip()
    if escolha == "1":
        dano = escalar(sorte(max(0, random.randint(5, 20) - shld)), turno)
        dano = reduzir_por_atk(dano, atk)
        ganho_atk = sorte(random.randint(1, 3))
        hp -= dano
        atk += ganho_atk
        print(f"você venceu a luta. {-dano:+} de vida, {ganho_atk:+} de ataque.")
    else:
        dano = escalar(sorte(random.randint(5, 10)), turno)
        hp -= dano
        print(f"você foge. {-dano:+} de vida.")
        hp, atk, shld, hpmax, inventario = punicao_fuga(hp, atk, shld, hpmax, turno, inventario)
    atk = max(1, atk)
    return hp, atk, shld, hpmax, inventario


def evento_3(hp, atk, shld, hpmax, turno, inventario):
    print("um comerciante misterioso oferece uma troca.")
    print("[1] trocar vida max por ataque")
    print("[2] trocar ataque por defesa")
    print("[3] recusar")
    escolha = input(">_ ").strip()
    if escolha == "1":
        d_hpmax = sorte(-15)
        d_atk = sorte(5)
        hpmax += d_hpmax
        atk += d_atk
        print(f"{d_hpmax:+} vida max, {d_atk:+} ataque.")
    elif escolha == "2":
        d_atk = sorte(-3)
        d_shld = sorte(3)
        atk += d_atk
        shld += d_shld
        print(f"{d_atk:+} ataque, {d_shld:+} defesa.")
    else:
        print("você recusa a oferta e segue em frente.")
        hp, atk, shld, hpmax, inventario = punicao_fuga(hp, atk, shld, hpmax, turno, inventario)
    atk = max(1, atk)
    return hp, atk, shld, hpmax, inventario


def evento_4(hp, atk, shld, hpmax, turno, inventario):
    print("você encontra um local seguro para descansar.")
    print("[1] descansar (recupera vida, perde um turno)")
    print("[2] continuar andando")
    escolha = input(">_ ").strip()
    if escolha == "1":
        cura = sorte(random.randint(15, 30))
        hp += cura
        print(f"{cura:+} de vida.")
    else:
        print("você decide não perder tempo.")
        hp, atk, shld, hpmax, inventario = punicao_fuga(hp, atk, shld, hpmax, turno, inventario)
    atk = max(1, atk)
    return hp, atk, shld, hpmax, inventario


def evento_5(hp, atk, shld, hpmax, turno, inventario):
    print("uma criatura selvagem rosna na sua direção.")
    print("[1] atacar primeiro")
    print("[2] tentar se defender")
    print("[3] correr")
    escolha = input(">_ ").strip()
    if escolha == "1":
        dano = escalar(sorte(max(0, random.randint(10, 25) - shld)), turno)
        dano = reduzir_por_atk(dano, atk)
        hp -= dano
        print(f"{-dano:+} de vida.")
    elif escolha == "2":
        dano = escalar(sorte(max(0, random.randint(5, 15) - shld * 2)), turno)
        dano = reduzir_por_atk(dano, atk)
        hp -= dano
        print(f"{-dano:+} de vida.")
    else:
        chance = random.random()
        if chance > 0.5:
            print("você consegue fugir sem se ferir.")
        else:
            dano = escalar(sorte(random.randint(10, 20)), turno)
            hp -= dano
            print(f"{-dano:+} de vida.")
        hp, atk, shld, hpmax, inventario = punicao_fuga(hp, atk, shld, hpmax, turno, inventario)
    atk = max(1, atk)
    return hp, atk, shld, hpmax, inventario


def evento_6(hp, atk, shld, hpmax, turno, inventario):
    print("você encontra uma encruzilhada com símbolos estranhos.")
    print("[1] seguir o caminho da esquerda (arriscado)")
    print("[2] seguir o caminho da direita (seguro)")
    escolha = input(">_ ").strip()
    if escolha == "1":
        if random.random() > 0.5:
            ganho = sorte(random.randint(10, 20))
            atk += ganho
            print(f"{ganho:+} de ataque.")
        else:
            dano = escalar(sorte(max(0, random.randint(10, 20) - shld)), turno)
            hp -= dano
            print(f"{-dano:+} de vida.")
    else:
        print("nada de interessante acontece, mas você está a salvo.")
        hp, atk, shld, hpmax, inventario = punicao_fuga(hp, atk, shld, hpmax, turno, inventario)
    atk = max(1, atk)
    return hp, atk, shld, hpmax, inventario


def evento_7(hp, atk, shld, hpmax, turno, inventario):
    print("um curandeiro viajante oferece ajuda.")
    print("[1] pedir cura")
    print("[2] pedir fortalecimento (defesa)")
    print("[3] ir embora")
    escolha = input(">_ ").strip()
    if escolha == "1":
        cura = sorte(random.randint(20, 40))
        hp += cura
        print(f"{cura:+} de vida.")
    elif escolha == "2":
        d_shld = sorte(3)
        shld += d_shld
        print(f"{d_shld:+} de defesa.")
    else:
        print("você agradece, mas segue seu caminho.")
        hp, atk, shld, hpmax, inventario = punicao_fuga(hp, atk, shld, hpmax, turno, inventario)
    atk = max(1, atk)
    return hp, atk, shld, hpmax, inventario


def evento_8(hp, atk, shld, hpmax, turno, inventario):
    print("um guerreiro rival te desafia para um duelo.")
    print("[1] aceitar o duelo")
    print("[2] recusar (perde reputação, sem efeito real)")
    escolha = input(">_ ").strip()
    if escolha == "1":
        dano = escalar(sorte(max(0, random.randint(15, 30) - shld)), turno)
        dano = reduzir_por_atk(dano, atk)
        hp -= dano
        if hp > 0:
            ganho = sorte(random.randint(2, 5))
            atk += ganho
            print(f"{-dano:+} de vida, {ganho:+} de ataque.")
        else:
            print(f"{-dano:+} de vida.")
    else:
        print("você recusa e segue seu caminho, um pouco humilhado.")
        hp, atk, shld, hpmax, inventario = punicao_fuga(hp, atk, shld, hpmax, turno, inventario)
    atk = max(1, atk)
    return hp, atk, shld, hpmax, inventario


def evento_9(hp, atk, shld, hpmax, turno, inventario):
    print("você encontra um poço antigo.")
    print("[1] jogar uma moeda e fazer um pedido")
    print("[2] ignorar")
    escolha = input(">_ ").strip()
    if escolha == "1":
        resultado = random.choice(["vida", "ataque", "defesa", "nada"])
        if resultado == "vida":
            d = sorte(10)
            hpmax += d
            hp += d
            print(f"{d:+} vida max, {d:+} vida.")
        elif resultado == "ataque":
            d_atk = sorte(3)
            atk += d_atk
            print(f"{d_atk:+} de ataque.")
        elif resultado == "defesa":
            d_shld = sorte(2)
            shld += d_shld
            print(f"{d_shld:+} de defesa.")
        else:
            print("nada acontece.")
    else:
        print("você não confia em poços estranhos.")
        hp, atk, shld, hpmax, inventario = punicao_fuga(hp, atk, shld, hpmax, turno, inventario)
    atk = max(1, atk)
    return hp, atk, shld, hpmax, inventario


def evento_10(hp, atk, shld, hpmax, turno, inventario):
    print("você pisa em uma armadilha de caçador escondida!")
    print("[1] tentar se soltar rapidamente")
    print("[2] se soltar com calma")
    escolha = input(">_ ").strip()
    if escolha == "1":
        dano = escalar(sorte(max(0, random.randint(10, 20) - shld)), turno)
        hp -= dano
        print(f"{-dano:+} de vida.")
    else:
        dano = escalar(sorte(max(0, random.randint(3, 8) - shld)), turno)
        hp -= dano
        print(f"{-dano:+} de vida.")
    atk = max(1, atk)
    return hp, atk, shld, hpmax, inventario


def evento_11(hp, atk, shld, hpmax, turno, inventario):
    print("você encontra uma árvore caída, cheia de madeira boa.")
    print("[1] coletar madeira")
    print("[2] ignorar")
    escolha = input(">_ ").strip()
    if escolha == "1":
        qtd = random.randint(1, 3)
        for aura in range(qtd):
            inventario.append("madeira")
        print(f"você coleta {qtd}x madeira.")
    else:
        print("você segue seu caminho.")
        hp, atk, shld, hpmax, inventario = punicao_fuga(hp, atk, shld, hpmax, turno, inventario)
    return hp, atk, shld, hpmax, inventario


def evento_12(hp, atk, shld, hpmax, turno, inventario):
    print("há um monte de pedras soltas no chão.")
    print("[1] coletar pedras")
    print("[2] ignorar")
    escolha = input(">_ ").strip()
    if escolha == "1":
        qtd = random.randint(1, 3)
        for rock_bottom in range(qtd):
            inventario.append("pedra")
        print(f"você coleta {qtd}x pedra.")
    else:
        print("você segue seu caminho.")
        hp, atk, shld, hpmax, inventario = punicao_fuga(hp, atk, shld, hpmax, turno, inventario)
    return hp, atk, shld, hpmax, inventario


def evento_13(hp, atk, shld, hpmax, turno, inventario):
    print("você avista ervas medicinais crescendo por perto.")
    print("[1] colher ervas")
    print("[2] ignorar")
    escolha = input(">_ ").strip()
    if escolha == "1":
        qtd = random.randint(1, 3)
        for tung in range(qtd):
            inventario.append("erva")
        print(f"você colhe {qtd}x erva.")
    else:
        print("você segue seu caminho.")
        hp, atk, shld, hpmax, inventario = punicao_fuga(hp, atk, shld, hpmax, turno, inventario)
    return hp, atk, shld, hpmax, inventario


def evento_14(hp, atk, shld, hpmax, turno, inventario):
    print("você encontra fragmentos de metal enferrujado, mas usável.")
    print("[1] coletar metal")
    print("[2] ignorar")
    escolha = input(">_ ").strip()
    if escolha == "1":
        qtd = random.randint(1, 2)
        for sahur in range(qtd):
            inventario.append("metal")
        print(f"você coleta {qtd}x metal.")
    else:
        print("você segue seu caminho.")
        hp, atk, shld, hpmax, inventario = punicao_fuga(hp, atk, shld, hpmax, turno, inventario)
    return hp, atk, shld, hpmax, inventario


def evento_15(hp, atk, shld, hpmax, turno, inventario):
    print("um brilho estranho chama sua atenção entre as pedras.")
    print("[1] investigar")
    print("[2] ignorar")
    escolha = input(">_ ").strip()
    if escolha == "1":
        if random.random() < 0.5:
            inventario.append("cristal")
            print("você encontra um cristal raro!")
        else:
            dano = escalar(random.randint(5, 15), turno)
            hp -= dano
            print(f"era uma armadilha. {-dano:+} de vida.")
    else:
        print("você segue seu caminho.")
        hp, atk, shld, hpmax, inventario = punicao_fuga(hp, atk, shld, hpmax, turno, inventario)
    return hp, atk, shld, hpmax, inventario


def evento_16(hp, atk, shld, hpmax, turno, inventario):
    print("você para para trabalhar nos materiais que carrega.")
    print(f"inventário: {inventario if inventario else 'vazio'}")
    print("[1] poção de cura (2x erva) -> +25 vida")
    print("[2] placa de metal (2x metal) -> +3 defesa")
    print("[3] pedra de amolar (2x pedra) -> +3 ataque")
    print("[4] amuleto de cristal (1x cristal + 2x madeira) -> +20 vida max")
    print("[5] não craftar nada")
    escolha = input(">_ ").strip()

    def tem(item, qtd):
        return inventario.count(item) >= qtd

    def gastar(item, qtd):
        for _ in range(qtd):
            inventario.remove(item)

    if escolha == "1" and tem("erva", 2):
        gastar("erva", 2)
        hp += 25
        print("você crafta uma poção de cura. +25 vida.")
    elif escolha == "2" and tem("metal", 2):
        gastar("metal", 2)
        shld += 3
        print("você crafta uma placa de metal. +3 defesa.")
    elif escolha == "3" and tem("pedra", 2):
        gastar("pedra", 2)
        atk += 3
        print("você crafta uma pedra de amolar. +3 ataque.")
    elif escolha == "4" and tem("cristal", 1) and tem("madeira", 2):
        gastar("cristal", 1)
        gastar("madeira", 2)
        hpmax += 20
        print("você crafta um amuleto de cristal. +20 vida max.")
    elif escolha == "5":
        print("você guarda seus materiais para depois.")
    else:
        print("você não tem materiais suficientes para isso.")

    return hp, atk, shld, hpmax, inventario

eventos_map = {
    "evento_1": evento_1,
    "evento_2": evento_2,
    "evento_3": evento_3,
    "evento_4": evento_4,
    "evento_5": evento_5,
    "evento_6": evento_6,
    "evento_7": evento_7,
    "evento_8": evento_8,
    "evento_9": evento_9,
    "evento_10": evento_10,
    "evento_11": evento_11,
    "evento_12": evento_12,
    "evento_13": evento_13,
    "evento_14": evento_14,
    "evento_15": evento_15,
    "evento_16": evento_16,
}
