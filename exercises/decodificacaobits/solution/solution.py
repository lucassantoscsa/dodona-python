mensagem = input()
alfabeto = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def base_n(numero,base):
    potencia = 0
    resultado = 0
    for algarismo in numero[::-1]:
        resultado = resultado+int(algarismo)*base**potencia
        potencia = potencia+1
    return resultado
decifrada = ""
for posicao in range(int(len(mensagem)/8)):
    seq = mensagem[posicao*8:posicao*8+8]
    caractere = alfabeto[base_n(seq[3:],2)]
    decifrada = decifrada+caractere
print(decifrada)