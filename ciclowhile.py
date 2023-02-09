#cliclo while: se ejecuta hasta que la condicion sea falsa
"""x = 0
while x <=10:#Asi es para Aumentar la candidad Asignada
  print(x)
  x+=1"""

"""x = 10
while x >0:#Asi es para Disminuir la candidad Asignada
  print(x)
  x-=1"""

  #while con if, break, continue
"""num = 0
while num <=8:
  print(num)
  num+=1
  if num == 6:
    break   #break: rompe un ciclo
"""

num = 0
while num <=8:
  num+=1
  if num == 6:
    continue #continue: continuan con el ciclo pero no tiene en cuenta el numero asignado
  print(num)