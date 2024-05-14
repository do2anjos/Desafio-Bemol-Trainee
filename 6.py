def tam_ord (str_list):
  return sorted(str_list, key=len)

str_list = ["Bemol","Escolha", "Com", "Confiança"]

list_ord = tam_ord(str_list)
print("A Lista é",list_ord)