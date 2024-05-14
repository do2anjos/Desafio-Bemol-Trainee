def maior_idade(idade1,idade2):
  if idade1 > idade2:
    return idade1
  else: 
    return idade2

idade1 =  int(input("insira a idade1:"))
idade2 =  int(input("insira a idade2:"))

maior = maior_idade(idade1,idade2)
print ("a maior idade é:", maior)
