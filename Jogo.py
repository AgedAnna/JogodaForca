import random

palavras = ["python", "java", "ruby","php","javascript"]
chance = 6
letras = []

palavra_sorteada = random.choice(palavras)

while True:
    quantidade_de_letras = ""
    for letra in palavra_sorteada:
        if letra in letras:
            quantidade_de_letras += letra + " "
        else:
            quantidade_de_letras += "_ "

    print("----BEM - VINDO !----")
    print("  AO JOGO DA FORCA    ")
    print("TENTE ADIVINHAR A LINGUAGEM: ")

    bonequinho = [
            "   _________",
            "   |/      |",
            "   |      (_)",
            "   |      \\|/",
            "   |       |",
            "   |      / \\",
            "___|___"
    ]

    for linha in bonequinho:
        print(linha)

    print(quantidade_de_letras)
    print("")

    tentativa = input("Digite uma letra: ").lower()

    letras.append(tentativa)

    if tentativa not in palavra_sorteada:
        chance -= 1
        print("Você errou! Tente novamente.")

    if chance == 0:
        print("Perdeu. A palavra era:", palavra_sorteada)
        break

    if all(letra in letras for letra in palavra_sorteada):
        print("Parabéns! Você acertou a palavra.")
        break

    descobriu_palavra = input("Você já descobriu a palavra? (s/n): ").lower()

    if descobriu_palavra == "s":
        palavra_tentativa = input("Digite a palavra: ").lower()
        if palavra_tentativa == palavra_sorteada:
            print(f"Que massa! Você acertou, a palavra era: { palavra_sorteada}")
            break
        else:
            print(f"Que pena! Você perdeu, a palavra era: { palavra_sorteada}")
            break
