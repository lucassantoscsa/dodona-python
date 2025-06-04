n = int(input())
cond = 0
if n/7 == int(n/7):
    cond = cond+1
if n/2 != int(n/2) and n<=70 and n>=30:
    cond = cond+1
if n/10 == int(n/10) and n/3!= int(n/3):
    cond = cond+1
if cond >= 2:
    print("Especial")
elif cond >= 1:
    print("Semiespecial")
else:
    print("Comum")