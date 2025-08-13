vencedor =[]
for i in range(20):
  piloto = input()
  piloto = piloto.split(';')
  piloto[3:] = [int(tempo) for tempo in piloto[3:]]
  if sum(vencedor[3:])==0:
      vencedor = piloto
  elif sum(vencedor[3:])>sum(piloto[3:]):
      vencedor = piloto
vencedor[3:] = [str(tempo) for tempo in vencedor[3:]]
print(",".join(vencedor))
