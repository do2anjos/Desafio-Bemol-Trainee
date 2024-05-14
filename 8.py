  def fat(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

  n = int(input("Insira um número: "))
  print('O fatorial de', n, 'é', fat(n))