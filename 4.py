import numpy as np

def fibo(n):
  fibo_seq = np.zeros(n)
  fibo_seq[0] = 1
  fibo_seq[1] = 1
  for i in range(2,n):
    fibo_seq[i] = fibo_seq[i-1] + fibo_seq[i-2]
  return fibo_seq
  
p_10_fibo = fibo(10)
print(p_10_fibo)