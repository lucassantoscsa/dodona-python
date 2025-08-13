import random
semente = input()
semente = int(semente)
random.seed(semente)
palavras = [ 
    "amigo", "certo", "livro", "carro", "terra", "festa", "piano", "gente",
    "tempo", "nuvem", "casal", "fruto", "navio", "pedra", "roupa", "viver",
    "cinto", "bravo", "leite", "sabor", "verde", "pente", "pleno", "vento",
    "campo", "couro", "somar", "troca", "folha", "claro", "prato", "sede",
    "firme", "cheio", "nobre", "areia", "lapis", "corte", "velho", "tocar",
    "resto", "dente", "papel", "corpo", "beijo", "curva", "largo", "salto",
    "farol", "falar", "linha", "forno", "muita", "natal", "vazio", "andar",
    "chave", "casco", "signo", "trigo", "manga", "lenda", "salva", "luzir",
    "ponto", "puxar", "fluir", "matar", "cansa", "dobro", "burro", "atual",
    "morar", "garra", "morro", "clube", "ciclo", "bolsa", "marca", "junta",
    "vasto", "perda", "poeta", "dizer", "lutar", "balde", "turma", "pular",
    "norte", "sulco", "fugir", "curar", "risco", "arroz", "banco", "vinho",
    "trono", "porta", "couro", "plano", "sinto", "cobre"
]
palavra = random.choice(palavras)
venceu = False
while venceu == False:
    palpite = input()
    if palpite == palavra:
        venceu = True
    else:
        retorno = ''
        for posicao, letra in enumerate(palpite):
            if letra == palavra[posicao]:
                retorno = retorno + '@'
            elif letra in palavra:
                retorno = retorno + '*'
            else:
                retorno = retorno + '_'
        print(retorno)
print(palavra)
