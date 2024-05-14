def rev_vo (text):
  vogais = "aeiouAEIOU"
  text_sem_v = ""
  for letra in text:
    if letra not in vogais:
      text_sem_v += letra
  return text_sem_v

text = "A vida é bela"
text_sem_v = rev_vo(text)
print("sua palavra sem vogais é:",text_sem_v)