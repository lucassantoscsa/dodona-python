## Corrida de Fórmula 1

---

### Regras
* Formem grupos de até três participantes (evitem fazer sozinhos, em hipótese alguma superem o máximo de três)
* A primeira linha do seu código deve ser uma linha de comentário (começando com #) com o nome dos integrantes do grupo. Só serão pontuados os integrantes que estiverem discriminados ali no código de maior pontuação do grupo.
* Seu código deve solicitar 20 inputs em que constará o resultado de cada piloto (use um `for` ou `while` para isso). Cada input será da seguinte forma: `'PILOTO;NÚMERO;EQUIPE;T_V1;T_V2;...;T_VN'`.
* Seu código deve imprimir o nome do piloto vencedor, sua equipe em quantos milésimos de segundo ele gastou para concluir cada volta, separados por *vírgula*.
* Você pode enviar (inclusive para testes) quantas vezes quiser seu trabalho, só avaliarei a versão que te render mais pontos.

---

### Contexto

Em uma corrida de Fórmula 1, os carros são equipados com equipamentos capazes de registrar o momento exato em que eles passam pela linha de chegada. Através da medição do equipamento, a organização da prova consegue computar o tempo que o piloto gastou em cada volta e o vencedor da corrida é aquele que gastou menos tempo no total para dar todas as voltas da prova.


---

### Tarefa

Sua tarefa é criar um código que leia os resultados de cada piloto em uma corrida e informe o piloto vencedor com seu tempo, em milésimos de segundo por volta.

**Dicas:**

1.  Analise piloto a piloto até o final usando o `for` que você usou para receber os `inputs`.
2.  Antes do `for`, crie uma variável, que será uma lista vazia, para você salvar o piloto vencedor até aquele momento.
3.  Após dividir as informações do piloto na lista, use o seguinte código para transformar o tempo de cada volta em um número inteiro:
```console?lang=python&prompt=>>>
    sua_lista[2:] = [int(tempo) for tempo in sua_lista[2:]]
```
4. Um lista fatiada ainda é uma lista, então a função `sum` serve para ela.
5. Compare a soma dos tempos do piloto analisado à soma dos tempos do piloto que está como vencedor na sua variável.
    * Se o piloto que está como vencedor tem tempo total igual a zero, considere que qualquer piloto é melhor do que ele.
    * Se o piloto que está sendo analisado tem tempo total menor do que o piloto que está como vencedor, ele é o novo vencedor.
6. Após definir o piloto vencedor, use o seguinte código para transformar os dados numéricos em texto antes de usar o `join` para juntá-los e imprimí-los.
```console?lang=python&prompt=>>>
    sua_lista[2:] = [str(tempo) for tempo in sua_lista[2:]]
```

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
