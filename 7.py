def p_l_r(str):
  cont = {} 

  for char in str:
      if char in cont:
          cont[char] += 1
      else:
          cont[char] = 1

  for char, count in cont.items():
      if count == 1:
          return char

palavra = input("Digite sua palavra: ")

p_n_r = p_l_r(palavra)

if p_n_r:
  print("A primeira letra não repetida é:", p_n_r)
else:
  print("Não há repetidas")