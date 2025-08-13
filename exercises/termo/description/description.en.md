---

## Termo

---

### Regras

* Formem grupos de até três participantes (evitem fazer sozinhos, em hipótese alguma superem o máximo de três).
* A primeira linha do seu código deve ser um comentário (começando com `#`) contendo o nome dos integrantes do grupo. Só serão pontuados os integrantes que estiverem discriminados no código de maior pontuação do grupo.
* Seu código deve receber como **primeiro input** a semente do gerador aleatório (`random.seed`) e, a partir dela, sortear a palavra a ser adivinhada.
* O jogo deve continuar solicitando palpites até que o usuário acerte a palavra.
* A cada palpite, o código deve indicar:

  * `@` para letra correta na posição correta.
  * `*` para letra que existe na palavra, mas em outra posição.
  * `_` para letra que não existe na palavra.
* Ao final, imprima a palavra correta.
* Você pode enviar (inclusive para testes) quantas vezes quiser seu trabalho; só avaliarei a versão que te render mais pontos.

---

### Contexto

O **Termo** é um jogo de adivinhação de palavras onde, a cada tentativa, o jogador recebe dicas sobre quais letras estão corretas e suas posições. Nesta tarefa, vamos implementar uma versão simples do Termo em Python, controlando a aleatoriedade por meio de uma semente fixa para garantir resultados reproduzíveis nos testes automáticos.

---

### Tarefa

1. **Importe a biblioteca**:

```console?lang=python&prompt=>>>
import random
```

2. **Leia a semente** e configure o gerador aleatório:

```console?lang=python&prompt=>>>
semente = input()
semente = int(semente)
random.seed(semente)
```

3. **Defina a lista de palavras**:

```console?lang=python&prompt=>>>
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
```

4. **Sorteie a palavra**:

```console?lang=python&prompt=>>>
palavra = random.choice(palavras)
```

5. **Controle de vitória**:

```console?lang=python&prompt=>>>
venceu = False
```

6. **Laço de tentativas**:

**Parte 1 – Teste de vitória:**

```console?lang=python&prompt=>>>
while venceu == False:
    palpite = input()
    if palpite == palavra:
        venceu = True
```

**Parte 2 – Entrada no `else`:**

```console?lang=python&prompt=>>>
    else:
        retorno = ''
```

**Parte 3 – Uso do `enumerate` (dividido em subpartes):**

**3.1 – Cabeçalho do `for` com `enumerate`:**

```console?lang=python&prompt=>>>
        for posicao, letra in enumerate(palpite):
```

**3.2 – Condição `if` (letra na posição correta):**

```console?lang=python&prompt=>>>
            if letra == palavra[posicao]:
                retorno = retorno + '@'
```

**3.3 – Condição `elif` (letra existe, mas em outra posição):**

```console?lang=python&prompt=>>>
            elif letra in palavra:
                retorno = retorno + '*'
```

**3.4 – Condição `else` (letra não existe na palavra):**

```console?lang=python&prompt=>>>
            else:
                retorno = retorno + '_'
```

**3.5 – Impressão do retorno após o `for`:**

```console?lang=python&prompt=>>>
        print(retorno)
```

7. **Exiba a palavra correta**:

```console?lang=python&prompt=>>>
print(palavra)
```



## Exemplo 1

### Entradas

```console?lang=python&prompt=>>>
42
xxxxx
amigo
perda
```

### Saída

```console?lang=python&prompt=>>>
_____
*____
perda
```

---

## Exemplo 2

### Entradas

```console?lang=python&prompt=>>>
7
tempo
vento
dente
```

### Saída

```console?lang=python&prompt=>>>
*@___
_@@@_
dente
```

