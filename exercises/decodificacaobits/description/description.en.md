## Código Binário

---

### Regras
* Formem grupos de até três participantes (evitem fazer sozinhos, em hipótese alguma superem o máximo de três)
* A primeira linha do seu código deve ser uma linha de comentário (começando com #) com o nome dos integrantes do grupo. Só serão pontuados os integrantes que estiverem discriminados ali no código de maior pontuação do grupo.
* Seu código deve solicitar um input em que constará a mensagem cifrada.
* Seu código deve imprimir a mensagem decifrada.
* Você pode enviar (inclusive para testes) quantas vezes quiser seu trabalho, só avaliarei a versão que te render mais pontos.

---

### Contexto

A comunicação digital que utilizamos diariamente, desde mensagens de texto até a navegação na internet, é fundamentalmente construída sobre um alicerce invisível: a **codificação em bits**. Cada imagem, som, caractere e instrução que seu computador processa é, na sua essência, uma sequência de **zeros e uns**, pulsos elétricos que representam o estado "ligado" ou "desligado". Essa linguagem binária permite que máquinas complexas compreendam e executem tarefas com uma velocidade e precisão incríveis.

A capacidade de converter informações de um formato compreensível por humanos para um formato legível por máquinas, e vice-versa, é o cerne da ciência da computação e da tecnologia moderna. Sem a codificação eficiente de dados, a era digital como a conhecemos simplesmente não existiria. É um processo fascinante que nos permite traduzir o mundo físico para o mundo digital.

---

### Tarefa

Sua tarefa é criar um código que decifre uma mensagem transmitida em **código binário de 8 bits**. Cada sequência de 8 bits representa um caractere, sendo que consideraremos `00000000` como o **espaço** em branco. A mensagem será escrita considerando apenas letras minúsculas, sem acentos gráficos ou caracteres especiais.

Para as letras minúsculas, a codificação segue um padrão específico:

* Todas as letras minúsculas começam com `011`.
* Após o `011`, os números binários crescem sequencialmente, representando a posição da letra no alfabeto (começando de 1 para 'a', 2 para 'b', e assim por diante, até 26 para 'z').

**Exemplos:**

* **'a'**: É a primeira letra do alfabeto. O número binário para 1 é `000001`. Portanto, o código binário completo para 'a' é `01100001`.
* **'b'**: É a segunda letra do alfabeto. O número binário para 2 é `000010`. Portanto, o código binário completo para 'b' é `01100010`.
* **'z'**: É a vigésima sexta letra do alfabeto. O número binário para 26 é `011010`. Portanto, o código binário completo para 'z' é `01111010`.

**Dicas:**

1.  Crie uma **lista Python** que contenha todos os caracteres que você precisará para decodificar a mensagem. Comece com o **espaço em branco** (`' '`) na primeira posição (índice 0), seguido pelas letras minúsculas do alfabeto em ordem alfabética (`'a'`, `'b'`, `'c'`, ..., `'z'`).
2.  Recrie a função `base_n` (que criamos em nossa última aula e converte um número - e você escolherá a base 2 - para sua representação decimal) para determinar a **posição** da letra correspondente a cada código binário. Lembre-se de que a parte relevante do código para a posição da letra é a parte **após o `011`**. Por exemplo, para `01100001`, você usaria `000001` na função `base_n`. O resultado dessa conversão para `000001` é 1, que indica a posição da letra 'a' se a sua lista começar com 'a' no índice 1. Se sua lista começar com o espaço no índice 0, 'a' estará no índice 1.
A função base_n está definida abaixo, lembre-se de entendê-la.
```console?lang=python&prompt=>>>
def base_n(numero,base):
&nbsp;&nbsp;&nbsp;&nbsp;potencia = 0
    resultado = 0
    for algarismo in numero[::-1]:
        resultado = resultado+int(algarismo)*base**potencia
        potencia = potencia+1
    return resultado
```
3. Lembre que você terá que dividir a mensagem cifrada em pedaços de oito caracteres, antes de pensar na conversão, foque nisso. Para isso, lembre-se que você pegará todos os intervalos de tamanho 8 que se iniciam em posições múltiplas de 8 na mensagem (se a mensagem for `0110111101101001`, você deverá ser capaz de dividí-la em `01101111` e `01101001`). Utilize o for e atente-se à dica de que estamos pulando de 8 em 8 o início do nosso "corte".
4. Quando já estiver conseguindo dividir sua mensagem e imprimir as sequências de bits separadamente, comece a se preocupar em decifrar a mensagem. Crie uma variável cujo dado seja uma string vazia. Isole os 5 últimos termos de cada sequência e busque na lista qual caractere deveria estar naquela posição. Atualize sua variável concatenando esse caractere a ela. No final, seu print será o valor final dessa variável.

**Lembrete:**

* Preste atenção à ordem dos elementos em sua lista.
* Considere como a função `base_n` se relaciona com os índices da sua lista de caracteres.



---

## Exemplo 1
### Entradas
```console?lang=python&prompt=>>>
01101000011011110110101001100101000000000110010101110011011101000110000100000000011101010110110100000000011001000110100101100001000000000110110001101001011011010111000001101111
```
### Saída
```console?lang=python&prompt=>>>
hoje esta um dia limpo
```

## Exemplo 2
### Entradas
```console?lang=python&prompt=>>>
011000100110111101100001000000000111010001100001011100100110010001100101
```
### Saídas
```console?lang=python&prompt=>>>
boa tarde
```

## Exemplo 3
### Entradas
```console?lang=python&prompt=>>>
0110111101101001
```
### Saída
```console?lang=python&prompt=>>>
oi
```
