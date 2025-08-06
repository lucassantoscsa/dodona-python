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
    sua_lista[3:] = [int(tempo) for tempo in sua_lista[3:]]
```
4. Um lista fatiada ainda é uma lista, então a função `sum` serve para ela.
5. Compare a soma dos tempos do piloto analisado à soma dos tempos do piloto que está como vencedor na sua variável.
    * Se o piloto que está como vencedor tem tempo total igual a zero, considere que qualquer piloto é melhor do que ele.
    * Se o piloto que está sendo analisado tem tempo total menor do que o piloto que está como vencedor, ele é o novo vencedor.
6. Após definir o piloto vencedor, use o seguinte código para transformar os dados numéricos em texto antes de usar o `join` para juntá-los e imprimí-los.
```console?lang=python&prompt=>>>
    sua_lista[3:] = [str(tempo) for tempo in sua_lista[3:]]
```

---

## Exemplo 1
### Entradas
```console?lang=python&prompt=>>>
George Russell;63;Mercedes;270478
Lance Stroll;18;Aston Martin-Mercedes;270479
Esteban Ocon;31;Haas-Ferrari;135409;135411
Lewis Hamilton;44;Ferrari;90168;90385;90462
Alexander Albon;23;Williams-Mercedes;135153;135345
Charles Leclerc;16;Ferrari;270473
Isack Hadjar;6;Racing Bulls-Honda RBPT;270374
Gabriel Bortoleto;5;Kick Sauber-Ferrari;135393;135201
Franco Colapinto;43;Alpine-Renault;135402;135386
Andrea Kimi Antonelli;12;Mercedes;90350;90412;90401
Pierre Gasly;10;Alpine-Renault;135407;135293
Oliver Bearman;87;Haas-Ferrari;90140;90252;90133
Liam Lawson;30;Racing Bulls-Honda RBPT;90097;89985;90055
Nico Hülkenberg;27;Kick Sauber-Ferrari;90118;90183;90537
Carlos Sainz Jr.;55;Williams-Mercedes;90196;90429;90408
Lando Norris;4;McLaren-Mercedes;135478;135374
Max Verstappen;1;Red Bull Racing-Honda RBPT;90380;90119;90412
Oscar Piastri;81;McLaren-Mercedes;270366
Fernando Alonso;14;Aston Martin-Mercedes;90416;90131;90498
Yuki Tsunoda;22;Red Bull Racing-Honda RBPT;90536;90488;90536
```
### Saída
```console?lang=python&prompt=>>>
Liam Lawson,Racing Bulls-Honda RBPT,90097,89985,90055
```

## Exemplo 2
### Entradas
```console?lang=python&prompt=>>>
Yuki Tsunoda;22;Red Bull Racing-Honda RBPT;90223;90288;90128
Lewis Hamilton;44;Ferrari;135554;135197
Andrea Kimi Antonelli;12;Mercedes;270528
Esteban Ocon;31;Haas-Ferrari;135280;135388
Pierre Gasly;10;Alpine-Renault;90510;90270;90352
Charles Leclerc;16;Ferrari;90511;90305;90464
Lance Stroll;18;Aston Martin-Mercedes;90150;90336;90375
Oliver Bearman;87;Haas-Ferrari;90121;90424;90138
Carlos Sainz Jr.;55;Williams-Mercedes;135395;135534
Nico Hülkenberg;27;Kick Sauber-Ferrari;90201;90517;90532
George Russell;63;Mercedes;90470;90190;90178
Alexander Albon;23;Williams-Mercedes;90313;90496;90424
Lando Norris;4;McLaren-Mercedes;135262;135435
Franco Colapinto;43;Alpine-Renault;90493;90255;90117
Isack Hadjar;6;Racing Bulls-Honda RBPT;90362;90325;90200
Liam Lawson;30;Racing Bulls-Honda RBPT;90455;90341;90369
Gabriel Bortoleto;5;Kick Sauber-Ferrari;90393;90529;90447
Oscar Piastri;81;McLaren-Mercedes;90280;90461;90145
Fernando Alonso;14;Aston Martin-Mercedes;90344;90203;90196
Max Verstappen;1;Red Bull Racing-Honda RBPT;90096;90098;89953
```
### Saída
```console?lang=python&prompt=>>>
Max Verstappen,1,Red Bull Racing-Honda RBPT,90096,90098,89953
```


