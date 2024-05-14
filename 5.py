def primo(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

n = int(input("insira um número:"))
if primo(n):
    print(n, "é um número primo")
else:
    print(n, "nao é um número primo")